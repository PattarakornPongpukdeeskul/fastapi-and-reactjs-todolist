from dotenv import load_dotenv
import json
import time
import jwt
import os

load_dotenv()
client_secret = os.getenv("CLIENT_SECRET")
class Middleware:
    def __init__(self,token,method):
        self.token = token
        self.method = method

    def check_verify(self):
        try:
            jwt.decode(self.token, client_secret, algorithms=["HS256"])
            return
        except Exception as e:
            raise ErrorHandler("412", 'invalid token', 401)

    def check_exp(self):
            token = jwt.decode(self.token, client_secret, algorithms=["HS256"])
            exp = int(time.time() * 1000)
            if exp < token['exp']:
              raise ErrorHandler("411", 'token expired', 401)
            return
