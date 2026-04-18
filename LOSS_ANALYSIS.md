# Loss Function Analysis

Diffusion models offer several ways to formulate the objective function. Each variant has different mathematical properties and impacts training stability and sample quality.

## 1. $\epsilon$-prediction (Noise Prediction)
This is the most common variant used in DDPM. The model aims to predict the noise $\epsilon \sim \mathcal{N}(0, \mathbf{I})$ added to the clean image $x_0$:

$$\mathcal{L}_\epsilon = \mathbb{E}_{x_0, \epsilon, t} \left[ \| \epsilon - \epsilon_\theta(x_t, t) \|^2 \right]$$

- **Pros:** High training stability across all timesteps $t$. Direct connection to the score function.
- **Cons:** Struggles with large-scale structures at low $t$ when $\bar{\alpha}_t \approx 0$.

## 2. $x_0$-prediction (Data Prediction)
The model directly predicts the original clean data $x_0$:

$$\mathcal{L}_{x_0} = \mathbb{E}_{x_0, \epsilon, t} \left[ \| x_0 - \hat{x}_{0,\theta}(x_t, t) \|^2 \right]$$

- **Pros:** Intuitive. Can produce sharper results at late stages of denoising.
- **Cons:** Highly unstable early in training ($t \approx T$) because $x_T$ is pure noise, making $x_0$ impossible to recover directly.

## 3. $v$-prediction (Velocity Prediction)
Introduced in Salimans & Ho (2022), the model predicts a target $v$ defined as:

$$v_t = \sqrt{\bar{\alpha}_t} \epsilon - \sqrt{1 - \bar{\alpha}_t} x_0$$

The loss is:
$$\mathcal{L}_v = \mathbb{E}_{x_0, \epsilon, t} \left[ \| v_t - v_\theta(x_t, t) \|^2 \right]$$

- **Pros:** Excellent for high-resolution video and large-scale temporal motion. It balances the signal-to-noise ratio effectively across all $t$.
- **Cons:** Slightly more complex to implement and analyze.

---

## 4. Choice for SMCG Project
Our model employs **$\epsilon$-prediction** because we utilize the Latent Video Diffusion (LVD) framework.
- **Justification:** Since we operate in the latent space of a pre-trained VAE, the manifold is already highly regularized. $\epsilon$-prediction provides the most stable convergence for these latent distributions and is the standard for the pre-trained SVD backbone we integrated.

---

## 5. Classifier-Free Guidance (CFG) Loss Modification
During inference, we modify the predicted noise $\epsilon_\theta$ to align better with the text prompt $c$:

$$\hat{\epsilon}_\theta(x_t, t, c) = \epsilon_\theta(x_t, t, \emptyset) + w \cdot (\epsilon_\theta(x_t, t, c) - \epsilon_\theta(x_t, t, \emptyset))$$

where $w$ is the guidance scale. This requires the model to be trained with **joint conditioning**, where the conditioning $c$ is randomly dropped (replaced by $\emptyset$) in 10-20% of training steps.
