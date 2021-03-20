from fastapi import FastAPI, Request
from pydantic import BaseModel

#from model import predictT5
import torch
import json 
from transformers import T5Tokenizer, T5ForConditionalGeneration, T5Config

model = T5ForConditionalGeneration.from_pretrained('t5-base')
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Jesus Mary Joseph, I love you save all souls"}

@app.get("/get")
async def get_name(name:str):
    return {"name": name}