from langdetect import detect

def detect_language(text: str) -> str:
    """
    Detect the language of extracted text.
    Returns ISO code like 'hi', 'ta', 'te'.
    """
    try:
        return detect(text)
    except:
        return "unknown"
