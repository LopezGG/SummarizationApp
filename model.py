
import torch
import json 
from transformers import T5Tokenizer, T5ForConditionalGeneration, T5Config
#from pathlib import Path
#BASE_DIR = Path(__file__).resolve(strict=True).parent

model = T5ForConditionalGeneration.from_pretrained('t5-base')
#tokenizer = T5Tokenizer.from_pretrained('t5-small')
device = torch.device('cpu')

def predictT5(text: str, minLen: int = 5,maxLen: int = 100):
    """
    takes in text  to generate summary
    """
    preprocess_text = text.strip().replace("\n","")
    t5_prepared_Text = "summarize: "+preprocess_text
    tokenized_text = tokenizer.encode(t5_prepared_Text, return_tensors="pt").to(device)
    # summmarize 
    summary_ids = model.generate(tokenized_text,
                                    num_beams=4,
                                    no_repeat_ngram_size=2,
                                    min_length=minLen,
                                    max_length=maxLen,
                                    early_stopping=True)
    output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return output


