# SMCG: Short Movie Clip Generation

This project implements a high-fidelity text-to-video generation pipeline powered by **Latent Video Diffusion (LVD)** models. The focus is on producing temporally coherent, aesthetically striking video clips based on a "Cyberpunk Rainy Neon Cityscape" theme.

## 🚀 Project Overview
The system utilizes a **3D U-Net** architecture with **Temporal Attention** mechanisms to solve the core challenge of temporal consistency in video generation. By operating in the latent space of a pre-trained VAE, the pipeline achieves high-quality results with manageable computational overhead.

## 📁 Key Documentation
- **[THEME.md](./THEME.md):** Detailed conceptual foundation and vision for the "Cyberpunk Rainy Neon Cityscape" theme.
- **[MATH.md](./MATH.md):** Mathematical formulation of the Denoising Diffusion Probabilistic Model (DDPM), forward/reverse processes, and the score function.
- **[ARCHITECTURE.md](./ARCHITECTURE.md):** Deep dive into the 3D U-Net structure, attention mechanisms, and position encodings.

## 🛠️ Technical Implementation
- **Architecture:** 3D U-Net with integrated Spatial and Temporal Self-Attention.
- **Conditioning:** Text-to-video alignment via CLIP-based cross-attention.
- **Sampling:** Support for DDPM, DDIM, and DPM-Solver++ for varying speed-quality trade-offs.
- **Guidance:** Classifier-Free Guidance (CFG) for fine-tuning the trade-off between prompt alignment and sample diversity.

## 📊 Evaluation Suite
The project evaluates performance using both quantitative and qualitative metrics:
- **FVD (Fréchet Video Distance):** Measures overall visual quality and temporal coherence.
- **CLIP-SIM:** Measures semantic alignment between the prompt and generated video.
- **SSIM/PSNR:** Frame-level quality assessment.
- **User Study:** Subjective realism and coherence rater scores.

## 📜 Assignment Requirements
This project fulfills the requirements for the **Selected Topics in AI 2 (AIE418)** final project at Alamein International University.

---
*Developed by Ahmed Islam Farouk*
