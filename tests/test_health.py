from systemhealthcheck.health import get_health


def test_health_contains_expected_keys():
    data = get_health()
    for key in [
        "cpu_percent",
        "memory_percent",
        "disk_percent",
        "uptime_seconds",
        "system",
        "hostname",
        "pid",
    ]:
        assert key in data