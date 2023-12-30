import os, sys
os.system("git pull")
try:
    __import__("FILE").shuvo_M()
except Exception as e:
    exit(str(e))
