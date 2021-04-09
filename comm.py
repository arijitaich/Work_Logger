import subprocess, pathlib
import time
import os
from datetime import datetime

def prepend_line(file_name, line):
    """ Insert given string as a new line at the beginning of a file """
    # define name of temporary dummy file
    dummy_file = file_name + '.bak'
    # open original file in read mode and dummy file in write mode
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Write given line to the dummy file
        write_obj.write(line + '\n')
        # Read lines from original file one by one and append them to the dummy file
        for line in read_obj:
            write_obj.write(line)
    # remove original file
    os.remove(file_name)
    # Rename dummy file as the original file
    os.rename(dummy_file, file_name)




r = 1
while (r==1):
    x = input("Enter response: ")
    print("Sending...", end="\r")
    time.sleep(0.5)
    now2 = datetime.now()
    dt = now2.strftime("%d/%m/%Y %H:%M:%S")

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    cc1 = " - "
    cc = ": "
    yy = dt + cc + x
    prepend_line("a1.txt", yy)
    print("Sent", end="\r")
    time.sleep(0.5)

    
print()