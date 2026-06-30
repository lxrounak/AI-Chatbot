from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
app=Flask(__name__)
client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
history=[{"role":"system","content":"You are a helpful assistant."}]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat",methods=["POST"])
def chat():
    msg=request.json["message"]
    history.append({"role":"user","content":msg})
    r=client.chat.completions.create(model="gpt-4.1-mini",messages=history)
    reply=r.choices[0].message.content
    history.append({"role":"assistant","content":reply})
    return jsonify({"reply":reply})

if __name__=="__main__":
    app.run(debug=True)
