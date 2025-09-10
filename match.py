# match.py
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")  # small & fast

def embed_text(text):
    # chunking long text is useful: but for short resumes/jds it's fine
    return model.encode([text], convert_to_numpy=True)[0]

def similarity_score(resume_text, jd_text):
    emb_r = embed_text(resume_text)
    emb_j = embed_text(jd_text)
    sim = cosine_similarity([emb_r], [emb_j])[0][0]  # between 0 and 1
    return float(sim)



def skill_overlap_score(resume_skills, jd_skills):
    if not jd_skills:
        return 0.0
    overlap = set(resume_skills).intersection(set(jd_skills))
    return len(overlap) / len(set(jd_skills))

def final_match_score(resume_text, jd_text, resume_skills, jd_skills, w_embed=0.6, w_skill=0.4):
    embed_sim = similarity_score(resume_text, jd_text)  # 0..1
    skill_score = skill_overlap_score(resume_skills, jd_skills)  # 0..1
    final = w_embed * embed_sim + w_skill * skill_score
    return {"embed_sim": embed_sim, "skill_score": skill_score, "final_score": final}