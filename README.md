# HAL9000 ~ Your retro inspired cli AI-assistant
**EDIT: UPDATE IN PROGRESS**
## Description

HAL9000 is an ultra convenient way to generate a unique instance of ChatGPT-3.5-Turbo in a terminal window on your desktop. Being able to gain access to one of the world's most powerful AIs, and generate tailored instances instanteously from a terminal is incredibly useful. You can set a customized personality (system prompt), and your conversations are conveniently logged locally to allow for you to refer to any content generated by your AI assistant at a later date. I have also forked and catalogued ChatGPT system prompts from some of the most popular repositories on Github. 

F's awesome-chatgpt-prompts: https://github.com/f/awesome-chatgpt-prompts

Spdustin's ChatGPT-AutoExpoert: https://github.com/spdustin/ChatGPT-AutoExpert

Mustvlad's ChatGPT-System-Prompts: https://github.com/mustvlad/ChatGPT-System-Prompts

## Really consider testing this one out for yourself.

This is hands down the most useful application I have ever made for myself. Sure, you can use the OpenAI app to gain access to ChatGPT. You could also set it up through Siri. You can use the unofficial app to gain access. I really like the idea of keeping it simple. With less than 100 lines of code, I can gain direct access to the world's most powerful AIs directly in from the terminal on my desktop. No telemetry, beyond what OpenAI is logging on their end. Maximum convenience, with all conversations being logged locally. 

A close friend of mine said this recently, "I think ChatGPT is probably the most profound technology that has happened since the internet, and we're just figuring out the very beginning of what can be done with it. Think the internet but in 1993, that's where we are now with LLMs, but they're going to change the world as profoundly as the internet did."

So why not have that tool sitting in a terminal on your desktop, with some old-school retro flair to boot.

"Hello, Dave. You're looking well today."


## Requirements

HAL9000 is written in Python. You will require a Python 3 installation, the openai Python library and an API key from OpenAI with some tokens on your account. For detailed instructions on how to get started with OpenAI, generate an API key, install Python, and install OpenAI's Python library, please visit: https://platform.openai.com/docs/quickstart?context=python


## Customizing the Nature of Your AI Assistant Manually or With Built in System Prompts:

`"Who do you need HAL9000 to be today?"`

System prompts are an incredibly valuable tool. I suggest you attempt to be as creative with them as possible. These allow you to format output, or create specific personalities that will shape the responses your AI assistant generates.

OpenAI have an indepth guide on prompt engineering that is a fantastic resource: https://platform.openai.com/docs/guides/prompt-engineering

This project has been updated to include a fork of the Mustvlad's popular repository of premade system prompts, allowing for you to have a plethora of options to choose from. https://github.com/mustvlad/ChatGPT-System-Prompts

Prompts can be preselected via adding an argument at runtime, or they can be selected via an options menu during runtime when HAL9000 asks you to define their personality.



## Usage

**To run the program with your global Python interpreter:**

```
git clone https://github.com/0x00wolf/HAL9000
pip install openai
cd ./HAL9000
# Copy and paste your API key into the designated variable in hal9000.py
python3 ./hal9000.py
```

**To run the program in a virtual environment:**

```
git clone https://github.com/0x00wolf/HAL9000
cd ./HAL9000
python3 -m venv venv
source ./venv/bin/activate
pip install open ai
./python3 ./hal9000.py
```

**To use a preselected system prompt at runtime, simply enter the path as a second argument into your terminal:**

`$ python3 ./hal9000.py './prompts/originals/red-team-operator'`

If launched in this manner, HAL9000 won't ask you to define a personality, and instead will automatically greet you and look for your initial query.


**To quit the program** enter: ctrl+c

Or input: 'quit' + enter.


## Logging

By default all of your conversations will be logged into the logs directory. The logs directory and the log-number.txt file are necessary for the program to run. Logfiles are saved as '.txt' files, but they are in JSON format.

The easiest way to review past logs is by launching a Python shell in the logs folder. 

`/logs/ $ python3`

Next you'll need to import JSON from the Python standard libary.

`>>> import json`

Then open the log that you're interested in reviewing:

```
with open('log1.txt', 'r') as f:
    dict = json.load(f)
```

Now you can print the log entries one at a time.

`print(dict[0]['content']) # display the system prompt`

`print(dict[1]['content']) # display your first query to the AI`

`print(dict[2]['content']) # display the AIs first response`

And so on.

If you want to save a conversation to a text file in human readable format this is one method:

```
import json
with open('log1.txt', 'r') as f:
  dict = json.load(f)
savefile = open('./savefile.txt', 'w')
for i in range(len(dict)):
  savefile.write(f"{dict[i]['role']:\n{dict[i]['content']}\n\n---------\n")
savefile.close()
```

I don't really intend on building log review into this project at any point, as using the Python shell is just fine with me, but if someone feels inspired please fork the code. 
