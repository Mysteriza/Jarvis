from TextToSpeech import speak
from SpeechRecognition import detect_speech
from Weather import get_weather
from YouTubePlayer import play_youtube
from gpt4_free import GPT
from datetime import datetime
import pyautogui

sleep_mode = False

speak("Halo tuan, apa yang bisa saya bantu?")

# Main program loop
while True:
    query = detect_speech().lower()

    if "hentikan" in query or "berhenti" in query:
        speak("Baik Tuan.")
        break
    elif "infokan cuaca" in query:
        weather_info = get_weather()
        speak(weather_info)
    elif "putar" in query:
        video_query = query.replace("putar", "")
        play_youtube(video_query)
        speak("siap!")
        pyautogui.hotkey("space")
    elif "jam berapa sekarang" in query:
        current_time = datetime.now().strftime("%H:%M")
        speak("Sekarang jam " + current_time)
    elif "pindah tab" in query:
        pyautogui.hotkey("ctrl", "tab")
    elif "tutup tab" in query:
        pyautogui.hotkey("ctrl", "w")
        speak("siap")
    elif "tutup aplikasi" in query:
        pyautogui.hotkey("alt", "f4")
        speak("beres tuan")
    elif "sleep" in query:
        speak("sleeping")
        sleep_mode = True
    else:
        jawab = GPT(query)
        speak(jawab)

    while sleep_mode:
        query = detect_speech().lower()
        print(query)
        if "wake up" in query:
            speak("Saya bangun.")
            sleep_mode = False
