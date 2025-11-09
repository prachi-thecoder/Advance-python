import os, json, zipfile, textwrap

# Project folder
base = "student_chatbot_web"
os.makedirs(base, exist_ok=True)
os.makedirs(os.path.join(base, "templates"), exist_ok=True)
os.makedirs(os.path.join(base, "static"), exist_ok=True)

# ---------- intents.json ----------
intents = {
  "intents": [
    {"tag": "greeting", "patterns": ["Hi", "Hello", "Hey"], "responses": ["Hello! How can I help you?"]},
    {"tag": "goodbye", "patterns": ["Bye", "Goodbye"], "responses": ["Goodbye! Have a great day!"]},
    {"tag": "fee_deadline", "patterns": ["When is the fee deadline?", "Fee due date?"], "responses": ["The fee payment deadline is October 31st."]},
    {"tag": "office_hours", "patterns": ["Registrar office hours", "When is the office open?"], "responses": ["The registrar's office is open Mon–Fri, 9 AM – 5 PM."]}
  ]
}
with open(f"{base}/intents.json", "w") as f: json.dump(intents, f, indent=2)

# ---------- requirements.txt ----------
reqs = "flask\nnltk\ntensorflow\nnumpy\n"
open(f"{base}/requirements.txt", "w").write(reqs)

# ---------- train_chatbot.py ----------
train_code = textwrap.dedent("""
import json, random, numpy as np, nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD

nltk.download('punkt'); nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

with open('intents.json') as f: intents = json.load(f)
words, classes, documents = [], [], []
for intent in intents['intents']:
    for p in intent['patterns']:
        w = nltk.word_tokenize(p); words.extend(w); documents.append((w, intent['tag']))
        if intent['tag'] not in classes: classes.append(intent['tag'])
ignore = ['?', '!', '.', ',']
words = sorted(set([lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore]))
classes = sorted(set(classes))

training, out_empty = [], [0]*len(classes)
for doc in documents:
    bag = [1 if w in [lemmatizer.lemmatize(word.lower()) for word in doc[0]] else 0 for w in words]
    out_row = list(out_empty); out_row[classes.index(doc[1])] = 1
    training.append([bag, out_row])

import random; random.shuffle(training); training = np.array(training, dtype=object)
train_x = np.array(list(training[:,0])); train_y = np.array(list(training[:,1]))

model = Sequential([
    Dense(128, input_shape=(len(train_x[0]),), activation='relu'),
    Dropout(0.5), Dense(64, activation='relu'), Dropout(0.5),
    Dense(len(train_y[0]), activation='softmax')
])
opt = SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
model.fit(train_x, train_y, epochs=100, batch_size=5, verbose=1)
model.save('chatbot_model.h5')
print("Model trained and saved.")
""")
open(f"{base}/train_chatbot.py", "w").write(train_code)

# ---------- app.py ----------
app_code = textwrap.dedent("""
from flask import Flask, render_template, request, jsonify
import random, json, nltk, numpy as np
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

app = Flask(__name__)
lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())
model = load_model('chatbot_model.h5')

words, classes = [], []
for intent in intents['intents']:
    for pattern in intent['patterns']:
        w = nltk.word_tokenize(pattern); words.extend(w)
        if intent['tag'] not in classes: classes.append(intent['tag'])
ignore = ['?', '!', '.', ',']
words = sorted(set([lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore]))
classes = sorted(set(classes))

def clean(sentence):
    sw = nltk.word_tokenize(sentence)
    return [lemmatizer.lemmatize(word.lower()) for word in sw]
def bow(sentence):
    sw = clean(sentence)
    bag = [1 if w in sw else 0 for w in words]
    return np.array(bag)
def predict_intent(sentence):
    p = bow(sentence)
    res = model.predict(np.array([p]))[0]
    threshold = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > threshold]
    results.sort(key=lambda x: x[1], reverse=True)
    return [{'intent': classes[i], 'prob': str(r)} for i, r in results]
def get_response(intents_list):
    if intents_list:
        tag = intents_list[0]['intent']
        for i in intents['intents']:
            if i['tag'] == tag:
                return random.choice(i['responses'])
    return "I'm not sure I understand."

@app.route("/")
def home(): return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    msg = request.form["msg"]
    ints = predict_intent(msg)
    res = get_response(ints)
    return jsonify({"response": res})

if __name__ == "__main__":
    app.run(debug=True)
""")
open(f"{base}/app.py", "w").write(app_code)

# ---------- templates/index.html ----------
html = """<!DOCTYPE html>
<html>
<head>
<title>Student Chatbot</title>
<link rel="stylesheet" href="/static/style.css">
</head>
<body>
<div class="chatbox">
  <h2>🎓 Student Chatbot</h2>
  <div id="chat"></div>
  <form id="form">
    <input type="text" id="msg" autocomplete="off" placeholder="Type your message...">
    <button type="submit">Send</button>
  </form>
</div>
<script>
const form = document.getElementById('form');
const chat = document.getElementById('chat');
form.addEventListener('submit', async (e)=>{
  e.preventDefault();
  const msg = document.getElementById('msg');
  const text = msg.value.trim();
  if(!text) return;
  chat.innerHTML += `<div class='user'>You: ${text}</div>`;
  msg.value='';
  const res = await fetch('/get',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:'msg='+encodeURIComponent(text)});
  const data = await res.json();
  chat.innerHTML += `<div class='bot'>Bot: ${data.response}</div>`;
  chat.scrollTop = chat.scrollHeight;
});
</script>
</body></html>"""
open(f"{base}/templates/index.html", "w").write(html)

# ---------- static/style.css ----------
css = """.chatbox{width:400px;margin:50px auto;border:1px solid #ccc;padding:10px;font-family:sans-serif;}
#chat{height:300px;overflow-y:auto;border:1px solid #ddd;margin-bottom:10px;padding:5px;}
.user{color:blue;margin:5px 0;}
.bot{color:green;margin:5px 0;}
input{width:80%;padding:5px;}button{padding:5px;}"""
open(f"{base}/static/style.css", "w").write(css)

# ---------- zip everything ----------
with zipfile.ZipFile("student_chatbot_web.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, _, files in os.walk(base):
        for f in files:
            path = os.path.join(root, f)
            zipf.write(path, os.path.relpath(path, base))
print("✅ Project created and zipped as student_chatbot_web.zip")
