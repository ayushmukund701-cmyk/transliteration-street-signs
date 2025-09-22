from flask import Flask, render_template, request
import os
from ocr_module import extract_text
from translit_module import transliterate_text
from utils import detect_language

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Mapping ISO language code to script
LANG_TO_SCRIPT = {
    "hi": "Devanagari",
    "ta": "Tamil",
    "te": "Telugu",
    "ml": "Malayalam",
    "kn": "Kannada",
    "gu": "Gujarati",
    "pa": "Gurmukhi",
    "bn": "Bengali"
}

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        file = request.files["image"]
        target_script = request.form["target_script"]

        if file:
            path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(path)

            # OCR
            extracted_text = extract_text(path)

            # Detect Language
            lang = detect_language(extracted_text)
            source_script = LANG_TO_SCRIPT.get(lang, "Devanagari")

            # Transliterate
            transliterated = transliterate_text(extracted_text, source_script, target_script)

            result = {
                "original": extracted_text,
                "source_script": source_script,
                "target_script": target_script,
                "output": transliterated
            }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
