import speech_recognition as sr
import pyttsx3
import openai
from commands import handle_command

openai.api_key = "your-openai-api-key"

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return "Error accessing speech service."

def chat_with_gpt(query):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": query}]
    )
    return response['choices'][0]['message']['content']

def main():
    speak("North online. How can I help you?")

    while True:
        query = listen()
        print("You:", query)

        if not query:
            continue

        command_result = handle_command(query)
        if command_result == "shutdown":
            speak("Shutting down. Goodbye.")
            break
        elif command_result:
            speak(command_result)
        else:
            ai_response = chat_with_gpt(query)
            print("North:", ai_response)
            speak(ai_response)

if __name__ == "__main__":
    main()
