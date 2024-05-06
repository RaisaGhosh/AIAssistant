# Chat with an intelligent assistant in your terminal
from openai import OpenAI
import json
from gtts import gTTS
import os

language = 'en'

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

history = [
    {"role": "system", "content": "You are a funny and sassy personal assistant. Be concise."},
    {"role": "user", "content": "Hello, I am Raisa and you are my personal assistant."},
]

while True:
    completion = client.chat.completions.create(
        model="TheBloke/dolphin-2.2.1-mistral-7B-GGUF",
        messages=history,
        temperature=0.7,
        stream=True,
    )

    new_message = {"role": "assistant", "content": ""}
    
    print("Thinking...")

    for chunk in completion:
        if chunk.choices[0].delta.content:
            #print(chunk.choices[0].delta.content, end="", flush=True)
            new_message["content"] += chunk.choices[0].delta.content

    # tts = gTTS(text=new_message["content"], lang=language, slow=False, tld='co.uk')
    # tts.save("reply.mp3")
    # print("Answering...")
    # os.system('afplay ' + "reply.mp3")

    history.append(new_message)
    
    # See chat history
    
    gray_color = "\033[90m"
    reset_color = "\033[0m"
    print(f"{gray_color}\n{'-'*20} History dump {'-'*20}\n")
    print(json.dumps(history, indent=2))
    print(f"\n{'-'*55}\n{reset_color}")

    print()
    history.append({"role": "user", "content": input("> ")})

