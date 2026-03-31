import hashlib

def verify_logs(logs):
    issues = []

    for i in range(1, len(logs)):
        current = logs[i]
        prev = logs[i - 1]

        recalculated_hash = hashlib.sha256(
            f"{current['index']}{current['timestamp']}{current['event']}{current['description']}{current['prev_hash']}".encode()
        ).hexdigest()

        if current["prev_hash"] != prev["current_hash"]:
            issues.append(f"❌ Chain broken at index {i}")

        if current["current_hash"] != recalculated_hash:
            issues.append(f"❌ Data tampered at index {i}")

        if current["index"] != i:
            issues.append(f"❌ Log reordering detected at index {i}")

    if issues:
        return issues
    return ["✅ All logs are secure"]