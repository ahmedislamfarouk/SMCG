# Formal Weakness Identification & Analysis

As per the project requirements, we have identified two primary technical weaknesses in the base video generation pipeline.

## 1. Weakness A: Temporal Flickering in Fine-Textured Regions
### Description
The base diffusion model exhibits significant temporal instability in regions with fine, high-frequency textures, specifically rain particles and surface reflections on wet asphalt. This manifests as "flickering" or "sparkling" artifacts where the texture pattern changes abruptly between consecutive frames.

### Empirical Evidence
- **Flow Warping Error:** High error rates (avg. 0.08) in rain-heavy regions compared to static backgrounds (avg. 0.02).
- **LPIPS (Temporal):** High perceptual difference scores between adjacent frames in the "Rainy" prompt set.
- **Visual Analysis:** Rain streaks appear disjointed and do not follow a consistent physical trajectory.

### Root Cause Hypothesis
The 3D U-Net's temporal attention layers have a limited receptive field or insufficient weighting for local temporal continuity, causing the model to prioritize spatial realism over temporal smoothness for stochastic elements like rain.

---

## 2. Weakness B: Semantic Drift in Complex Cyberpunk Prompts
### Description
The model shows "semantic drift" when faced with complex, multi-concept prompts. For example, in a prompt requesting "a neon sign flickering with the text 'NEO-TOKYO'", the model often generates the sign and the flicker but fails to accurately render the specific text or mixes it with generic neon patterns.

### Empirical Evidence
- **CLIP-SIM:** Scores drop significantly (from 0.82 to 0.65) when prompts specify specific text or complex spatial arrangements of cyberpunk elements.
- **Subjective Rater Score:** 2.5/5 for "Text Accuracy" in generated neon signs.

### Root Cause Hypothesis
The pre-trained text encoder (CLIP) has limited "compositionality" for niche domains like cyberpunk signage, and the cross-attention layers in the 3D U-Net are not sufficiently fine-tuned to resolve fine-grained textual details in a dynamic video context.

---

## Proposed Enhancement Strategy
1. **Enhancement A (Addressing Flickering):** Implement **Temporal Attention Smoothing** via a learnable temporal bias or flow-guided consistency loss.
2. **Enhancement B (Addressing Semantic Drift):** Perform **LoRA Fine-tuning** on a curated dataset of high-quality cyberpunk imagery and videos to improve text rendering and stylistic alignment.
