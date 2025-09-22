import cv2
import pytesseract

def extract_text(image_path: str) -> str:
    """
    Extract text from a street sign image using Tesseract OCR.
    Supports multiple Indian languages.
    """
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # OCR with multiple Indian language packs
    text = pytesseract.image_to_string(gray, lang='hin+eng+tam+tel+ben+mal+kan+guj+pan')
    return text.strip()
