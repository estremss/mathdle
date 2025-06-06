from flask import Flask, render_template, url_for, redirect, request
import random
from datasets import load_dataset
from datetime import date
import os
from mistralai import Mistral
from dotenv import load_dotenv

load_dotenv()


api_key = os.environ["MISTRAL_API_KEY"]

client = Mistral(api_key=api_key)


# Load dataset and chose a random question
ds = load_dataset("HuggingFaceH4/MATH-500", split='test')
q = random.choice(ds)
while q['problem'].find('asy') != -1:
    q = random.choice(ds)

app = Flask(__name__)

# --------- Functions ---------

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/questions", methods=['POST', 'GET'])
def questions():    
    return render_template('questions.html', date=date.today(), question=q['problem'])

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form.get('msg')
    input = msg
    return get_chat_response(input)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/skip_question")
def skip_question():
    global q
    q = random.choice(ds)
    while q['problem'].find('asy') != -1:
        q = random.choice(ds)
    return q['problem']

def get_chat_response(txt):
    global q
    prompt = "1. " + q["problem"] + "\n\n" + "2. " + q["solution"] + "\n\n" + "3. " + q['answer'] + '\n\n' + "4. USER RESPONSE: " + txt
    chat_response = client.agents.complete(
        agent_id = os.environ['MODEL'],
        messages = [
            {
                "role": "user",
                "content": prompt,
            },
        ]
    )
    return chat_response.choices[0].message.content

if __name__=="__main__":
    app.run()