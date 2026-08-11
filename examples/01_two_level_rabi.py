"""Simulate resonant Rabi oscillations in a closed two-level system."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import qutip as qt


def main() -> None:
    """Solve the Schrodinger equation and save the population dynamics."""
    rabi_frequency = 2 * np.pi
    hamiltonian = 0.5 * rabi_frequency * qt.sigmax()
    initial_state = qt.basis(2, 0)
    times = np.linspace(0.0, 5.0, 501)

    ground_projector = qt.basis(2, 0).proj()
    excited_projector = qt.basis(2, 1).proj()

    result = qt.sesolve(
        hamiltonian,
        initial_state,
        times,
        e_ops=[ground_projector, excited_projector],
    )

    figure, axis = plt.subplots(figsize=(8, 4.5))
    axis.plot(times, result.expect[0], label=r"$P_0$")
    axis.plot(times, result.expect[1], label=r"$P_1$")
    axis.set(
        xlabel="Time",
        ylabel="Population",
        title="Two-level resonant Rabi oscillation",
        ylim=(-0.05, 1.05),
    )
    axis.grid(alpha=0.3)
    axis.legend()
    figure.tight_layout()

    output_path = Path(__file__).resolve().parents[1] / "two_level_rabi.png"
    figure.savefig(output_path, dpi=160)
    print(f"Saved figure to: {output_path}")


if __name__ == "__main__":
    main()
