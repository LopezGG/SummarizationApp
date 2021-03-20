
from fastapi import FastAPI
from pydantic import BaseModel

from model import predictT5

app = FastAPI() # create an app

@app.get("/") # set root directory

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

'''@app.post("/predict", response_model=TextOut, status_code=200)
def get_prediction(payload: TextIn):
    """
    Gets a text and runs through T5, GPT2 and outputs summary
    """

    text = payload.text
    minLen = payload.minLen
    maxLen = payload.maxLen
    t5Summary = predictT5(text,minLen,maxLen)
    if not t5Summary:
        raise HTTPException(status_code=400, detail="Unable to run T5")
    summary = dict()
    summary['t5'] = t5Summary
    response_object = {"Summary": summary}
    return response_object'''

"""
activate learning
uvicorn main:app --reload

"""