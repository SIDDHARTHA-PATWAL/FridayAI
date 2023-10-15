# This is a sample Python script.
import webbrowser
import pyautogui
import datetime
import requests
import subprocess  # subprocess.call
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import speech_recognition as sr
import os
import win32com.client
from gtts import gTTS
speaker=win32com.client.Dispatch("SAPI.SpVoice")

import openai
from config import apikey
openai.api_key = apikey
def say(text):
    speaker.Voice = speaker.GetVoices("Language=409;Gender=Female").Item(0)
    speaker.Speak(f" {text}")
    # tts = gTTS(text=text, lang='hi')
    # tts.save('output.mp3')
    # os.system('start output.mp3')
    # #os.remove('output.mp3')
    #os.system(f"say {text}")

def ai(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": message
            },
            {
                "role": "assistant",
                "content": "Hi there! How can I assist you today?"
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response["choices"][0]["message"]["content"])
    say(response["choices"][0]["message"]["content"])

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold =  0.8  #default pause_threshold jis 0.8
        audio = r.listen(source)
        try:
            query=r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            print("sorry  from Friday, some error occurred")
            return " sorry  from Friday, some error occurred "
def get_weather_forecast(location):
    api_key = "00f794c982b7bbbdd286bbd46d596126"  # Replace with your actual API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    weather_data = response.json()

    if "weather" in weather_data:
        description = weather_data["weather"][0]["description"]

        main=weather_data['main']
        temperature= main['temp']
        pressure=main['pressure']
        humidity=main['humidity']

        visibility=weather_data['visibility']

        wind=weather_data["wind"]
        wind_speed=wind['speed']
        wind_direction=wind['deg']
        cloudiness=weather_data["clouds"]['all']
        say(f"The weather in {location} is {description}.")
        say(f"The temperature is {temperature-273} Celcius ,the pressure is {pressure}  Hectopascals ,and humidity is {humidity} percent")

        print("Do you want to know more details?")
        say("Do you want to know more details?")
        print("Listenting for YES or NO..")
        answer=takeCommand()
        if ("yes" or "yup" or "ofcourse") in answer.lower():
            say(f"the visibilty is {visibility} metres,wind speed is {wind_speed} metres per second {wind_direction} degrees (°) from true north and the cloudiness is {cloudiness} percent")
        else :
            say("Have a good day ,sir")

    else:
        say("Sorry, I couldn't retrieve the weather information.")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hi, {name}")  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
say("Hello , I am Friday , your personal AI assistant")

'''
while True:
    print("enter text")
    s=input()
    if(s.lower()=="stop"):
        say("stopping..")
        break
    say(s)  '''
sites=[["Youtube","https://www.youtube.com/"],["Leetcode","https://leetcode.com/SIDDHARTHA_PATWAL/"],["Instagram","https://www.instagram.com/"],["Google","https://www.google.com"]]
while 1:
    print("Listening...")
    text=takeCommand()
    if text.lower()=="stop":
        say("stopping..")
        break
    if "open"  in text.lower() or "close" in text.lower():
        for site in sites:
            if f"open {site[0]}".lower() in text.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
            if f"close {site[0]}".lower() in text.lower():
                say(f"Closing {site[0]} sir...")
                # Simulate Ctrl+W keyboard shortcut to close the active tab
                pyautogui.hotkey('ctrl', 'w')
    elif "play music".lower() in text.lower():
        #musicPath="C:\\Users\\siddh\\OneDrive\\Desktop\\be_it.mp4"
        #musicPath=r"C:\Users\siddh\OneDrive\Desktop\be_it.mp4"
        musicPath=r".\be_it.mp4"
        print("Playing music sir..")
        say("Playing music sir..")
        os.system(f"start {musicPath}")
    # elif "the time".lower() in text.lower():
    #     strfTime=datetime.datetime.now().strftime("%H:%M:%S")
    #     say(f" sir , the time is {strfTime}")
    elif "the time" in text.lower():
        strfTime = datetime.datetime.now().strftime("%H:%M:%S")
        say(f"Sir, the time is {strfTime}")


    elif "weather" in text.lower():
        say("Sure, please provide the location.")
        print("Listening for entry into weather...")
        location = takeCommand()
        get_weather_forecast(location)
    elif "use artificial intelligence".lower() in text.lower():
        print("starting open ai model")
        print("you can start your query")
        message=takeCommand()
        if message==" sorry  from Friday, some error occurred ":
            say("sorry , query not reached")
            print("sorry , query not reached")
        else:
            ai(message)


    # elif "open word".lower() in text.lower():
    #
    #     print("Starting Microsoft Word, sir...")
    #
    #     say("Starting Microsoft Word, sir...")
    #
    #     subprocess.Popen(["start", "winword"])

    else:
            print(1)
            say(text)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
