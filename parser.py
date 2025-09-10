# parser.py
import re
import spacy
nlp = spacy.load("en_core_web_sm")

EMAIL_RE = re.compile(r"[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+")
PHONE_RE = re.compile(r"(\+?\d{1,3}[-.\s]?)?(\d{10}|\d{5}[-.\s]\d{5}|\d{3}[-.\s]\d{3}[-.\s]\d{4})")

def extract_contacts(text):
    emails = list(set(EMAIL_RE.findall(text)))
    phones = list(set(m[0] if isinstance(m, tuple) else m for m in PHONE_RE.findall(text)))
    # PHONE_RE.findAll returns tuples; convert as needed — simplifed here
    # Better: re.findall(r'\+?\d[\d\s\-]{7,}\d', text)
    return emails, phones

def extract_entities(text):
    doc = nlp(text)
    names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
    orgs  = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
    dates = [ent.text for ent in doc.ents if ent.label_ in ("DATE", "TIME")]
    return {"names": names, "orgs": orgs, "dates": dates}

def clean_text(text):
    txt = text.replace("\n", " ").strip()
    txt = re.sub(r"\s+", " ", txt)
    return txt


from rapidfuzz import process, fuzz

def load_skills(path="skills.txt"):
    with open(path, "r", encoding="utf-8") as f:
        skills = [line.strip().lower() for line in f if line.strip()]
    return skills

def extract_skills(text, skills_list, threshold=80):
    text_lower = text.lower()
    found = set()
    # direct substring match
    for s in skills_list:
        if s in text_lower:
            found.add(s)
    # fuzzy match for multi-word or slightly different forms
    tokens = text_lower.split()
    # optionally check top fuzzy matches from entire text
    for s in skills_list:
        score = fuzz.partial_ratio(s, text_lower)
        if score >= threshold:
            found.add(s)
    return sorted(found)