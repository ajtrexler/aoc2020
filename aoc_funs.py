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

            