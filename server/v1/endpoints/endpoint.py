from fastapi import FastAPI,  APIRouter, Form, HTTPException, Header, Response
from fastapi.responses import FileResponse
import os
from core.models.database import User, Authentication
from helper.encode_jwt import Encode

router = APIRouter()


@router.get("/")
async def main():

    return FileResponse("client/src/assets/svg/icon-account.svg")

@router.post("/login", status_code=200)
async def login(response: Response, email: str = Form(...), password: str = Form(...)):
    user = User(email, password)
    user_documents = user.query()
    
    if len(user_documents)  == 0 :
        raise HTTPException(
            status_code=406, detail="this email does not exist.")

    if user_documents["password"] != password :
        raise HTTPException(
            status_code=406, detail="the password is wrong.")
    encode = Encode(email)

    refresh_token = encode.refresh_token()
    access_token = encode.access_token()

    response.set_cookie(key="token", value="fake-cookie-session-value")
    return user_documents


@router.post("/user", status_code=201)
async def create_user(email: str = Form(...), password: str = Form(...), name: str = Form(...)):
    user = User(email, password)
    user_documents = user.query()

    if len(user_documents) > 0:
        raise HTTPException(
            status_code=406, detail="this email already register")

    user_id = user.create(name)

    return {"id": user_id}


@router.post("/user/login", status_code=201)
async def create_user(email: str = Form(...), password: str = Form(...)):
    user = User(email, password)
    user.create_user()

    return {"message": "test"}
