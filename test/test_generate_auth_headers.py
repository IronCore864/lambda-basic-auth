import unittest

from main import _generate_auth_headers, usr, pwd


class GenerateAuthHeadersTest(unittest.TestCase):
    def test_generate_auth_headers(self):
        self.assertEqual(_generate_auth_headers(usr, pwd),
                         "Basic YXpkaXI6NlVwUzJGS1pSNWc3ZTg2blZGYzdpQzJMc1NuQUlNc0VMVVQ5M1NMRkpiT1NUYUdPelQ1TW16bDJLM2thYzdDZg==")
