from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
import aksharamukha.transliterate as aksharamukha

def transliterate_text(text: str, source_script: str, target_script: str) -> str:
    """
    Transliterate given text from source_script to target_script.
    Uses Aksharamukha for Indian scripts.
    """
    try:
        result = aksharamukha.process(source_script, target_script, text)
        return result
    except Exception as e:
        return f"Error: {str(e)}"
