import re
from app.regex_patterns import PAN_PATTERN, SSN_PATTERN, CC_PATTERN

def test_pan_detection():
    data = "PAN: ABCDE1234F"
    match = re.search(PAN_PATTERN, data)
    assert match is not None

def test_ssn_detection():
    data = "SSN: 123-45-6789"
    match = re.search(SSN_PATTERN, data)
    assert match is not None

def test_invalid_data():
    data = "No sensitive data here"
    assert re.search(PAN_PATTERN, data) is None