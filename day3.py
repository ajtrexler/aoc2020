# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 06:47:27 2020
AOC 2020: Day 3

sudden arboreal trees

@author: adam.trexler
"""
import aoc_funs
import pandas as pd
import numpy as np

def main():
    
    with open("./data/test_day3.txt","r") as f:
        test_data = f.readlines()
        
    aoc_funs.encounter_trees(test_data)     
    
    b_steps = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    all_test_trees = []
    for steps in b_steps:
        all_test_trees.append(aoc_funs.encounter_trees(test_data,
                                                       steps[0],
                                                       steps[1]))
    np.prod(all_test_trees)
    
    with open("./data/day3.txt","r") as f:
        data = f.readlines()
    
    tree_num_a = aoc_funs.encounter_trees(data)  
    print(tree_num_a)
    
    tree_num_b = []
    for steps in b_steps:
        tree_num_b.append(aoc_funs.encounter_trees(data,
                                                   steps[0],
                                                   steps[1]))
    tree_num_b = np.prod(tree_num_b)
    print(tree_num_b)
    

    

if __name__ == "__main__":
    main()
