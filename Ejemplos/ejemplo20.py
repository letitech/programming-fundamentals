from time import sleep
from random import randint

count = 20
for i in range(100):
    snow = " * " * randint(1, count)
    space = " "  * randint(1, 50)
    sleep(0.5)
    print(snow.replace(" ", space))
    
