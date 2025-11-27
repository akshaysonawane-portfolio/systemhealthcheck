# systemhealthcheck

[![PyPI version](https://img.shields.io/pypi/v/systemhealthcheck.svg)](https://pypi.org/project/systemhealthcheck/)
[![Python versions](https://img.shields.io/pypi/pyversions/systemhealthcheck.svg)](https://pypi.org/project/systemhealthcheck/)
[![License](https://img.shields.io/pypi/l/systemhealthcheck.svg)](LICENSE)

`systemhealthcheck` is a lightweight, production-style Python package that exposes real-time system health metrics.  
It includes both:

- A **fast API-safe `get_health()` function**, and  
- A **console-based monitoring CLI tool** that prints metrics at fixed intervals.

This project is ideal for learning, DevOps demonstrations, monitoring scripts, and showcasing your Python packaging skills.

---

## 📦 Installation (from PyPI)

```bash
pip install systemhealthcheck
```

---

## 🖥️ CLI Usage (Console Monitoring)

After installation, `systemhealthcheck` provides a command-line tool that prints system metrics in a tabular format.

### ▶ Monitor for 5 seconds (default)
```bash
systemhealthcheck
```

### ▶ Monitor for custom time and interval 

```bash
systemhealthcheck --duration 10 --interval 2
```

