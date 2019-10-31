from base64 import b64encode

usr = "basic_auth_user_name"
pwd = "basic_auth_password"


def _build_unauthorized_response():
    return {
        "status": "401",
        "statusDescription": "Unauthorized",
        "body": "Unauthorized",
        "headers": {
            "www-authenticate": [{"key": "WWW-Authenticate", "value": "Basic"}]
        }
    }


def _generate_auth_headers(usr, pwd):
    usr_pwd_base64 = b64encode(str.encode("{}:{}".format(usr, pwd))).decode("ascii")
    return "Basic {}".format(usr_pwd_base64)


def handler(event, context):
    request = event["Records"][0]["cf"]["request"]
    headers = request["headers"]
    auth_headers = _generate_auth_headers(usr, pwd)
    if "authorization" not in headers or headers["authorization"][0]["value"] != auth_headers:
        return _build_unauthorized_response()
    else:
        return request
