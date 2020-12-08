# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 05:36:30 2020
back to the opcode
@author: adam.trexler
"""

import aoc_funs

def main():
    with open("./data/test_day8.txt","r") as f:
        test_data = f.readlines()
    
    print(aoc_funs.read_boot_code(test_data))
    print(aoc_funs.fix_boot_code(test_data))
    
                
    with open("./data/day8.txt","r") as f:
        data = f.readlines()
    
    print(aoc_funs.read_boot_code(data))
    print(aoc_funs.fix_boot_code(data))

if __name__ == "__main__":
    main()

