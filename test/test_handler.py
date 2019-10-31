import unittest

from main import handler


def _build_unauthorized_event():
    return {
        "Records": [
            {
                "cf": {
                    "request": {
                        "headers": {
                            "host": [
                                {
                                    "value": "set-cookie.dev.azdev.direct"
                                }
                            ]
                        }
                    }
                }
            }
        ]
    }


def _build_authorized_event():
    return {
        "Records": [
            {
                "cf": {
                    "request": {
                        "headers": {
                            "host": [
                                {
                                    "value": "set-cookie.dev.azdev.direct"
                                }
                            ],
                            "authorization": [
                                {
                                    "value": "Basic YXpkaXI6NlVwUzJGS1pSNWc3ZTg2blZGYzdpQzJMc1NuQUlNc0VMVVQ5M1NMRkpiT1NUYUdPelQ1TW16bDJLM2thYzdDZg=="
                                }
                            ]
                        }
                    }
                }
            }
        ]
    }


class GenerateAuthHeadersTest(unittest.TestCase):
    def test_handler_unauthorized(self):
        self.assertDictEqual(handler(_build_unauthorized_event(), None), {
            "status": "401",
            "statusDescription": "Unauthorized",
            "body": "Unauthorized",
            "headers": {
                "www-authenticate": [{"key": "WWW-Authenticate", "value": "Basic"}]
            }
        })

    def test_handler_unauthorized(self):
        event = _build_authorized_event()
        request = event["Records"][0]["cf"]["request"]
        self.assertDictEqual(handler(_build_authorized_event(), None), request)
