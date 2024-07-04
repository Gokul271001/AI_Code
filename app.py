from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

url = "http://localhost:11434/api/generate"
headers = {'Content-Type': 'application/json'}
history = []

def generate_response(prompt):
    history.append({"role": "user", "content": prompt})
    final_prompt = "\n".join([f"{h['role']}: {h['content']}" for h in history])

    data = {
        "model": "jarvis",
        "prompt": final_prompt, 
        "stream": False
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            data = response.json()
            actual_response = data['response']
            history.append({"role": "assistant", "content": actual_response})
            return history
        else:
            error_message = f"Error: {response.status_code}, {response.text}"
            history.append({"role": "system", "content": error_message})
            return history
    except Exception as e:
        error_message = f"Error: {str(e)}"
        history.append({"role": "system", "content": error_message})
        return history

def format_history(history):
    formatted = ""
    for entry in history:
        if entry["role"] == "user":
            formatted += f"<div class='user'><strong>User:</strong> {entry['content']}</div>"
        elif entry["role"] == "assistant":
            formatted += f"<div class='assistant'><strong>Assistant:</strong>\n\n<pre><code>{entry['content']}</code></pre></div>"
        else:
            formatted += f"<div class='error'>{entry['content']}</div>"
    return formatted

@app.route("/", methods=["GET", "POST"])
def index():
    global history
    if request.method == "POST":
        prompt = request.form["prompt"]
        history = generate_response(prompt)
    return render_template("index.html", history=format_history(history))

@app.route("/clear", methods=["POST"])
def clear():
    global history
    history = []
    return jsonify({"status": "cleared"})

if __name__ == "__main__":
    app.run(debug=True)
