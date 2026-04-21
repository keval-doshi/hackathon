from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from backend.query_engine import query_knowledge_base

app = Flask(__name__)
CORS(app)

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/chat")
def chat():
    data = request.get_json()
    query = data.get("query", "")
    return jsonify(query_knowledge_base(query))

if __name__ == "__main__":
    app.run(debug=True, port=8000)
