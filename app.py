import os
import streamlit as st
from utils import parse_pdf, load_rubric, compute_rubric_score, compute_semantic_scores, load_llm, generate_explanation, build_resume_context
import pandas as pd
from sentence_transformers import SentenceTransformer

st.title("📄 Hiring Assistant")

embedder = SentenceTransformer('all-MiniLM-L6-v2')

jd_files = os.listdir("job_descriptions")
selected_jd = st.selectbox("Select Job Description:", jd_files)

if selected_jd:
    jd_text = parse_pdf(os.path.join("job_descriptions", selected_jd))
    resume_files = os.listdir("resumes")
    resume_texts = [parse_pdf(os.path.join("resumes", r)) for r in resume_files]

    rubric = load_rubric()

    semantic_scores = compute_semantic_scores(jd_text, resume_texts, embedder)
    rubric_scores = [compute_rubric_score(text, rubric) for text in resume_texts]
    final_scores = [(s + r) / 2 for s, r in zip(semantic_scores, rubric_scores)]
    explanations = [generate_explanation(resume_files[i], rubric_scores[i], semantic_scores[i], rubric, jd_text, resume_texts[i]) for i in range(len(resume_files))]

    st.subheader("📊 Candidate Ranking")
    df = pd.DataFrame({
        "Resume": resume_files,
        "Semantic Score": semantic_scores,
        "Rubric Score": rubric_scores,
        "Final Score": final_scores,
        "Explanation": explanations
    })
    st.dataframe(df.sort_values(by="Final Score", ascending=False))

    # Prepare upgraded resume context for chatbot
    resume_context = build_resume_context(resume_texts, resume_files, rubric, embedder)
else:
    resume_context = ""

st.subheader("🤖 Chatbot for Q&A and Rubric Updates")
query = st.text_input("Ask a question or update the rubric (e.g., Update rubric weight for Python to 5):")

llm = load_llm()

if query:
    if "update rubric weight" in query.lower():
        try:
            skill = query.split("for")[1].split("to")[0].strip()
            weight = float(query.split("to")[1].strip())
            rubric[skill] = weight
            with open("rubric/rubric.json", "w") as f:
                import json
                json.dump(rubric, f)
            st.success(f"Rubric updated: {skill} -> {weight}")
        except Exception as e:
            st.error(f"Failed to update rubric: {e}")
    else:
        prompt = f"Here is the candidate data:\n{resume_context}\n\nAnswer the following: {query}"
        response = llm(prompt)
        st.write(response)
