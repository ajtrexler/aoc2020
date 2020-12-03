# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 09:52:00 2020
AOC 2020: Day 2
@author: adam.trexler
"""
import aoc_funs

def main():
    test_data = ["1-3 a: abcde",
                 "1-3 b: cdefg",
                 "2-9 c: ccccccccc"]
    
    valid_test_pw = aoc_funs.find_valid_pws(test_data)
    print(len(valid_test_pw))
    
    with open("./data/day2.txt","r") as f:
        data = f.read()
    data = data.split("\n")
    data.remove("")
    
    valid_pw_a = aoc_funs.find_valid_pws(data)
    print(len(valid_pw_a))
    
    valid_pw_b = aoc_funs.find_valid_pws(data, pw_policy = "toboggan corp")
    print(len(valid_pw_b))

if __name__ == "__main__":
    main()
