import pygame
import subprocess


def speak(text):
    voice = "id-ID-ArdiNeural"
    output_file = "audio/output.mp3"

    # Use subprocess module for a more flexible and secure command execution
    command = [
        "edge-tts",
        "--voice",
        voice,
        "--text",
        text,
        "--write-media",
        output_file,
    ]

    try:
        # Use subprocess.run instead of os.system for better control
        subprocess.run(command, check=True)

        pygame.init()
        pygame.mixer.init()

        pygame.mixer.music.load(output_file)
        pygame.mixer.music.play()

        # Use pygame.mixer.music.get_busy() directly in the while loop condition
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(e)

    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
