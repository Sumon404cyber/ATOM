import os, sys
os.system("git pull")
try:
    __import__("ATOM").fuck()
except Exception as e:
    exit(str(e))
