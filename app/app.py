import gradio as gr
from PIL import Image
import re

from utils.classify_flip import predict_flip
from utils.ocr import extract_text
from utils.tts import text_to_audio

def clean_text_for_tts(text):

    # Remove OCR symbols
    text = re.sub(r"[*|_=~#<>\\/\[\]{}]", " ", text)

    # Remove isolated single characters
    text = re.sub(r"\b[a-zA-Z]\b", "", text)

    # Remove repeated punctuation
    text = re.sub(r"[.,!?]{2,}", ".", text)

    # Remove multiple spaces/newlines
    text = re.sub(r"\s+", " ", text)

    return text.strip()

def process_page(image: Image.Image):
    flip_label, confidence = predict_flip(image)

    if flip_label == "flipping":
        return (
            f"Page appears to be flipping. Confidence: {confidence:.2f}",
            "",
            None
        )

    text = extract_text(image)
    clean_text = clean_text_for_tts(text)
    
    if not text.strip():
        return (
            f"Page is not flipping. Confidence: {confidence:.2f}",
            "No readable text found.",
            None
        )

    audio_path = text_to_audio(clean_text)

    return (
        f"Page is not flipping. Confidence: {confidence:.2f}",
        text,
        audio_path
    )


demo = gr.Interface(
    fn=process_page,
    inputs=gr.Image(type="pil", label="Upload page image"),
    outputs=[
        gr.Textbox(label="Flip Detection Result"),
        gr.Textbox(label="Extracted Text", lines=12),
        gr.Audio(label="Generated Audio File", type="filepath")
    ],
    title="CV Reader",
    description="Upload a page image. The app checks if the page is flipping, extracts readable text, and converts it to audio."
)

if __name__ == "__main__":
    demo.launch()