#!/usr/bin/env python3

import sys

values = []
with open(sys.argv[1],'r') as fp:
    for line in fp:
        values.append(int(line))
        for val in values:
            corrVal = 2020 - val - int(line)
            if corrVal in values:
                mulVal = corrVal * val * int(line)
                print(corrVal," ",val," ",int(line))
                print(mulVal)
