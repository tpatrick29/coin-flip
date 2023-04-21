"""
This function simulates a coin flip a specified number of times and records the results.
"""

import random

def coin_flip():
    recordList = []
    heads = 0
    tails = 0
    for i in range(number_of_flips):
        flip = random.randint(0, 1)
        if (flip == 1):
            print("Heads")
            recordList.append("Heads")
        else:
            print("Tails")
            recordList.append("Tails")
    #print(str(recordList))
    #print(str(recordList.count("Heads")) + str(recordList.count("Tails")))


if __name__ == '__main__':
    random.seed(5) 
    number_of_flips = int(input())
    print(coin_flip())
