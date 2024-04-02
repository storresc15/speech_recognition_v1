import sys
from speech_recognition import Recognizer, AudioFile

def recognize_speech(file_path):
    recognizer = Recognizer()

    with AudioFile(file_path) as audio_file:
        audio = recognizer.record(audio_file)

    text = recognizer.recognize_google(audio)
    print(text)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python speech_recognition_cli.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    recognize_speech(file_path)
