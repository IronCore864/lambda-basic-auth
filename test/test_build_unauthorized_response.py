import unittest

from main import _build_unauthorized_response


class BuildUnauthorizedResponseTest(unittest.TestCase):
    def test_build_unauthorized_response(self):
        self.assertDictEqual(_build_unauthorized_response(), {
            "status": "401",
            "statusDescription": "Unauthorized",
            "body": "Unauthorized",
            "headers": {
                "www-authenticate": [{"key": "WWW-Authenticate", "value": "Basic"}]
            }
        })
