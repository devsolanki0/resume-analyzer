import re

def calculate_ats_score(resume_text, job_description):

    resume_words = set(resume_text.split())
    jd_words = set(job_description.split())

    keyword_match = len(resume_words.intersection(jd_words)) / len(jd_words)

    # Simple scoring formula
    ats_score = (
        keyword_match * 0.6 +
        (1 if "experience" in resume_text else 0) * 0.1 +
        (1 if "education" in resume_text else 0) * 0.1 +
        (1 if "skills" in resume_text else 0) * 0.1 +
        (1 if "project" in resume_text else 0) * 0.1
    )

    return round(ats_score * 100, 2)