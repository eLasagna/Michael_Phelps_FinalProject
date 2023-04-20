# Group: Michael Phelps
    # Name: Ethan Lansangan
    # Name: Jake Pielage
    # Name: James Keen
    # Name: Branden McKinney
# Assignment Title: Final Project
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: This demonstrates our ability to use Pillow, JSON files, and .txt files
# Citations: 
# Anything else that's relevant: 

# functions.py

import json
from PIL import Image


def locationHint(team_name):
    # Opening JSON file
    hintsJson = open('Hints.json')
    # returns JSON object as a dictionary
    hints = json.load(hintsJson)
    ourHints = hints[team_name]
    ourHints = [int(i) for i in ourHints]
    # Opening the txt file and saving it as a lsit
    wordsTxt = open('english.txt')
    words = wordsTxt.readlines()
    # Index the list of words using our hints
    for i in range(0,len(ourHints)):
        wordIndex = ourHints[i]-1
        print(words[wordIndex])

def displayPhoto():
    picFile = "ourPic.png"
    Pic = Image.open(picFile)
    Pic.show()
