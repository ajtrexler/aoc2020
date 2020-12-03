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
