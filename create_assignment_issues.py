#!/usr/bin/env python3
"""
Script to create restructured issues for the Short Movie Clip Generation (SMCG) project.
Usage: python create_assignment_issues.py --token YOUR_GITHUB_TOKEN --repo ahmedislamfarouk/SMCG
"""

import argparse
from github import Github

ISSUES = [
    {
        "title": "RESEARCH - Define Theme Selection & Conceptual Foundation",
        "body": """**Objective:** Define a compelling, creative, and meaningful theme to drive the Short Movie Clip Generation project.

**Subtasks:**
- Finalize a theme (e.g., "Cyberpunk Rainy Streets," "Ethereal Forest Creatures," "Abstract Fluid Dynamics").
- Document the theme's core elements: visual style, motion types, and emotional tone in THEME.md.
- Create a set of base prompts tailored to the theme for consistent testing.
- Explain how this theme will guide prompt engineering, scene generation, and evaluation in the final paper.

**Acceptance Criteria:**
- A `THEME.md` file detailing the theme, visual style, and sample prompts.
- A mood board or descriptive section in the README.
- 5-10 standardized prompts for benchmarking.

**Labels:** ["Phase 1", "Design"]
""",
        "labels": ["Phase 1", "Design"]
    },
    {
        "title": "MATH - Diffusion Process (DDPM) Mathematical Formulation",
        "body": """**Objective:** Document and explain the mathematical foundation of the Denoising Diffusion Probabilistic Model (DDPM) as applied to our project.

**Subtasks:**
- Explain the **Forward Process** ($q(x_t | x_{t-1})$): The Markovian addition of Gaussian noise.
- Explain the **Reverse Process** ($p_\\theta(x_{t-1} | x_t)$): The denoising step and the model's objective to estimate the signal.
- Document the **Score Function** intuition: $\\nabla_x \\log p(x)$ and its link to noise prediction.
- Derive/Explain the **Training Objective**: How the ELBO simplifies to a Mean Squared Error (MSE) loss on the predicted noise.

**Acceptance Criteria:**
- A `MATH.md` or a detailed section in the README with LaTeX equations.
- Clear intuition provided for the forward/reverse processes.
- Connection between heavy theory and the practical implementation of the loss function.

**Labels:** ["Phase 1", "Math"]
""",
        "labels": ["Phase 1", "Math"]
    },
    {
        "title": "MATH - Noise Schedules & Temporal Consistency in Video Modeling",
        "body": """**Objective:** Analyze noise schedules and formulate the strategy for temporal coherence in video generation.

**Subtasks:**
- Compare **Linear** vs. **Cosine** noise schedules and their impact on training stability and output quality.
- Formulate the challenge of **temporal consistency**: Explain why frame-by-frame generation is problematic.
- Detail the chosen solution for temporal modeling (e.g., 3D U-Net, temporal attention layers).
- Define how time and motion are represented in the latent space.

**Acceptance Criteria:**
- Comparative analysis of noise schedules in documentation.
- Technical specification for temporal layers.
- Explanation of the model's approach to maintaining continuity between frames.

**Labels:** ["Phase 1", "Math", "Architecture"]
""",
        "labels": ["Phase 1", "Math", "Architecture"]
    },
    {
        "title": "ARCHITECTURE - 3D U-Net & Attention Mechanism Deep Dive",
        "body": """**Objective:** Fully document and audit the architecture of the video generation model.

**Subtasks:**
- Map the **3D U-Net structure**: Spatial and temporal downsampling, residual blocks, and skip connections.
- Analyze **Attention Mechanisms**: Spatial self-attention, temporal self-attention, and cross-attention for text conditioning.
- Specify **Position Encodings**: sinusoidal, rotary, or learned encodings for both spatial and temporal dimensions.
- Describe the **Conditioning Mechanisms**: Text encoder (CLIP/T5) integration and conditioning tokens.

**Acceptance Criteria:**
- Architectural diagram of the 3D U-Net.
- Layer-by-layer breakdown of attention blocks.
- Documentation of embedding dimensions and conditioning flow.

**Labels:** ["Phase 1", "Architecture"]
""",
        "labels": ["Phase 1", "Architecture"]
    },
    {
        "title": "MATH - Loss Variants Analysis & CFG Implementation Strategy",
        "body": """**Objective:** Mathematically analyze loss variants and plan the Classifier-Free Guidance (CFG) strategy.

**Subtasks:**
- Compare **Noise prediction ($\\epsilon$)**, **Image prediction ($x_0$)**, and **Velocity prediction ($v$)** losses.
- Justify the choice of loss variant for our implementation.
- Explain **Classifier-Free Guidance (CFG)**: The mechanism for balancing text-video alignment and visual diversity.
- Formulate the sampling equation incorporating CFG with a guidance scale $w$.

**Acceptance Criteria:**
- Mathematical formulation of each loss variant.
- CFG strategy document with recommended guidance scale ranges.
- Justification for the selected loss and guidance method.

**Labels:** ["Phase 1", "Math", "Sampling"]
""",
        "labels": ["Phase 1", "Math", "Sampling"]
    },
    {
        "title": "IMPLEMENTATION - Core Text-to-Video Pipeline Setup",
        "body": """**Objective:** Implement the base text-to-video generation pipeline using a pretrained diffusion model.

**Subtasks:**
- Set up the environment (PyTorch, Diffusers, Transformers).
- Integrate a pretrained model (e.g., Stable Video Diffusion or ModelScope).
- Implement the inference script (`generate_video.py`) for producing clips of $\\geq 4$ seconds.
- Verify basic text-to-video alignment on the finalized theme.

**Acceptance Criteria:**
- Functional `generate_video.py` script.
- Sample video clips generated from theme-specific prompts.
- `requirements.txt` file for environment setup.

**Labels:** ["Phase 2", "Implementation"]
""",
        "labels": ["Phase 2", "Implementation"]
    },
    {
        "title": "ANALYSIS - Formal Weakness Identification & Empirical Measurement",
        "body": """**Objective:** Formally identify and quantify at least two technical weaknesses in the base pipeline.

**Subtasks:**
- Conduct baseline runs on standard and theme-specific prompts.
- Identify at least two weaknesses (e.g., temporal flickering, low semantic alignment, motion blurring).
- Quantify these weaknesses using metrics (FVD, CLIP-SIM, etc.).
- Formulate a hypothesis for the root cause of these weaknesses.

**Acceptance Criteria:**
- A "Weakness Analysis" report in the documentation.
- Quantitative data (tables/graphs) supporting the identified weaknesses.
- Root-cause hypothesis for each weakness.

**Labels:** ["Phase 2", "Analysis"]
""",
        "labels": ["Phase 2", "Analysis"]
    },
    {
        "title": "IMPLEMENTATION - Technical Enhancement A: [Specify Enhancement]",
        "body": """**Objective:** Implement the first technical enhancement to address an identified weakness.

**Subtasks:**
- Formulate the mathematical motivation for the enhancement.
- Implement the changes in the architecture or sampling loop.
- Conduct an ablation study comparing the enhancement against the baseline.
- Verify metric improvements (e.g., improved FVD or CLIP-SIM).

**Acceptance Criteria:**
- Source code for Enhancement A.
- Ablation study results showing quantitative improvement.
- Mathematical justification for why this enhancement works.

**Labels:** ["Phase 2", "Enhancement"]
""",
        "labels": ["Phase 2", "Enhancement"]
    },
    {
        "title": "IMPLEMENTATION - Technical Enhancement B: [Specify Enhancement]",
        "body": """**Objective:** Implement the second technical enhancement to address another identified weakness.

**Subtasks:**
- Formulate the mathematical motivation for the enhancement.
- Implement the changes in the architecture or sampling loop.
- Conduct an ablation study comparing the enhancement against the baseline and Enhancement A.
- Verify metric improvements.

**Acceptance Criteria:**
- Source code for Enhancement B.
- Ablation study results.
- Mathematical justification.

**Labels:** ["Phase 2", "Enhancement"]
""",
        "labels": ["Phase 2", "Enhancement"]
    },
    {
        "title": "EVALUATION - Comprehensive Metric Suite & Benchmarking",
        "body": """**Objective:** Implement and run a comprehensive evaluation suite to measure the project's success.

**Subtasks:**
- Implement **FVD (Fr\\'echet Video Distance)** and **IS (Inception Score)**.
- Implement **CLIP-SIM** for semantic alignment.
- Implement **SSIM/PSNR** and **LPIPS (temporal)** for frame-level quality.
- Implement **Flow Warping Error** for temporal consistency.
- Conduct a **User Study** with $\\geq 10$ raters for subjective realism and coherence.

**Acceptance Criteria:**
- `evaluate.py` script that computes all metrics.
- Final metrics table comparing Baseline vs. Enhancement A vs. Enhancement B vs. Combined.
- User study results and analysis.

**Labels:** ["Phase 2", "Evaluation"]
""",
        "labels": ["Phase 2", "Evaluation"]
    },
    {
        "title": "DOC - Scientific Paper Formulation (IEEE Format)",
        "body": """**Objective:** Write a comprehensive scientific paper documenting the project in IEEE double-column format.

**Subtasks:**
- Abstract (150-250 words).
- Introduction (Motivation, Theme, Contributions).
- Background & Math (DDPM, Loss, Architecture).
- Model Architecture & Loss Analysis.
- Weakness Analysis, Proposed Enhancements, and Implementation Details.
- Results (Metrics, Ablation Study, User Study).
- Discussion, Conclusion, and References.

**Acceptance Criteria:**
- Final scientific paper in PDF format.
- Adherence to all IEEE formatting rules.
- Complete and accurate references.

**Labels:** ["Phase 2", "Documentation"]
""",
        "labels": ["Phase 2", "Documentation"]
    },
    {
        "title": "BONUS - Text-to-Audio Synchronization (TTS/Narration)",
        "body": """**Objective:** Implement an emotional, multi-voice TTS module synchronized with the generated video.

**Subtasks:**
- Integrate a neural TTS model (e.g., Bark, Tortoise-TTS, or Coqui).
- Implement multi-voice support and emotion control (happy, sad, neutral).
- Develop a synchronization layer to align narration with video timing.
- Evaluate the enhancement's impact on storytelling.

**Acceptance Criteria:**
- Functional `audio_gen.py` script.
- Final demo video with emotional narration.
- Technical documentation of the TTS integration.

**Labels:** ["Bonus"]
""",
        "labels": ["Bonus"]
    }
]


def main():
    parser = argparse.ArgumentParser(description="Create SMCG project issues on GitHub")
    parser.add_argument("--token", required=True, help="GitHub personal access token")
    parser.add_argument("--repo", required=True, help="Repository name (e.g., ahmedislamfarouk/SMCG)")
    parser.add_argument("--dry-run", action="store_true", help="Print issues without creating them")
    args = parser.parse_args()

    if args.dry_run:
        print("🔍 DRY RUN MODE - Issues will be printed but NOT created\\n")
        for i, issue in enumerate(ISSUES, 1):
            print(f"\\n{'='*80}")
            print(f"Issue {i}: {issue['title']}")
            print(f"{'='*80}")
            print(f"Labels: {', '.join(issue['labels'])}")
            print(f"\\nBody:\\n{issue['body']}")
            print(f"{'='*80}\\n")
        return

    print(f"🚀 Creating {len(ISSUES)} issues on {args.repo}...\\n")
    
    gh = Github(args.token)
    repo = gh.get_repo(args.repo)

    for i, issue in enumerate(ISSUES, 1):
        print(f"Creating issue {i}/{len(ISSUES)}: {issue['title']}")
        try:
            new_issue = repo.create_issue(
                title=issue['title'],
                body=issue['body']
            )
            print(f"✅ Created: {new_issue.html_url}")
            
            # Add labels if they exist
            if issue['labels']:
                try:
                    # Create labels if they don't exist
                    for label_name in issue['labels']:
                        try:
                            repo.get_label(label_name)
                        except:
                            repo.create_label(name=label_name, color="f29513")
                    
                    new_issue.add_to_labels(*issue['labels'])
                    print(f"   Labels added: {', '.join(issue['labels'])}")
                except Exception as e:
                    print(f"   ⚠️  Could not add labels: {e}")
        except Exception as e:
            print(f"❌ Failed to create issue: {e}")
        print()

    print("✨ Done!")


if __name__ == "__main__":
    main()
