import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"Tesseract-OCR\tesseract.exe"

def extract_text(image: Image.Image):
    text = pytesseract.image_to_string(image)
    return text.strip()