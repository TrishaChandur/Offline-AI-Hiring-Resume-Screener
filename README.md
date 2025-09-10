# 🤖 Offline AI Hiring Resume Screener

A private, local-first AI assistant for resume screening, capable of performing recruiter-style Q&A and intelligent resume ranking without internet access.

---

## 🧠 Overview

This project aims to streamline the recruitment process by reducing manual effort through automation and intelligent AI-driven screening. The app evaluates candidate resumes against job descriptions and predefined rubrics, enabling explainable, transparent, and private hiring decisions.

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit (local app interface)
- **NLP & AI**:
  - `MiniLM` for generating semantic embeddings
  - `Mistral-7B` integrated using **RAG** (Retrieval-Augmented Generation)
- **Frameworks**: LangChain, FAISS
- **Cloud/Local Compute**: Vertex AI (for remote model execution)

---

## 🔍 Features

- 📄 Resume parsing and semantic embedding
- 🔗 Job description comparison using vector search
- ✅ Scoring via rubric-based criteria
- 💬 Recruiter-style Q&A powered by RAG
- 🛡️ Fully offline mode for secure data handling

---

## 📈 Impact

- ⏱️ Reduced manual resume screening time by 50%
- 🔐 Ensures privacy and control in hiring decisions
- 🤝 Promotes transparency and explainability for recruiters

---

## 📁 Project Structure

```bash
resume_screener/
├── app.py                   # Streamlit interface
├── embeddings.py            # MiniLM + FAISS logic
├── rag_chain.py             # RAG + Mistral-7B setup
├── rubric.yaml              # Rules for scoring resumes
├── data/
│   ├── resumes/             # Candidate resumes (PDFs)
│   ├── job_descriptions/    # Target job roles
│   └── outputs/             # Shortlist results
└── README.md
