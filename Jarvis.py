# main_program.py
from wit import Wit
from TextToSpeech import speak
from SpeechRecognition import detect_speech
from Weather import get_weather
from YouTubePlayer import play_youtube
from gpt4_free import GPT
from datetime import datetime
import pyautogui

WIT_AI_API_KEY = "7Q6HE2CSHLIGIEFT56YPOKMX6JL4Y7T7"
client = Wit(WIT_AI_API_KEY)


def get_intent(query):
    try:
        response = client.message(query)
        intents = response.get("intents", [])
        intent = intents[0]["name"] if intents else None
        return intent
    except Exception as e:
        print(f"Error communicating with Wit.ai: {e}")
        return None


def main():
    sleep_mode = False

    speak("Halo tuan!")

    while True:
        query = detect_speech().lower()
        intent = get_intent(query)

        if intent == "berhenti":
            speak("Baik Tuan.")
            break
        elif intent == "infokan_cuaca":
            weather_info = get_weather()
            speak(weather_info)
        elif "putar" in query:
            video_query = query.replace("putar", "")
            play_youtube(video_query)
            speak("siap!")
            # pyautogui.hotkey("space")
        elif intent == "jam_sekarang":
            hours_time = datetime.now().strftime("%H")
            minutes_time = datetime.now().strftime("%M")
            speak(f"Sekarang jam {hours_time} lewat {minutes_time} menit")
        elif "pindah tab" in query:
            pyautogui.hotkey("ctrl", "tab")
        elif "tutup tab" in query:
            pyautogui.hotkey("ctrl", "w")
            speak("siap")
        elif "jeda" in query:
            pyautogui.hotkey("space")
        elif "lanjut" in query:
            pyautogui.hotkey("space")
        elif "tutup aplikasi" in query:
            pyautogui.hotkey("alt", "f4")
        elif intent == "sleep":
            speak("sleep")
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


if __name__ == "__main__":
    main()
