from transformers import pipeline
import joblib
from flask import Flask,make_response,jsonify,request
from transformers import AutoTokenizer
import os
from dotenv import load_dotenv
load_dotenv()


generator=joblib.load(os.getenv("finetuned_model_link"))
pipe = pipeline("text-classification", model="s-nlp/roberta_toxicity_classifier")
tokenizer = AutoTokenizer.from_pretrained("facebook/bart-base")

def usernamecontroller(body):
    try:
        loop_count=2
        name=body
        model=generator 
        max_length=50
        for i in range(loop_count):
            generated_usernames=[]
            input_ids = tokenizer(name, padding="max_length", truncation=True, return_tensors="pt", max_length=max_length)
            output = model.generate(**input_ids, max_length=max_length, num_return_sequences=1, do_sample=True, top_k=50, top_p=0.95)
            generated_username = tokenizer.decode(output[0], skip_special_tokens=True)
            cleaned_username = generated_username.replace(',', '').strip()
            split_usernames = cleaned_username.split()
            generated_usernames.extend(split_usernames)
        return make_response(jsonify( generated_usernames),200)
    except Exception as e:
        return make_response(jsonify({"error":str(e)}),400)
    
def toxiccontroller(body):
    try:
        input_data=body
        response=pipe(input_data)
        return make_response(jsonify(response),200)
    except Exception as e:
        return make_response(jsonify({"error":str(e)}),400)