# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from openai import OpenAI
from speechtotext import speechtotext, translatekannadatoenglish
from streamfunction import streamfunction

client = OpenAI()


def print_hi(name):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": "What is the name of the person who set foot on the moon for the first time"}
        ]
    )
    print(completion.choices[0].message)
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def getcontentfromuser():
    content = input("User: ")
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": content}
        ]
    )
    chatgptresponse = completion.choices[0].message.content
    print(chatgptresponse)

def chatbotchatgptsimplesample():
    global message
    messages = []

    while message == input("") and input != "quit()":
        #message = input("")
        messages.append({"role": "user", "content": message})
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages)
        reply = response.choices[0].message.content
        print("\n" + reply + "\n")
        messages.append({"role": "assistant", "content": reply})


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi("Telestreak")
    getcontentfromuser()
    chatbotchatgptsimplesample()
    streamfunction()
    speechtotext()
    translatekannadatoenglish()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
