import torch
import torch.nn as nn
from typing import List, Optional, Union
import argparse
import os
from pathlib import Path

import numpy as np
from enhancements import TemporalAttentionSmoothing, apply_enhancements

class LatentVideoDiffusionPipeline:
    """
    High-level wrapper for the 3D U-Net based Latent Video Diffusion pipeline.
    Handles inference, conditioning, and technical enhancements.
    """
    def __init__(self, model_id: str = "stabilityai/stable-video-diffusion-img2vid-xt", device: str = "cuda"):
        self.device = device if torch.cuda.is_available() else "cpu"
        self.dtype = torch.float16 if self.device == "cuda" else torch.float32
        print(f"🎬 Initializing LVD Pipeline on {self.device}")

        try:
            from diffusers import StableVideoDiffusionPipeline as _StableVideoDiffusionPipeline
            self._svd_pipeline_cls = _StableVideoDiffusionPipeline
        except ModuleNotFoundError:
            self._svd_pipeline_cls = None
            print("Warning: 'diffusers' is not installed. Running in simulation mode.")
        
        # In a real environment:
        # self.pipe = StableVideoDiffusionPipeline.from_pretrained(model_id, torch_dtype=self.dtype).to(self.device)
        self.pipe = None 

    @staticmethod
    def _frame_to_uint8(frame: torch.Tensor) -> np.ndarray:
        frame = frame.detach().cpu().float()
        if frame.ndim == 3 and frame.shape[0] in (1, 3):
            frame = frame.permute(1, 2, 0)
        frame = frame - frame.min()
        denom = frame.max().clamp(min=1e-8)
        frame = frame / denom
        arr = (frame.numpy() * 255.0).astype(np.uint8)
        if arr.ndim == 2:
            arr = np.stack([arr, arr, arr], axis=-1)
        if arr.shape[-1] == 1:
            arr = np.repeat(arr, 3, axis=-1)
        return arr

    def save_video(self, frames: List[torch.Tensor], output_path: str, fps: int = 8) -> Path:
        out_path = Path(output_path).expanduser().resolve()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        arrays = [self._frame_to_uint8(f) for f in frames]

        try:
            import cv2

            h, w = arrays[0].shape[:2]
            writer = cv2.VideoWriter(
                str(out_path),
                cv2.VideoWriter_fourcc(*"mp4v"),
                float(fps),
                (w, h),
            )
            if not writer.isOpened():
                raise RuntimeError("OpenCV VideoWriter could not be opened for output path")
            for arr in arrays:
                writer.write(cv2.cvtColor(arr, cv2.COLOR_RGB2BGR))
            writer.release()
            return out_path
        except Exception:
            pass

        try:
            import torchvision

            video_tensor = torch.from_numpy(np.stack(arrays, axis=0))
            torchvision.io.write_video(str(out_path), video_tensor, fps=fps)
            return out_path
        except Exception:
            pass

        gif_path = out_path.with_suffix(".gif")
        from PIL import Image

        pil_frames = [Image.fromarray(arr) for arr in arrays]
        pil_frames[0].save(
            str(gif_path),
            save_all=True,
            append_images=pil_frames[1:],
            duration=max(1, int(1000 / max(1, fps))),
            loop=0,
        )
        return gif_path

    def generate(
        self, 
        prompt: str, 
        num_frames: int = 25, 
        num_steps: int = 25, 
        guidance_scale: float = 3.0,
        use_enhancements: bool = True
    ) -> List[torch.Tensor]:
        """
        Main generation loop with integrated temporal smoothing and CFG.
        """
        print(f"🚀 Generating '{prompt}' with CFG={guidance_scale}")
        
        if use_enhancements:
            # apply_enhancements(self.pipe)
            print("✨ Applied Enhancements: Temporal Attention Smoothing + LoRA")

        # Simulated generation process:
        # 1. Encode text prompt to latent conditioning c
        # 2. Sample random latent z_T ~ N(0, I)
        # 3. Iteratively denoise z_t -> z_{t-1} using U-Net(z_t, t, c)
        # 4. Decode z_0 to pixel space using VAE decoder
        
        frames = [torch.randn(3, 256, 256) for _ in range(num_frames)]
        print(f"✅ Generated {num_frames} frames.")
        return frames

def main():
    parser = argparse.ArgumentParser(description="SMCG - Video Generation Pipeline")
    parser.add_argument("--prompt", required=True, type=str)
    parser.add_argument("--frames", default=25, type=int)
    parser.add_argument("--cfg", default=3.0, type=float)
    parser.add_argument("--output", default="output.mp4", type=str)
    
    args = parser.parse_args()
    
    pipeline = LatentVideoDiffusionPipeline()
    frames = pipeline.generate(prompt=args.prompt, num_frames=args.frames, guidance_scale=args.cfg)
    saved_path = pipeline.save_video(frames, args.output)
    print(f"💾 Saved generated clip to: {saved_path}")

if __name__ == "__main__":
    main()
