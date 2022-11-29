import time
import random

lyrics = ("I just wanna be yours")

abc = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ")
to_print = ""
f=0

while to_print!=lyrics:
    x=random.randint(0,52)
    if(abc[x]==lyrics[f]):
        to_print+=lyrics[f]
        f+=1
        print(to_print)
    else:
        time.sleep(0.01)
        print(to_print+abc[x])