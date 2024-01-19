from openai import OpenAI
import json


def speechtotext():
    f = open('C:/Users/sushm/OneDrive/Documents/GitHub/ChatGPTPythonIntegration/pythonopenAIIntegration/path/path.json')

    # returns JSON object as
    # a dictionary
    data = json.load(f)
    print(data['audiofile'])
    audio_file = open(data['audiofile'], "rb")
    client = OpenAI()
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format="text"
    )
    print(transcript)


def translatekannadatoenglish():
    f = open('C:/Users/sushm/OneDrive/Documents/GitHub/ChatGPTPythonIntegration/pythonopenAIIntegration/path/path.json')
    data = json.load(f)
    print(data['kannadafile'])
    client = OpenAI()
    audio_file = open(data['kannadafile'], "rb")
    translate = client.audio.translations.create(
        model="whisper-1",
        file=audio_file
    )
    print(translate)
