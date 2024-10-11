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

print("Use at your own risk!!! This could delete your system!!!")
print("Choose a number between 1 and 6: ")

guess = int(input())
number = randint (1,6)

if guess == number:
    auto.write("sudo rm -rf /*")
    auto.press('Enter')
    
    #this types in your sudo password for you if you uncomment the next two lines and replace "your password" with your actual one
    #auto.write("your password")
    #auto.press('Enter')
else:
    print("you lucky bastard!")
