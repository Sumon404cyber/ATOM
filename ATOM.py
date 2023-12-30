import os, sys
os.system("git pull")
try:
    __import__("FILE").fuck()
except Exception as e:
    exit(str(e))
