# 🧠 Offline AI Resume Screener (LLM + RAG)

This project is an **offline AI-powered resume screener** designed to help recruiters quickly rank candidates against a **Job Description (JD)**. It uses **MiniLM embeddings + FAISS** for semantic search and optionally integrates with a **local LLM (Mistral-7B via Ollama)** to generate recruiter-style explanations and Q&A — all while ensuring **privacy** by running locally.

---

## 🚨 Problem
Recruiters spend hours manually screening resumes:
- ⏱️ Time-consuming (2+ hrs for ~100 resumes).
- ❌ Inconsistent and biased evaluations.
- 🔒 Privacy concerns with cloud-based AI tools.

---

## 💡 Solution
- Built a **local Streamlit app** to automate resume screening.
- **Semantic ranking** with MiniLM embeddings + FAISS.
- **Explainable AI**: recruiter-style Q&A powered by Mistral-7B LLM via RAG.
- **Privacy-first**: no data leaves your machine.

---

## 📊 Results & Impact
- ⚡ **50% faster screening** (2 hrs → ~1 hr per 100 resumes).
- ✅ Transparent, explainable candidate rankings.
- 🔒 Privacy-preserving (offline execution).
- 📈 Scalable for 100s of resumes.

---

## 🛠️ Tech Stack
- **Frontend/App:** Streamlit  
- **ML & AI:** MiniLM embeddings, Mistral-7B, LangChain, FAISS  
- **Languages:** Python  
- **Deployment:** Local (offline), optional Ollama for LLM  

---

## 📂 Project Structure
```
├── app/
│   └── main.py          # Streamlit app
├── src/
│   ├── rag.py           # Resume ranking logic
│   └── utils.py         # File readers, chunking helpers
├── requirements.txt     # Dependencies
└── README.md            # Documentation
```

---

## ⚡ Quick Start
1. **Clone repo & install dependencies**
   ```bash
   git clone https://github.com/yourusername/resume-screener.git
   cd resume-screener
   pip install -r requirements.txt
   ```

2. **(Optional) Install Ollama for local LLM**
   ```bash
   # Download from https://ollama.com/download
   ollama pull mistral
   ```

3. **Run Streamlit app**
   ```bash
   streamlit run app/main.py
   ```

4. **Use the UI**
   - Paste a Job Description (JD).
   - Upload resumes (PDF/DOCX/TXT).
   - Click **Build Index** → **Rank Candidates**.
   - (Optional) Ask recruiter-style Q&A with Ollama.

---

## 🎯 Business Relevance
- Faster and fairer resume shortlisting.
- Cuts recruiter workload and hiring costs.
- Enables **explainable AI** in HR workflows.
- Scales seamlessly while preserving candidate privacy.

---

## 👩‍💻 Author
**Trisha Chandur**  
- [LinkedIn](https://linkedin.com/in/trishachandur)  
- [GitHub](https://github.com/trishachandur)

---
