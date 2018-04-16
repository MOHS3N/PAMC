import time
import os


print("Time is :" + time.ctime())
print(os.getcwd())
totalTime = 3
curentTime = 0

while(curentTime <= totalTime):
    time.sleep(5)
    print(curentTime)
    curentTime = curentTime + 1
