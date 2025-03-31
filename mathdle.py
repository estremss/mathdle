from flask import Flask, render_template, url_for
from random import randint
import random
from datasets import load_dataset
from datetime import date
import os
from dotenv import load_dotenv
from mistralai import Mistral

load_dotenv('api_keys.env')
api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-small-latest"

client = Mistral(api_key=api_key)

# ------------- Examples of AI use -------------
chat_response = client.chat.complete(
    model = model,
    messages = [
        {
            "role": "user",
            "content": "What is the best French cheese?",
        },
    ]
)
print(chat_response.choices[0].message.content)
# -----------------------------------------------


# Load dataset and chose a random question
ds = load_dataset("HuggingFaceH4/MATH-500", split='test')
q = random.choice(ds)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/questions")
def questions():
    return render_template('questions.html', date=date.today(), question=q['problem'])

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/skip_question")
def skip_question():
    global q
    q = random.choice(ds)
    return q['problem']

if __name__=="__main__":
    app.run()