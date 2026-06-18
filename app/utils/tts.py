from gtts import gTTS
import tempfile

def text_to_audio(text):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts = gTTS(text=text, lang="en")
    tts.save(temp_file.name)
    return temp_file.name