# 🛣️ Street Sign Transliterator

## 📌 Problem Statement
In India, people speak and write in many languages using different scripts. A traveler from Andhra Pradesh visiting Punjab may not be able to read **Gurmukhi script**, and a pilgrim from Manipur visiting Kerala may not understand **Malayalam script**.  
This project solves the problem by providing a **Transliteration Tool** that converts text from one Indदिल्ली → Dilli → தில்லி → ദില്ലിian script into another **without changing its meaning**.  

For example:  
दिल्ली → Dilli → தில்லி → ദില്ലി

##  🎯 Objective
- Extract text from **street signboards** using OCR.  
- Detect the **script/language** of the text.  
- Convert it into a **user-selected target script**.  
- Provide a simple **web-based interface** for real usage.  

## 🚀 Features
✅ Extract text from street sign images (OCR).  
✅ Detect the source language/script.  
✅ Transliterate text into **any major Indian script**.  
✅ User-friendly **web app (Flask + HTML/CSS)**.  
✅ Supports multilingual OCR (Hindi, Tamil, Telugu, Malayalam, Kannada, Gujarati, Bengali, Gurmukhi).  

## 📂 Project Structure
street-sign-transliterator/
│── app.py # Main Flask app
│── ocr_module.py # OCR text extraction
│── translit_module.py # Transliteration logic
│── utils.py # Language detection
│── requirements.txt # Python dependencies
│── README.md # Documentation
│── static/
│ └── style.css # Web styling
│── templates/
│ └── index.html # Web interface
│── samples/
│ └── street1.jpg # Example street sign image

## ⚙️ Installation Guide

### 1️⃣ Clone Repository
```bash
1. git clone https://github.com/yourusername/street-sign-transliterator.git
   cd street-sign-transliterator

2. pip install -r requirements.txt

3. sudo apt install tesseract-ocr
   sudo apt install libtesseract-dev

4. python app.py

5. http://127.0.0.1:5000/

## 🖼️ Usage
1.Open the web app.
2.Upload a street sign image (e.g., samples/street1.jpg).
3.Select target script (Tamil, Telugu, Malayalam, etc.).
4.Get transliterated text instantly.

## 🔧 How It Works
1.OCR Extraction (pytesseract + OpenCV)
Reads text from street sign images.
2.Language Detection (langdetect)
Identifies the script (Hindi, Tamil, Telugu, etc.).
3.Transliteration (Aksharamukha + indic-transliteration)
Converts text into the chosen target script.
4.Web UI (Flask + HTML/CSS)
Displays extracted text, detected script, and transliterated text.


## ✅ Advantages
1.Supports all major Indian scripts.
2.Helps travelers, tourists, and pilgrims read local signs.
3.Preserves phonetics (word sounds remain intact).
4.Can be extended to mobile apps (Flutter/React Native).
5.Lightweight and easy to deploy.

## ❌ Limitations
1.OCR accuracy depends on image quality (blurry or faded signs may fail).
2.Requires Tesseract OCR language packs.
3.Transliteration may not be perfect for rare words or dialects.
4.Aksharamukha API may need internet for some conversions.

## 🚀 Future Enhancements
1.Add speech output → Text-to-Speech (TTS) in chosen language.
2.Build an offline mobile app for Android/iOS.
3.Improve OCR with deep learning (EasyOCR, Google Vision).
4.Add real-time camera mode (scan signboards live).
5.Multi-script output (show same word in 3–4 scripts simultaneously).

## 👨‍💻 Tech Stack
1.Backend: Python (Flask)
2.OCR: Tesseract OCR + OpenCV
3.Language Detection: langdetect
4.Transliteration: Aksharamukha, indic-transliteration
5.Frontend: HTML, CSS (Bootstrap style)

## 📸 Sample
1.Input Image (Hindi sign):
2.samples/street1.jpg → "दिल्ली 10km"
3.Output (Tamil Script): தில்லி 10km

## 👥 Team
Developed for Smart India Hackathon (SIH)
Organization: AICTE – Indian Knowledge Systems (IKS Division)
Theme: Heritage & Culture

## 📜 License
This project is open-source for educational and hackathon purposes.
✅ With this README:  
- It covers **Problem Statement, Objective, Features, Installation, Working, Advantages, Limitations, Future Enhancements, Sample, Team Info**.  
- It’s **SIH submission-ready**.  

---

Do you want me to also **write the commands for installing Indian language packs in Tesseract (Hindi, Tamil, etc.)** step by step for your README? That way judges can run it without errors.
