#!/bin/python3

import sys

def solve(arr, money):
    # find 2 indices (Johnny, Sunny) in which the sum of them is equal to money
    lookup = {}
    # set the lookup dictionary with key : target - johnny's cost, value: index
    for i, cost in enumerate(arr):
        index = i + 1
        lookup[money - cost] = index
    # now let's see if there is a cost in the array that satisfies target - johnny
    for i, cost in enumerate(arr):
        index = i + 1
        if cost in lookup.keys():
            smaller = index
            bigger = lookup[cost]
            # if index is bigger, then switch the smaller and bigger index
            if lookup[cost] < index:
                smaller = lookup[cost]
                bigger = index
            print(smaller, bigger)
            return 

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        # money the person has
        money = int(input().strip())
        # number of flavor avaiable
        n = int(input().strip())
        # cost of each flavor
        arr = list(map(int, input().strip().split(' ')))
        solve(arr, money)
