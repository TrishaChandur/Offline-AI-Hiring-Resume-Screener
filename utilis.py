import os
import fitz
import json
import torch
import numpy as np
from sentence_transformers import util
from ctransformers import AutoModelForCausalLM

def parse_pdf(file_path):
    text = ""
    doc = fitz.open(file_path)
    for page in doc:
        text += page.get_text()
    return text

def load_rubric():
    rubric_path = "rubric/rubric.json"
    if os.path.exists(rubric_path):
        with open(rubric_path, "r") as f:
            rubric = json.load(f)
    else:
        rubric = {}
    return rubric

def compute_rubric_score(text, rubric):
    score = 0
    for skill, weight in rubric.items():
        if skill.lower() in text.lower():
            score += float(weight)
    return score

def compute_semantic_scores(jd_text, resumes, embedder):
    jd_embedding = embedder.encode(jd_text, convert_to_tensor=True)
    scores = []
    for text in resumes:
        resume_embedding = embedder.encode(text, convert_to_tensor=True)
        similarity = util.cos_sim(jd_embedding, resume_embedding).item()
        scores.append(similarity)
    return scores

def load_llm():
    model_path = "models/mistral-7b-instruct-v0.2.Q5_0.gguf"
    llm = AutoModelForCausalLM.from_pretrained(
        model_path,
        model_type="mistral",
        gpu_layers=0,
    )
    return llm

def generate_explanation(name, r_score, s_score, rubric, jd_text, resume_text):
    matched_skills = [skill for skill in rubric.keys() if skill.lower() in resume_text.lower()]
    explanation = f"Candidate {name} matched the following skills: {', '.join(matched_skills) if matched_skills else 'None'}. "
    explanation += f"Semantic similarity to JD: {s_score:.2f}. Rubric score: {r_score}."
    return explanation

def build_resume_context(resume_texts, resume_names, rubric, embedder):
    summaries = []
    for idx, text in enumerate(resume_texts):
        matched_skills = [skill for skill in rubric.keys() if skill.lower() in text.lower()]
        jd_embedding = embedder.encode(text, convert_to_tensor=True)
        summary = f"Candidate: {resume_names[idx]}\nSkills: {', '.join(matched_skills) if matched_skills else 'None'}\n"
        summaries.append(summary)
    return "\n\n".join(summaries)
