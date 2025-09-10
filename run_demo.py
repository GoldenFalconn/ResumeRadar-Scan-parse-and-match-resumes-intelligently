# run_demo.py

# NEW

from text_extractor import extract_text
from parser import clean_text, extract_contacts, extract_entities, load_skills, extract_skills
from match import final_match_score

def run(resume_path, jd_path):
    resume_raw = extract_text(resume_path)
    jd_raw = extract_text(jd_path)
    resume = clean_text(resume_raw)
    jd = clean_text(jd_raw)

    emails, phones = extract_contacts(resume)
    entities = extract_entities(resume)
    skills_list = load_skills("skills.txt")
    resume_skills = extract_skills(resume, skills_list)
    jd_skills = extract_skills(jd, skills_list)

    scores = final_match_score(resume, jd, resume_skills, jd_skills)

    print("Emails:", emails)
    print("Phones:", phones)
    print("Top Entities:", entities)
    print("Resume Skills:", resume_skills)
    print("JD Skills:", jd_skills)
    print("Scores:", scores)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python run_demo.py resume.pdf jobdesc.pdf")
    else:
        run(sys.argv[1], sys.argv[2])
