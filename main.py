from fastapi import FastAPI, Response, status, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from http import HTTPStatus
app = FastAPI()

@app.get('/ping')
def ping():
  return 'pong'

@app.get('/info')
def info(request: Request):
  return {'method': request.method,
          'url': request.url,
          'protocol': HTTPStatus.OK.value}

@app.get('/hello')
def hello():
  return  {"message": "Hello, nfactorial!"}

@app.get('/meaning')
def meaning():
  return {"meaning": "42"}


