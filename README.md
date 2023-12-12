# HAL9000 ~ Your retro inspired cli AI-assistant

## Requirements
HAL 9000 lets you generate a terminal based AI assistant on your desktop to have conversations with. You can set a customized personality, and your conversations are conveniently logged to allow you to refer to any content generated by your assistant at a later date.

## Requirements

HAL9000 is written in Python. You will require a Python 3 installation, the openai Python library and an API key from OpenAI with some tokens on your account. For detailed instructions on how to get started with OpenAI, generate an API key, install Python, and install OpenAI's Python library, please visit: https://platform.openai.com/docs/quickstart?context=python

## Built in System Prompts:

`"Who do you need HAL9000 to be today?"`

This project has been updated to include a fork of the Mustvlad's popular repository of premade system prompts. https://github.com/mustvlad/ChatGPT-System-Prompts

Prompts can be preselected via adding an argument at runtime, or they can be selected via an options menu during runtime when HAL9000 asks you to define their personality.

System prompts are an incredibly valuable tool. I suggest you attempt to be as creative with them as possible.

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

## Defining your ai assistant





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
