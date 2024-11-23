import re

# Define regex patterns for sensitive data
PATTERNS = {
    "PII": [
        (r"[A-Z]{5}[0-9]{4}[A-Z]", "PAN Number"),
        (r"\d{3}-\d{2}-\d{4}", "SSN"),
    ],
    "PCI": [
        (r"\b(?:\d[ -]*?){13,16}\b", "Credit Card Number"),
    ],
    "PHI": [
        (r"\b[A-Z0-9]{10}\b", "Medical Record Number"),
    ],
}

def scan_file(content):
    """Scan file content for sensitive information."""
    results = []
    for data_type, patterns in PATTERNS.items():
        for pattern, label in patterns:
            matches = re.findall(pattern, content)
            if matches:
                results.append({
                    "data_type": data_type,
                    "label": label,
                    "matches": matches,
                })
    return results
