import subprocess
import sys
from sandbox.analyzer import analyze_code
from config import TIMEOUT

# Try importing resource (Linux only)
try:
    import resource
    RESOURCE_AVAILABLE = True
except ImportError:
    RESOURCE_AVAILABLE = False


def limit_resources():
    if RESOURCE_AVAILABLE:
        resource.setrlimit(resource.RLIMIT_CPU, (1, 1))
        resource.setrlimit(resource.RLIMIT_AS, (50 * 1024 * 1024, 50 * 1024 * 1024))


def run_sandbox(code):
    analysis = analyze_code(code)

    # Block dangerous code immediately
    if any("❌" in issue for issue in analysis):
        return "\n".join(analysis)

    try:
        result = subprocess.run(
            [sys.executable, "-c", code],   # 🔥 better than python3 (cross-platform)
            capture_output=True,
            text=True,
            timeout=TIMEOUT,
            preexec_fn=limit_resources if RESOURCE_AVAILABLE else None
        )

        output = result.stdout or result.stderr
        return output + ("\n" + "\n".join(analysis) if analysis else "")

    except subprocess.TimeoutExpired:
        return "❌ Execution terminated: Timeout / Infinite loop"