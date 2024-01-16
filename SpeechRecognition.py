import speech_recognition as sr

def detect_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
        
    try:
        query = recognizer.recognize_google(audio, language="id-ID")
        return query.lower()
    except Exception as e:
        #print(e)
        return "sleep"
    

