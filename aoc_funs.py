# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:47:30 2020
Functions for AOC 2020.

@author: adam.trexler
"""
import itertools
import numpy as np

def fix_expense_report(values, target = 2020, mode = 2):
    for c in itertools.combinations(values,mode):
        if sum(c) == target:
            return np.prod(c)

def find_valid_pws(values, pw_policy = "sled rental"):
    valids = []
    for value in values:
        # parse the contents of the rules and pw data
        rules = value.split(":")[0]
        pw = value.split(":")[1].lstrip()
        lb = int(rules.split("-")[0])
        ub = int(rules.split("-")[1].split(" ")[0])
        ltr = rules.split("-")[1].split(" ")[1]
        # find number of occurrences of ltr in pw
        # this won't work if rules contain more than 1 letter.
        occs = sum([ltr == p for p in pw])
        
        if pw_policy == "sled rental":
            if occs >= lb and occs <= ub:
                valids.append(pw)
        elif pw_policy == "toboggan corp":
            if (pw[lb-1] == ltr and pw[ub-1] != ltr) or \
                (pw[lb-1] != ltr and pw[ub-1] == ltr):
                valids.append(pw)
    # return the list of valid pws
    return valids

def encounter_trees(data, right = 3, down = 1):
    
    data = [d.replace("\n","") for d in data]
    c = len(data[0])
    r = len(data)
    tmp_data = "".join(data)
    foo = [int(d=="#") for d in tmp_data]
    foo = np.reshape(foo,(r,c))
                  
    stepsize = right+(c*down)
    number_steps = (r-1) // down
    idxs = [stepsize+(j*stepsize) for j in range(number_steps)]
    #idxs = np.arange(stepsize,stepsize*r,stepsize)
    #idxs = np.arange(stepsize,r*c,stepsize)

    trees = []
    for i,pos in enumerate(idxs):
        if i < len(idxs):
            trees.append(foo[i*down+down,(pos % (right*c)) % c])
    return(sum(trees))
