# Mathematical Foundation of Diffusion Models (DDPM)

## 1. Denoising Diffusion Probabilistic Models (DDPM)

Diffusion models generate data by reversing a process that adds noise to data. This involves two main processes: the **Forward Process** (diffusion) and the **Reverse Process** (denoising).

### 1.1 Forward Diffusion Process ($q$)
The forward process gradually adds Gaussian noise to a clean data point $x_0$ over $T$ steps, according to a variance schedule $\{\beta_t \in (0,1)\}_{t=1}^T$:

$$q(x_t | x_{t-1}) = \mathcal{N}(x_t; \sqrt{1 - \beta_t} x_{t-1}, \beta_t \mathbf{I})$$

As $t$ increases, $x_t$ becomes increasingly noisy until $x_T$ is nearly pure Gaussian noise. A key property of the forward process is that we can sample $x_t$ directly from $x_0$ using:

$$q(x_t | x_0) = \mathcal{N}(x_t; \sqrt{\bar{\alpha}_t} x_0, (1 - \bar{\alpha}_t) \mathbf{I})$$

where $\alpha_t = 1 - \beta_t$ and $\bar{\alpha}_t = \prod_{i=1}^t \alpha_i$.

### 1.2 Reverse Denoising Process ($p_\theta$)
The goal of the model is to learn the reverse process $p_\theta(x_{t-1} | x_t)$, which approximates the true (but unknown) reverse distribution $q(x_{t-1} | x_t)$. This is modeled as a Gaussian:

$$p_\theta(x_{t-1} | x_t) = \mathcal{N}(x_{t-1}; \mu_\theta(x_t, t), \sigma_t^2 \mathbf{I})$$

The model learns to predict the mean $\mu_\theta$ or, more commonly, the noise $\epsilon$ that was added to $x_t$.

---

## 2. Score Function Intuition
The score function $\nabla_x \log p(x)$ points in the direction where data density increases. In diffusion models, the noise prediction $\epsilon_\theta(x_t, t)$ is directly related to the score function of the noisy data distribution:

$$\nabla_{x_t} \log p(x_t) \approx - \frac{1}{\sqrt{1 - \bar{\alpha}_t}} \epsilon_\theta(x_t, t)$$

By learning to predict noise, the model implicitly learns the gradient of the log-density of the data, allowing it to "walk" from high-noise regions to low-noise (high-density) data regions.

---

## 3. Training Objective (ELBO to MSE)
The model is trained by maximizing the Evidence Lower Bound (ELBO) of the log-likelihood. For DDPM, this simplifies to a weighted Mean Squared Error (MSE) loss between the true noise $\epsilon$ and the predicted noise $\epsilon_\theta$:

$$\mathcal{L}_{simple}(\theta) = \mathbb{E}_{x_0, \epsilon, t} \left[ \| \epsilon - \epsilon_\theta(x_t, t) \|^2 \right]$$

This objective encourages the model to accurately reconstruct the original signal by predicting the noise component at each timestep $t$.

---

## 4. Noise Schedules
The variance schedule $\beta_t$ controls the rate of noise addition.
- **Linear Schedule:** $\beta_t$ increases linearly from $\beta_1$ to $\beta_T$. Simple but may add noise too quickly at the start or end.
- **Cosine Schedule:** Provides a smoother transition, often leading to better sample quality by preserving more information in the early stages of diffusion.

---

## 5. Temporal Consistency in Video
For video generation, $x$ is a sequence of frames $(f_1, f_2, \dots, f_F)$. Temporal coherence is achieved by:
1. **Temporal Attention:** Allowing each pixel at $(x, y, t)$ to attend to $(x, y, t')$ in other frames.
2. **3D Convolutions:** Applying kernels that span both spatial and temporal dimensions $(k \times k \times k_{temp})$.
3. **Motion Conditioning:** Explicitly conditioning the model on optical flow or motion vectors (optional but advanced).

Our implementation will focus on **3D U-Net** and **Temporal Attention** to maintain continuity across frames.
