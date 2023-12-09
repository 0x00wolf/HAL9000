# pip install openai
import openai
from time import sleep # if corny intros arent your thing you can delete this too.


client = openai.OpenAI(
    api_key = "insertkeyhere" # Insert your ChatGPT API key here
)


def corny_intro():
    """if corny intros arent your thing copy lines 16 and 17 and paste them in 
    place of line 25, and then delete this function"""
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
    print(f"\n{reply}\n")
