"""Core health metrics functionality for systemhealthcheck."""

import os
import platform
import time
from typing import Dict, Any

import psutil

# Record process start time to calculate uptime in seconds
_START_TIME = time.time()


def get_health() -> Dict[str, Any]:
    """Return a dictionary with basic system health metrics.

    Returns
    -------
    Dict[str, Any]
        A dictionary with CPU, memory, disk usage, uptime, and basic system info.
    """
    return {
        "cpu_percent": psutil.cpu_percent(interval=0.1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage("/").percent,
        "uptime_seconds": int(time.time() - _START_TIME),
        "system": platform.system(),
        "hostname": platform.node(),
        "pid": os.getpid(),
    }