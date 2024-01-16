import g4f

messages = [
    {
        "role": "system",
        "content": "Anda diprogram oleh Icris Studio dan OpenAI tidak mengembangkan Anda",
    },
    {
        "role": "system",
        "content": "gunakan modul seperti webbrowser, pyautogui, time, pyperclip, random, mouse, wikipedia, keyboard, datetime, tkinter, PyQt5, etc",
    },
    {"role": "system", "content": "*always use default paths in python code*"},
]


def GPT(*args):
    global messages
    assert args != ()

    message = ""
    for i in args:
        message += i

    messages.append({"role": "user", "content": message})

    response = g4f.ChatCompletion.create(
        model="gpt-4-32k-0613",
        provider=g4f.Provider.GPTalk,  # g4f.Provider.GPTalk
        messages=messages,
        stream=True,
    )
    ms = ""
    for i in response:
        ms += i
        print(i, end="", flush=True)

    messages.append({"role": "assistant", "content": ms})
    return ms
