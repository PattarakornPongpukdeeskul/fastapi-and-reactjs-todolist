from fastapi import FastAPI, Depends, Header, HTTPException, Response
from .endpoints import endpoint

app = FastAPI(title="Auth FastAPI",
              description="Login and Register | Author : Pattarakorn Pongpukdeeskul",
              version="0.0.1")


@app.get("/api/v1/info")
async def information():
    return {"app_name": app.title, "description": app.description, "version": app.version, "documents_path": "/docs"}


app.include_router(
    endpoint.router,
    prefix="/api/v1",
    responses={404: {"message": "Not found"}},
)
