# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 05:52:11 2020
attack XMAS?!
@author: adam.trexler
"""
       
def main():
    with open("./data/test_day9.txt","r") as f:
    test_data = f.readlines()
    test_data = [int(t) for t in test_data]


    testa = aoc_fun.attack_xmas_data(test_data)[0]
    aoc_funs.find_xmas_weakness(test_data,testa)
    
    with open("./data/day9.txt","r") as f:
        data = f.readlines()
    data = [int(t) for t in data]
    
    foo = aoc_funs.attack_xmas_data(data,l=25)[0]
    aoc_funs.find_xmas_weakness(data,foo)

if __name__ == "__main__":
    main()