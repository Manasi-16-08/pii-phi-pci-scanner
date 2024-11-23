import unittest
from scanner import scan_file

class TestScanner(unittest.TestCase):
    def test_scan_file(self):
        content = "My PAN is ABCDE1234F and my SSN is 123-45-6789."
        results = scan_file(content)
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]['data_type'], "PII")
        self.assertEqual(results[1]['data_type'], "PII")

if __name__ == '__main__':
    unittest.main()
