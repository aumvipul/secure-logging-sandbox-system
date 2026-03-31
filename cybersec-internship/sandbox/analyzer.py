from config import FORBIDDEN_KEYWORDS

def analyze_code(code):
    issues = []

    for keyword in FORBIDDEN_KEYWORDS:
        if keyword in code:
            issues.append(f"❌ Forbidden keyword detected: {keyword}")

    if "while True" in code:
        issues.append("⚠️ Potential infinite loop detected")

    if len(code) > 500:
        issues.append("⚠️ Code too long (possible abuse)")

    return issues