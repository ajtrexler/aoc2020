# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 07:49:50 2020

@author: adam.trexler
"""

import aoc_funs

def main():
    
    with open("./data/test_day4.txt","r") as f:
        test_data = f.read()
    
    aoc_funs.find_valid_passports(test_data, cid_valid = False)
    
    with open("./data/test_invalid_day4.txt","r") as f:
        data = f.read()
    aoc_funs.find_valid_passports(data, cid_valid = False)
    
    with open("./data/test_valid_day4.txt","r") as f:
        data = f.read()
    aoc_funs.find_valid_passports(data, cid_valid = False)
    
    with open("./data/day4.txt","r") as f:
        data = f.read()
    
    aoc_funs.find_valid_passports(data, cid_valid = False)
        
    
    
if __name__ == "__main__":
    main()