# Architecture Deep Dive: 3D U-Net and Attention Mechanisms

The core of the Short Movie Clip Generation (SMCG) system is a **3D U-Net** based diffusion model, which extends spatial 2D diffusion architectures by incorporating a temporal dimension.

## 1. 3D U-Net Structure
The 3D U-Net follows an encoder-decoder structure with symmetric skip connections.

### 1.1 Encoder (Downsampling)
The encoder reduces the spatial resolution of the video frames while extracting high-level features.
- **3D Convolutional Layers:** $3 \times 3 \times 3$ kernels with padding to preserve temporal depth while reducing spatial dimensions.
- **ResNet Blocks:** Residual connections with 3D convolutions and Group Normalization (GN).
- **Downsampling:** Strided convolutions or pooling to reduce resolution (e.g., $128 \times 128 \rightarrow 64 \times 64 \rightarrow 32 \times 32$).

### 1.2 Bottleneck (Latent Space)
The bottleneck contains the most compressed representation of the video.
- **Self-Attention:** Spatial self-attention to capture long-range spatial dependencies.
- **Temporal Attention:** Captures dependencies between frames in the bottleneck.
- **Cross-Attention:** Injects text conditioning from the text encoder (CLIP/T5).

### 1.3 Decoder (Upsampling)
The decoder reconstructs the video frames from the latent representation.
- **3D Deconvolution/Upsampling:** Increases spatial resolution.
- **Skip Connections:** Concatenates features from the corresponding encoder stage to preserve fine-grained spatial details.
- **Refinement Blocks:** ResNet blocks and attention layers for high-fidelity reconstruction.

---

## 2. Attention Mechanisms
Attention is critical for both spatial detail and temporal coherence.

### 2.1 Spatial Self-Attention
Applied independently to each frame or feature map at a given timestep.
- **Function:** Relates pixels within a single frame to each other.
- **Formulation:** $Attention(Q, K, V) = softmax(\frac{QK^T}{\sqrt{d_k}}) V$, where $Q, K, V$ are linear projections of spatial features.

### 2.2 Temporal Self-Attention
Applied across the temporal dimension for each spatial location $(x, y)$.
- **Function:** Each pixel $(x, y)$ at frame $t$ attends to the same $(x, y)$ pixel in all other frames $\{1, \dots, F\}$.
- **Benefit:** Ensures that a specific object or texture remains consistent as it moves or changes across time.

### 2.3 Cross-Attention (Text Conditioning)
Relates video features to text embeddings from the text encoder.
- **Queries ($Q$):** Video features.
- **Keys ($K$) and Values ($V$):** Text embeddings (e.g., CLIP's last hidden state).
- **Function:** Guides the model to generate content that aligns with the natural language description.

---

## 3. Position Encodings
Since attention is permutation-invariant, we must inject information about the relative or absolute position of pixels and frames.

### 3.1 Spatial Position Encodings
- **Sinusoidal:** Standard 2D sinusoidal embeddings added to the feature maps.
- **Rotary Position Encodings (RoPE):** More advanced method for preserving relative spatial relationships (optional enhancement).

### 3.2 Temporal Position Encodings
- **1D Sinusoidal:** Added along the time axis to indicate frame order.
- **Relative Temporal Bias:** Learnable bias added to the attention weights to prioritize neighboring frames.

---

## 4. Latent Space vs. Pixel Space
Our system utilizes a **Latent Video Diffusion** approach:
1. **VAE Encoder:** Compresses the input video into a low-dimensional latent space ($H \times W \times F \rightarrow h \times w \times f \times c$).
2. **Diffusion Model:** Operates entirely within this latent space, significantly reducing computational cost.
3. **VAE Decoder:** Reconstructs the final pixel-space video from the denoised latents.
