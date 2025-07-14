# main.py
from fastapi import FastAPI
import ipinfo
import os

app = FastAPI()

@app.get("/{ip_address}")
def read_root(ip_address: str):
    access_token = os.environ.get("access_token")
    handler = ipinfo.getHandler(access_token)
 
    details = handler.getDetails(ip_address)
    return {"mensagem": details.details}
