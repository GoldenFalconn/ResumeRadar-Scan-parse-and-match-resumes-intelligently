import streamlit as st
from text_extractor import extract_text
from parser import extract_email, extract_phone, extract_skills
from match import similarity_score

st.set_page_config(page_title="Resume Parser & Job Matcher", layout="wide")

st.title("📄 Resume Parser & Job Match")

# Upload resume
resume_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])
# Upload Job Description
jd_file = st.file_uploader("Upload Job Description (PDF/DOCX/TXT)", type=["pdf", "docx", "txt"])

if st.button("Parse & Match"):
    if resume_file is None or jd_file is None:
        st.warning("Please upload both Resume and Job Description!")
    else:
        # Extract text


# resume_text = extract_text(resume_file)
# jd_text = extract_text(jd_file)


        resume_text = extract_text(resume_file)
        jd_text = extract_text(jd_file)

        # Parse info
        emails = extract_email(resume_text)
        phones = extract_phone(resume_text)
        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(jd_text)

        # Calculate similarity
        sim_score = similarity_score(resume_text, jd_text)
        skill_overlap = len(set(resume_skills).intersection(set(jd_skills))) / max(len(jd_skills), 1)
        final_score = 0.6 * sim_score + 0.4 * skill_overlap

        # Display results
        st.subheader("Resume Information")
        st.write("**Emails:**", emails)
        st.write("**Phones:**", phones)
        st.write("**Resume Skills:**", resume_skills)
        st.write("**Job Description Skills:**", jd_skills)

        st.subheader("Match Scores")
        st.write("**Text Embedding Similarity:**", round(sim_score, 3))
        st.write("**Skill Overlap Score:**", round(skill_overlap, 3))
        st.write("**Final Match Score:**", round(final_score, 3))
