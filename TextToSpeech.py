import os
import pygame


def speak(text):
    voice = "id-ID-ArdiNeural"
    output_file = "audio/output.mp3"

    command = (
        f'edge-tts --voice "{voice}" --text "{text}" --write-media "{output_file}"'
    )

    os.system(command)

    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(output_file)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(e)

    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
