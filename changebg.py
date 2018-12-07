import subprocess

name = input('enter theme-file name: ')

subprocess.Popen(['osascript','scripts/terminal/' + name + '.scpt']) #run process in terminal (for terminal application) - is powerful.
