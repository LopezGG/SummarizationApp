
from fastapi import FastAPI
from pydantic import BaseModel

#from model import predictT5

testApp = FastAPI() # create an app

@testApp.get("/") # set root directory

# pydantic models


class TextIn(BaseModel):
    text: str
    minLen: int
    maxLen: int

class TextOut(BaseModel):
    Summary: dict # this should not have () after dict

    # routes
def root():
    return {"message":"Jesus please help me. O Lord I need you"}