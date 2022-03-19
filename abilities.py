#MindBridge abilities
import random
import pywhatkit

#1) Wikihow
def wikihow(dowhat):
    import os
    import webbrowser
    url = f"https://www.wikihow.com/wikiHowTo?search={dowhat}"

    '''Note: The main creating a lists is beacuse starting soon, Google Chrome
       will install in the C:\Program Files\ folder by default on Windows if it 
       is a 64-bit installer. Chrome 64-bit versions installed in the C:\Program Files (x86)\ 
       folder will continue to work and will be updated just like before.'''

    chromepath_options = [r"c:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
                          r"C:\Program Files\Google\Chrome\Application\chrome.exe"]

    for i in chromepath_options:
        if os.path.exists(i) == True:
            chromepath = i
        else:
            chromepath = i

    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromepath))
    return webbrowser.get("chrome").open_new(url)

#2) Motivational Music

songlist=[
          "I Hope This Song Makes You Feel Special Today",
          "Every Scar Is A Lesson 😥 This song is so empowering!",
          "Such A Beautiful Song! 🥺 So Emotional! 😢 (True Colors Cover)",
          "Crowded House - Don't Dream It's Over (Beautiful Cover Song)",
          "She Sings The Most Beautiful Cover of \"FIX YOU\" by Coldplay (LIVE off the floor)",
          "MY IMMORTAL by Evanescence (LYRICS) The Most Beautiful Cover!",
          ]


def music():
    pywhatkit.playonyt(random.choice(songlist))

#3) Quote Feature

quoteslist=[ "Nothing is impossible. The word itself says I'm possible!",
             "There is no success like failure",
             "Life has got all those twists and turns. You’ve got to hold on tight and off you go.",
            "Keep your face always toward the sunshine, and shadows will fall behind you.",
            "Success is not final, failure is not fatal: it is the courage to continue that counts.",
            "You are never too old to set another goal or to dream a new dream.",
            "You can be everything. You can be the infinite amount of things that people are."
            ]

def quote():
    import random
    return random.choice(quoteslist)

#4)Motivation
def audioplay():
    import playsound as ps
    ps.playsound(r"C:\Users\User\Desktop\LIFEwav.wav")
#4) Abilities to Answer personal question

def byebye():

    return "I hope you enjoyed using me as much as I did helping you....So thank you:). I will see you when I see you."

def gratitude():
    import random
    return random.choice(gratitudes)

def greeting():
    import random
    return random.choice(greetings)

def feeling():
    import random
    return random.choice(feelings)

#Task list

def dont_know():# if the user input something random with Metis is unable to perform
    tasklist = '''Here is a list of what I can do
                        1: "Show you my features"
                        2: "Guide you to articles on how to solve (anything)",
                        3: "Uplifting your mood with some good music",
                        4: "To improve your spirits with some fresh quotes",
                        5: "Emergency Hotline-Talk to someone"
                           '''
    return tasklist

def powers():

    tasklist = '''Here is a list of what I can do
                    1: "Guide you to articles on how to solve(anything)",
                    2: "Uplifting your mood with some good music",
                    3: "To improve your spirits with some fresh quotes",
                    4: "Motivation"
                    5: "Emergency Hotline"

                       '''
    return tasklist

#Keyword List

keyword =     {1: ["powers", "abilities", "features"],
               2: ["how","wikihow"],
               3: ["music","song"],
               4: ['quote',"thought"],
               5: ["audio","motivat","sad","life"],
               "hotline":["abortion","abuse","addiction","cancer","care ","domestic violence","poison","suicide","missing"]
               }# Fill in the keyword list for hotline inside or create a sep variable and an algo and do something

nonab_key={6:["great","awesome","fantastic","thank","wow","cool","best","good","nice","excellent","perfect","love","epic","fabulous"],
            7: ["leave", "bye", "good night", "seeya", "take care", "close", "terminate", "stop", "nothing",
               "leaving", "going", "ttyl"]
           }

#friendly responses

gratitudes=["I'm so excited to do more;)",r"My pleasure_/\_","Always at your service:D","You are welcome:)"]

greetings=["Heyyy! I'm ahamdhi",
           "Yo I'm ahamdhi",
           "Hai,I'm ahamdhi",
           "Hey there!, I'm ahamdhi",
           "hi, I'm ahamdhi"]

feelings=["Im fine!" , "Better than ever!", "Never felt better!" , "Always better than before"]

#files
hotline=["abortion","abuse","addiction","cancer","care ","domestic violence","poison","suicide","missing"]


