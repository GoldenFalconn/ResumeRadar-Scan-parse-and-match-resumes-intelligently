ResumeRadar is a Python-based **NLP project** that intelligently parses resumes, extracts candidate information, and matches skills with job descriptions. Powered by **Hugging Face embeddings** and modern NLP techniques, it helps recruiters and HR teams quickly evaluate candidate-job fit.

---

## **Key Functionalities**

- **Resume Parsing:** Extract structured information from resumes including:
  - Emails
  - Phone numbers
  - Skills

- **Job Description Parsing:** Extract required skills from job descriptions (PDF, DOCX, TXT).

- **Skill Matching:** Compare skills in resumes with job description requirements.

- **Semantic Similarity:** Uses **Hugging Face Sentence Transformers** to compute **text embedding similarity** between resume and job description.

- **Final Match Score:** Combines skill overlap and semantic similarity to provide a **weighted final match score**.

- **Multi-format Support:** Works with **PDF, DOCX, and TXT files**.

---


## **Installation**

1. Clone the repository:

```bash
git clone https://github.com/YourUsername/ResumeRadar.git
cd ResumeRadar


2. Create a virtual envvironment
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate


3. Install dependencies
pip install -r requirements.txt


