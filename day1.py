# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:44:37 2020
AOC 2020: Day 1
@author: adam.trexler
"""
import aoc_funs

def main():
    
    test_data = [1721,979,366,299,675,1456]
    test1 = aoc_funs.fix_expense_report(test_data)
    assert test1 == 514579
    
    test2 = aoc_funs.fix_expense_report(test_data,mode = 3)
    assert test2 == 241861950
    
    with open("./data/day1.txt","r") as f:
        data = f.readlines()
    data = [int(d) for d in data]
    answer1a = aoc_funs.fix_expense_report(data)
    print(answer1a)
    
    answer1b = aoc_funs.fix_expense_report(data,mode = 3)
    print(answer1b)
    
    
    
    
    
if __name__ == "__main__":
    main()