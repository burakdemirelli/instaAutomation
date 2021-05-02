from instabot import Bot
import random
import datetime

username = ""
password = ""

bot = Bot()

weekdays = {
    0 : "monday",
    1 : "tuesday",
    2 : "wednesday",
    3 : "thursday",
    4 : "friday",
    5 : "saturday",
    6 : "sunday"
    }

timesToPost = {
    "monday" : [11, 14],
    "tuesday": [10, 15],
    "wednesday": [11, 14],
    "thursday": [10, 14],
    "friday" : [9, 14],
    "saturday": [9, 11],
    "sunday" : [8, 14]
    }


def bootupSequence():
    print("Enter your username:")
    username = input()
    print("Enter your password:")
    password = input()

    if(username != "" or password != ""):
        print("Username and password succesfully saved. Logging in...")
        login()
    else:
        print("Could not save username or password. Trying again...")
        bootupSequence()

def whenToPost():
    range = timesToPost[
        weekdays[
            datetime.datetime.today().weekday()
            ]
    ]
    hour = random.randint(range[0], range[1])
    minute  = random.randint(0, 60)

    return [hour, minute]

def login():
    try:
        bot.login(username = username, password = password)
        print("Successfully logged in.")
    except:
        print("An error occured trying to log in. See above for details.")

def postImages(image, captionTxt, tags):
    finalCaption = captionTxt + "  "
    for tag in tags:
        finalCaption += " " + tag
    bot.upload_photo(image, finalCaption)

