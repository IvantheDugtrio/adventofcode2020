#!/usr/bin/env python3
import sys

validCount = 0
lineCount = 0
with open(sys.argv[1],'r') as fp:
    for line in fp:
        lineCount+=1
        criteria = line.split(": ")[0]
        password = line.split(": ")[1].strip()
        keyChar = criteria.split(" ")[1]
        keyRange = criteria.split(" ")[0]
        minKeyCnt = int(keyRange.split("-")[0])
        maxKeyCnt = int(keyRange.split("-")[1])
        # Part 1
        #keyCharCount = password.count(keyChar)
        #if keyCharCount >= minKeyCnt and keyCharCount <= maxKeyCnt:
        #    validCount+=1
        # Part 2
        if ((password[minKeyCnt-1] == keyChar or
                password[maxKeyCnt-1] == keyChar) and
            not (password[minKeyCnt-1] == keyChar and
                password[maxKeyCnt-1] == keyChar)):
            validCount+=1
print("There are ",lineCount," passwords given")
print("There are ",validCount," valid passwords")
