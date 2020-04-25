#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    birdTypeCount = [0,0,0,0,0,0]
    for i in range(len(arr)):
        birdTypeCount[arr[i]] += 1
    return birdTypeCount.index(max(birdTypeCount))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
