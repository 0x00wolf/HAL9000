# pip install openai
import openai
import os
import sys
from time import sleep
from random import randint
from json import dump
import readline


client = openai.OpenAI(
    api_key="INSERT_API_KEY")  # Insert your ChatGPT API key here


def corny_intro():
    print("\n" * 40 + "[*] HAL 9000 ~ performing startup checks")
    sleep(1)
    print('[*] HAL 9000 ~ neural network initialized.')
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
        sleep(2)


def goodbye_hal():
    print("Goodbye, Dave.")
    sys.exit()


def init_log():
    with open('./logs/log-number.txt', 'r') as f:
        log_number = int(f.read())
    log_number += 1
    with open('./logs/log-number.txt', 'w') as f:
        f.write(str(log_number))
    new_log = f'./logs/log{log_number}.txt'
    with open(new_log, 'x') as f:
        pass
    return new_log


def log_conversation(_logfile, messages):
    with open(_logfile, 'w') as f:
        dump(messages, f, indent=6)


if __name__ == '__main__':
    try:
        logfile = init_log()
        msgs = corny_intro()
        while input != "quit":
            message = input("> ")
            msgs.append({"role": "user", "content": message})
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=msgs)
            reply = response.choices[0].message.content
            msgs.append({"role": "assistant", "content": reply})
            funny_robot()
            print(f"\n{reply}\n")
            log_conversation(logfile, msgs)
        goodbye_hal()
    except KeyboardInterrupt:
        goodbye_hal()
