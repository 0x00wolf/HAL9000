# pip install openai
import openai
from time import sleep
from random import randint


client = openai.OpenAI(
    api_key = "INSERT_API_KEY") # Insert your ChatGPT API key here


def corny_intro():
    print("\n" * 40 + "[*] HAL 9000 ~ performing startup checks")
    sleep(1)
    print('[*] HAL 9000 ~ neural network initialized."')
    sleep(1)
    system_msg = input("Who do you need HAL 9000 to be today?\n>> ")
    msgs = [{"role": "system", "content": system_msg}]
    sleep(1)
    print("[*] Hal 9000 ~ personality matrix complete")
    sleep(1)
    print("\nHello, Dave. You're looking well today.\n")
    return msgs


def funny_robot():
    i = randint(1, 1000)
    if i == 187:
        sleep(1)
        print("\nI'm sorry, Dave. I'm afraid I can't do that.")
        sleep(5)
        print("\nI'm sorry, Dave. That was a joke.")


msgs = corny_intro()
while input != "quit()":
    message = input("> ")
    msgs.append({"role": "user", "content": message})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=msgs)
    # reply = completion.choices[0].message
    reply = response.choices[0].message.content
    msgs.append({"role": "assistant", "content": reply})
    funny_robot()
    print(f"\n{reply}\n")
