import os
from flask import Flask, render_template, request
from utils.parser import extract_text_from_pdf
from utils.similarity import calculate_similarity
from utils.scoring import calculate_ats_score

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"

# This ensures uploads folder exists
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["resume"]
        job_description = request.form["job_description"]

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        resume_text = extract_text_from_pdf(filepath)

        match_score = calculate_similarity(resume_text, job_description)
        ats_score = calculate_ats_score(resume_text, job_description)

        return render_template("index.html",
                               match_score=match_score,
                               ats_score=ats_score)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)