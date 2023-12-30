import os, sys
os.system("git pull")
try:
    __import__("ATOM").shuvo_M()
except Exception as e:
    exit(str(e))
