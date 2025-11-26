"""Utility helpers for systemhealthcheck.

Currently small, but exists to demonstrate an extensible package layout.
"""

from typing import Mapping


def pretty_print_metrics(metrics: Mapping) -> str:
    """Return a nicely formatted string for health metrics.

    Parameters
    ----------
    metrics : Mapping
        A mapping (e.g., dict) containing health metrics.

    Returns
    -------
    str
        A multi-line string with aligned keys and values.
    """
    lines = []
    for key, value in metrics.items():
        lines.append(f"{key:16}: {value}")
    return "\n".join(lines)