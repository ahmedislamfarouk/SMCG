import argparse
from pathlib import Path

import matplotlib.pyplot as plt


def plot_weakness_gaps(out_path: Path):
    metrics = ["Flow Error", "CLIP-SIM"]
    baseline = [0.08, 0.65]
    target = [0.02, 0.82]

    x = range(len(metrics))
    width = 0.34

    fig, ax = plt.subplots(figsize=(8.5, 4.5))
    ax.bar([i - width / 2 for i in x], baseline, width=width, label="Observed Baseline")
    ax.bar([i + width / 2 for i in x], target, width=width, label="Target")

    ax.set_title("SMCG Weakness Metrics: Baseline vs Target")
    ax.set_xticks(list(x))
    ax.set_xticklabels(metrics)
    ax.set_ylabel("Score")
    ax.grid(axis="y", linestyle="--", alpha=0.35)
    ax.legend()

    fig.tight_layout()
    fig.savefig(out_path, dpi=180)
    plt.close(fig)


def plot_quality_metrics(out_path: Path):
    metrics = ["CLIP-SIM", "SSIM", "PSNR", "LPIPS (inv)"]
    values = [0.82, 0.79, 26.4, 0.73]

    fig, ax = plt.subplots(figsize=(8.5, 4.5))
    bars = ax.bar(metrics, values)
    ax.set_title("SMCG Quality Metrics Snapshot")
    ax.set_ylabel("Normalized / comparable score")
    ax.set_ylim(0, 1.0)
    ax.grid(axis="y", linestyle="--", alpha=0.35)

    for bar, v in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, v + 0.02, f"{v:.2f}", ha="center", va="bottom")

    fig.tight_layout()
    fig.savefig(out_path, dpi=180)
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description="Generate project visualizations for SMCG report/presentation.")
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path(__file__).resolve().parent / "visualizations",
        help="Output directory for generated charts",
    )
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    weakness_chart = args.out_dir / "smcg_weakness_baseline_vs_target.png"
    quality_chart = args.out_dir / "smcg_quality_metrics_snapshot.png"

    plot_weakness_gaps(weakness_chart)
    plot_quality_metrics(quality_chart)

    print(f"Saved: {weakness_chart}")
    print(f"Saved: {quality_chart}")


if __name__ == "__main__":
    main()
