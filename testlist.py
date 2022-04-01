import random
import time
i = True
while i == True:
    y_c = random.randint(30,37)
    y = "\033[1;"+str(y_c) + ";40m"
    print(y+"|-----------------|")
    print(" \---------------/")
    print("  ~-_---------_-~")
    print("     ~-_---_-~")
    print("        ~-_")
    print("     _-~---~-_")
    print("  _-~---------~-_")
    time.sleep(0.3)
