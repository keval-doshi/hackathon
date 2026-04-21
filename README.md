# 🤖 IT Specialized AI Chatbot

RAG-based IT support chatbot using Flask + LangChain + Gemini + FAISS.

---

## ⚙️ Setup (Run Once)

### 1. Install dependencies
```
pip install -r requirements.txt
```

### 2. Add your Google API Key
Open `.env` and replace with your key:
```
GOOGLE_API_KEY=your_actual_key_here
```

### 3. Build the FAISS index
```
python -m backend.ingest_docs
```

---

## 🚀 Run the App
```
python app.py
```
Then open → http://127.0.0.1:8000

---

## 📁 Project Structure
```
IT-chatbot/
├── app.py                  ← Flask server (run this)
├── .env                    ← Your Google API key
├── requirements.txt
├── backend/
│   ├── config.py           ← Paths & settings
│   ├── ingest_docs.py      ← Build FAISS index
│   ├── query_engine.py     ← RAG search logic
│   └── llm_fallback.py     ← Gemini fallback
├── data/
│   ├── microsoft_365.md    ← Knowledge base docs
│   └── outlook.md
├── embeddings/
│   └── faiss_index/        ← Auto-generated index
└── templates/
    └── index.html          ← Chat UI
```

## 🧠 How it works
1. User asks a question
2. FAISS searches knowledge base docs
3. If confident match → returns doc answer (🗂️ Knowledge Base)
4. If low confidence → Gemini generates answer (🤖 AI)
