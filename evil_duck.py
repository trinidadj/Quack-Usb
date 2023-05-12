from keyboard import press_and_release, write
from os import getcwd
from time import sleep
from getpass import getuser

user_name = getuser()
current_dir = getcwd()

press_and_release("left windows + r")
sleep(0.2)
write("cmd")
press_and_release("enter")
sleep(0.2)

command = ["""cd C:\\Users\\{}\\Desktop""".format(user_name),]
#change the command to your needs

for cmd in command:
      write(cmd)
      press_and_release("enter")
      
