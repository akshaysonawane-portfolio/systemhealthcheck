"""Top-level package for systemhealthcheck.

This package exposes a simple `get_health` function that returns a dictionary
of basic system metrics.
"""

from .health import get_health

__all__ = ["get_health"]