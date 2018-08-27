#!/usr/bin/env python

numpairs = [(5, 1),(1,5),(5,0),(0,5)]

total = 0

for x, y in numpairs:
    try:
        quotient = x/y
    except Exception as e:
        print("uh-oh, when y = {}, {}".format(y, e))
    else:   
        total += quotient  # <1>
print(total)