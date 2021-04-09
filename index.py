import subprocess, pathlib
import time
import os

print("\n")
print("Welcome to Work Logger")
print("Version 1.0 launched on 30th March 2021")
print("Author: Arijit Aich")
print()
x = input("Enter username: ")
y = input("Enter passkey: ")

print("Connecting.", end="\r")
time.sleep(1)
print("Connecting..", end="\r")
time.sleep(1)
print("Connecting...", end="\r")
time.sleep(1)
print("Connected.   ", end="\r") 

print()
# print()
time.sleep(1)

r = 1

while (r==1):
    # Reading File   
    f = open("a1.txt", "r") 
    x = f.read()
    print(x, end="\r")
    time.sleep(0.5)
    os.system( 'clear' )



