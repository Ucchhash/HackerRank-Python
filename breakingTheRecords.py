#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    highScore  = lowScores= scores[0]
    highCount = 0
    lowCount = 0
    for i in scores[1:]:
        if i > highScore:
            highCount+=1
            highScore = i
        if i < lowScores:
            lowCount+=1
            lowScores = i
    return highCount,lowCount
   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
