import argparse
import time
import time
import psutil
import platform


def monitor_health(duration=5, interval=1):
    """
    Print system health in a tabular format for duration seconds.
    Now includes cleanly formatted per-core CPU usage.
    """

    # Print header once
    print(f"{'HOST':<15}{'CPU (%)':<10}{'MEM (%)':<10}{'GPU (%)':<10}{'DISK (%)':<10}{'RAM (GB)':<10}")
    print("-" * 65)

    start = time.time()
    next_time = start

    while time.time() - start < duration:

        # CPU, memory, disk info
        cpu = psutil.cpu_percent(interval=0.1)
        per_core = psutil.cpu_percent(interval=0.1, percpu=True)
        mem = psutil.virtual_memory().percent
        disk = psutil.disk_usage("/").percent

        # Total RAM in GB
        ram_gb = psutil.virtual_memory().total / (1024**3)

        # GPU info (if available, otherwise 0)
        try:
            import GPUtil
            gpus = GPUtil.getGPUs()
            gpu = gpus[0].load * 100 if gpus else 0
        except:
            gpu = 0  # No GPU found

        host = platform.node()

        # Print main table row
        print(f"{host:<15}{cpu:<10.1f}{mem:<10.1f}{gpu:<10.1f}{disk:<10.1f}{ram_gb:<10.2f}")
        print("\nCPU Per Core:")

        # Pretty vertical formatting
        for i, v in enumerate(per_core):
            print(f"  Core {i:<2}: {v:>5.1f}%")

        print("-" * 65)

        # Maintain interval timing
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
