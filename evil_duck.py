import os
import platform
import subprocess
import getpass

from time import sleep

def execute_commands(commands):
    if platform.system() == "Windows":
        # On Windows, use the "start" command to open a new terminal window
        # and execute the commands inside it
        subprocess.Popen(["start", "cmd", "/c"] + commands)
    else:
        # On non-Windows platforms, execute the commands directly in the current terminal
        subprocess.Popen(commands, cwd=os.getcwd())

if __name__ == "__main__":
    # Replace these commands with the ones you want to execute
    commands = [
        "cd ~/Desktop",
        "ls -l",
        "echo 'Done!'"
    ]

    # Get the current user name and home directory
    user_name = getpass.getuser()
    home_dir = os.path.expanduser("~")

    # Change the directory to the user's Desktop
    desktop_dir = os.path.join(home_dir, "Desktop")
    os.chdir(desktop_dir)

    # Execute the commands in a new terminal window or in the current terminal
    execute_commands(commands)