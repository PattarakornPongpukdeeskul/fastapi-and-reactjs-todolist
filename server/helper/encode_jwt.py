import jwt
import time
import uuid
import os

class Encode:

    def __init__(self, email):
        self.email = email

    def refresh_token(email):
        return jwt.encode({
            "exp": int(time.time() * 1000)+172800000,
            "iat": int(time.time() * 1000),
            "typ": "Refresh",
            "email": email,
        },
            os.getenv("CLIENT_SECRET"), algorithm="HS256")

    def access_token(email):
        return jwt.encode({
            "exp": int(time.time() * 1000)+600000,
            "iat": int(time.time() * 1000),
            "typ": "Bearer",
            "email": email,
        },
            os.getenv("CLIENT_SECRET"), algorithm="HS256")
