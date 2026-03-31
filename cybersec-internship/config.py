LOG_FILE = "tamper_log/logs.json"

FORBIDDEN_KEYWORDS = [
    "import os", "import sys", "subprocess",
    "open(", "__", "eval", "exec", "socket"
]

CPU_LIMIT = 1
MEMORY_LIMIT = 50 * 1024 * 1024
TIMEOUT = 2