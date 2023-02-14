"""
Example for run HTTPWebServer
"""
from HTTPWebServer.HTTPWebServer import HTTPWebServer

app = HTTPWebServer()


@app.get('/')
async def home():
    pass

# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}