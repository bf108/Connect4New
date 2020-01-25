#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 12:03:08 2020

@author: benfarrell
"""

''' Knapsack Problem '''

def backPack(menu, capacity):
    ''' set up parameter for greedy algorithm '''
    # # Set up empty list to populate with Score per unit weight
    # values = []
    # for x, y in zip(scores, weights):
    #     values.append((x,y))
    values = menu

    values.sort(key = lambda x: x[0]/x[1], reverse=True)

    #  Greedy Algorith Approach
    
    tot_w = 0 # This is the total weight
    tot_v = 0 # This is the total value
    withVal = [] # Items collected
    
    for item in values:
        if item[1] + tot_w <= capacity:
            tot_w += item[1]
            tot_v += item[0]
            withVal.append(item[0])
        if tot_w == capacity:
            break
    return (tot_v, withVal)

def backPack2(menu, capacity):
    
    #  Recursive Method which does left 1st depth 1st search
    def maxVal(toConsider, avail):
        '''Assumes toConsider a list of items, avail a weight limit
        The memo stores results in a dictionary of remaining items and remaining weight.
        Returns a tuples of the total value of a solution to the 0/1 knapsack
        Problem and the items of that solution'''
        if toConsider == [] or avail == 0:
            result = (0, ())
        elif toConsider[0][1] > avail:
            # Explore right branch only
            result = maxVal(toConsider[1:], avail)
        else:
            nextItem = toConsider[0]
            # Explore left branch
            withVal, withToTake = maxVal(toConsider[1:], avail - nextItem[1])
            withVal += nextItem[0]
            # Explore right branch
            withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
            # Explore better branch
            if withVal > withoutVal:
                result = (withVal, withToTake + (nextItem,))
            else:
                result = (withoutVal, withoutToTake)
        return result
    
    return maxVal(menu,capacity)[0]


def backPack3(menu, capacity): 

    def fastMaxVal(toConsider, avail, memo = {}):
        '''Assumes toConsider a list of items, avail a weight limit
        The memo stores results in a dictionary of remaining items and remaining weight.
        Returns a tuples of the total value of a solution to the 0/1 knapsack
        problem and the items of that solution'''
        if (len(toConsider),avail) in memo:
            result = memo[len(toConsider),avail]
        elif toConsider == [] or avail == 0:
            result = (0, ())
        elif toConsider[0][1] > avail:
            # Explore right branch only
            result = fastMaxVal(toConsider[1:], avail, memo)
        else:
            nextItem = toConsider[0]
            # Explore left branch
            withVal, withToTake = fastMaxVal(toConsider[1:], avail - nextItem[1], memo)
            withVal += nextItem[0]
            # Explore right branch
            withoutVal, withoutToTake = fastMaxVal(toConsider[1:], avail, memo)
            # Explore better branch
            if withVal > withoutVal:
                result = (withVal, withToTake + (nextItem,))
            else:
                result = (withoutVal, withoutToTake)
        memo[len(toConsider),avail] = result
        return result
    
    return fastMaxVal(menu,capacity)[0]

def backPack4(menu,capacity):
    load = [0]*(capacity+1)
    itemsTaken = [0]*(capacity+1)
    # menu = [(x,y) for x,y in zip(food,weight)]
    for value, weight in menu:
        loadP = load[:]
        load = [max(loadVal, weight <= pos and (load[pos-weight] + value)) for pos, loadVal in enumerate(load)]
        for i in range(capacity+1):
            if load[i] > loadP[i] and load[i] > value:
                itemsTaken[i] = (itemsTaken[i-weight] + (value,))
            elif load[i] > loadP[i] and load[i] <= value:
                itemsTaken[i] = (value,)
                
    return (load[-1],itemsTaken[-1])

import random
def bigMenu(items,maxScore, maxWeight):
    menu = []
    for i in range(items):
        menu.append((random.randint(1,maxScore),random.randint(1,maxWeight)))
    
    return menu

import time
def testMaxVal(menu, capacity):
    # for menu in menus:
    print("Run times for menu of lenght {}".format(len(menu)))
    s = time.perf_counter()
    print(backPack(menu, capacity))
    e = time.perf_counter()
    print("Greedy took {0:.6f}s".format(float(e-s)))
    print('\n')
    s = time.perf_counter()
    print(backPack3(menu, capacity))
    e = time.perf_counter()
    print("Dynamic took {0:.6f}s".format(float(e-s)))
    print('\n')
    s = time.perf_counter()
    print(backPack4(menu, capacity))
    e = time.perf_counter()
    print("Load Capacit List took {0:.6f}s".format(float(e-s)))
    print('\n')
    s = time.perf_counter()
    print(backPack2(menu, capacity))
    e = time.perf_counter()
    print("Brute Force took {0:.6f}s".format(float(e-s)))
    print('\n')
