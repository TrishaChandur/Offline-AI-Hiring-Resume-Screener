📌 Case Study: Offline AI Hiring Resume Screener
🚨 Problem

Recruiters often spend hours manually screening resumes:

Time-consuming (2+ hrs for ~100 resumes).

Inconsistent evaluations.

Lack of explainable shortlisting.

Concerns about data privacy when using cloud-based tools.

💡 Solution

I built an Offline AI Resume Screener:

A local Streamlit app that works entirely offline.

Uses MiniLM embeddings for semantic search.

Powered by Mistral-7B LLM with RAG (Retrieval-Augmented Generation) for contextual answers.

Provides recruiter-style Q&A (e.g., “Does this candidate have SQL experience?”).

Ensures transparent, explainable ranking of resumes.

🛠️ Tech Stack

Frontend/App: Streamlit

ML & AI: MiniLM embeddings, Mistral-7B, LangChain, FAISS

Deployment: Local (privacy-first), GCP Vertex AI (for experiments)

Languages: Python

📊 Results & Impact

⏱️ Reduced manual screening effort by ~50% (2 hrs → ~1 hr per 100 resumes).

🔍 Explainable AI → Every ranking included a rationale, avoiding “black-box” outputs.

🔒 Privacy-first → Runs offline, ensuring candidate data security.

⚡ Scalable → Can handle 100s of resumes consistently and quickly.

🎯 Business Relevance

This project demonstrates how Applied AI + RAG pipelines can transform HR workflows:

Faster, fairer candidate shortlisting.

Reduced recruiter workload → lower hiring costs.

Compliance-friendly (local execution, no external API calls).
