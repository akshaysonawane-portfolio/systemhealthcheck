import argparse
import time
from systemhealthcheck.health import get_health
from systemhealthcheck.utils import pretty_print_metrics

def monitor_health(duration=5, interval=1):
    """
    Print system health every `interval` seconds for `duration` seconds.
    Console-only version.
    """

    start = time.time()
    next_time = start

    while time.time() - start < duration:
        sample = get_health()
        print(pretty_print_metrics(sample))
        print("-" * 40)

        next_time += interval
        sleep_time = next_time - time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)

def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="System health monitoring tool")
    parser.add_argument(
        "--duration",
        type=int,
        default=5,
        help="Duration in seconds to monitor (default: 5)"
    )
    parser.add_argument(
        "--interval",
        type=float,
        default=1,
        help="Interval between samples in seconds (default: 1)"
    )

    args = parser.parse_args()
    monitor_health(duration=args.duration, interval=args.interval)
