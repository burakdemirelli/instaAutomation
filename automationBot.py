from instabot import Bot
import random
import datetime
import os 
import csv
import shutil
from time import sleep

username = "yanki.kirlikova@gmail.com"
password = "burakedebiyat"

postsPath = "/Users/burakdemirelli/Documents/python/AutomationBot"
postExtension = ".jpg"

loggedIn = False
tag = ["#siir", "#edebiyat", "#sair", "#cemalsureya", "#canyucel", "ozdemirasaf", "siirsokakta", "#turkiye", "#istanbul"]
dayCheck = False

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

def getDay():
    return datetime.datetime.today().weekday()

def getCurrentTime():
    now = datetime.datetime.now()
    return [now.hour, now.minute]

def timeToSeconds(timeArray):
    return timeArray[0]*60*60 + timeArray[1]*60

def getDate():
    return str(datetime.datetime.today().date())

def login():
    try:
        bot.login(username = username, password = password)
        print("Successfully logged in.")
        loggedIn = True
    except:
        print("An error occured trying to log in. Trying again...")
        #bootupSequence()

def postImages(image, captionTxt, tags):
    finalCaption = str(captionTxt) + "                            "
    for tag in tags:
        finalCaption += " " + tag
    bot.upload_photo(image, finalCaption)

#def getPostDirectoryForDate(date):
#    posts = os.listdir("./posts")
#    date += postExtension
#    for post in posts:
#        if date == post:
#            return os.getcwd() + "/posts/" + post
            
def getPostDirectoryForDate(fileName):
    return os.getcwd() + "/posts/" + fileName

def movePost(date):
    shutil.move(getPostDirectoryForDate(date), os.getcwd() + "/posted")

def getDescriptionForDate(date, file_name):
    f = open(file_name, 'r')

    reader = csv.reader(f)
    for row in reader:
        if str(date) == row[0]:
            print(row[1])
            return row[1]
    return 1

while True:
    if not loggedIn:
        login()
    if not dayCheck:
        date = getDate()
        postDirectory = getPostDirectoryForDate(str(date)+postExtension)
        description = getDescriptionForDate(date, "description.csv")
        whenToPost = whenToPost()
        dayCheck = True
    
    #[hours, mins]
    currentTime = getCurrentTime()
    print(currentTime)
    timeUntilPost = [whenToPost[0] - currentTime[0], whenToPost[1] - currentTime[1]]
    print("Time Until Post", timeUntilPost)
    #timeUntilPost = [0, 0]

    sleep(timeToSeconds(timeUntilPost))
    postImages(postDirectory,description,tag)
    #movePost(str(date)+postExtension)

    currentTime = getCurrentTime()
    timeUntilNextDay = [24-currentTime[0], 60 - currentTime[1]]

    sleep(timeToSeconds(timeUntilNextDay))
    dayCheck = False

    