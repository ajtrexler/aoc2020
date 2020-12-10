# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:47:30 2020
Functions for AOC 2020.

@author: adam.trexler
"""
import itertools
import numpy as np
import re
from collections import Counter

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
    
def hgt_helper(x):
    if "cm" in x:
        return 150 <= int(x.replace("cm","")) <= 193
    elif "in" in x:
        return 59 <= int(x.replace("in","")) <= 76
    else:
        return False
    
def check_passport_values(p):
    #p.pop("",None) # remove any empty keys, debris from file load?  
    # rules for each field  
    field_rules = {"byr":"len({x})==4 and int({x})>=1920 and int({x}) <= 2002",
               "iyr":"len({x})==4 and int({x})>=2010 and int({x}) <= 2020",
               "eyr":"len({x})==4 and int({x})>=2020 and int({x}) <= 2030",
               "hcl":"True if re.search(\"#[0-9a-f]{6}\",{x}) else False",
               "ecl":"{x} in [\"amb\",\"blu\", \"brn\", \"gry\", \"grn\", \"hzl\", \"oth\"]",
               "pid":"True if re.search(\"[0-9]{9}\",{x}) else False",
               "cid":"True"
               }
    foo = []
    for f in p:
        v = None
        if f == "hgt":
            v = hgt_helper(p[f])
        elif f == "byr":
            v = len(p[f])==4 and 1920 <= int(p[f]) <= 2002
        elif f == "iyr":
            v = len(p[f])==4 and 2010 <= int(p[f]) <= 2020
        elif f == "eyr":
            v = len(p[f])==4 and 2020 <= int(p[f]) <= 2030
        elif f == "hcl":
            v = True if re.search("^#[0-9a-f]{6}$",p[f]) else False
        elif f == "ecl":
            v = p[f] in ["amb","blu", "brn", "gry", "grn", "hzl", "oth"]    
        elif f == "pid":
            v = True if re.search("^\d{9}$",p[f]) else False   
        elif f == "cid":
            v = True
        else:
            print(p)
            
        if v == None:
            print(p)
        else:
            foo.append(v)

    return all(foo)
#    foo = list(map(lambda x,p: eval(field_rules[p[x]]),p))
#    foo = list(map(lambda x: x,p))
#    list(map(lambda x,p: (eval(field_rules[x],p)),p,itertools.repeat(p)))
#    return(all(foo))

def find_valid_passports(data, cid_valid = True):
    fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]
    if cid_valid == False:
        fields.remove("cid")
    
    passport_list = data.strip().split("\n\n")
    passport_list = [p.replace("\n"," ") for p in passport_list]
    passport_dict = [dict(map(lambda x: x.split(":") if len(x.split(":"))>1 else [x.split(":")[0],""], p.split(" "))) for p in passport_list]
    
    valid_pps = []    
    for p in passport_dict:
        if all([f in p.keys() for f in fields]):
            if check_passport_values(p) == True:
                valid_pps.append(p)
            
            
    return len(valid_pps)
    
def find_seat_id(x):
    row_seq = x[0:7]
    col_seq = x[7:]
    row_seq = row_seq[::-1] # reverse order for easier
    col_seq = col_seq[::-1]
    b = [int(f=="B") for f in row_seq] # convert to binary format
    br = [int(f=="R") for f in col_seq]
    row = sum([(2**i)*n for i,n in enumerate(b)])
    col = sum([(2**i)*n for i,n in enumerate(br)])
    
    seat_id = row*8+col
    return seat_id

def how_many_custom_q(data, question_mode = "any"):
    
    if question_mode == "any":
        data = [t.replace("\n","") for t in data.split("\n\n")]
        ansr_qs = []
        for d in data:
            ansr_qs.append(len(set(dd for dd in d)))
        return sum(ansr_qs)
    elif question_mode == "all":
        data = data.split("\n\n")
        group_sum = []
        for d in data:
            num_people = len(d.rstrip("\n").split("\n"))
            d = d.replace("\n","")
            ansr_qs = Counter(d)
            group_sum.append(sum([v==num_people for v in ansr_qs.values()]))
        return sum(group_sum)

def read_boot_code(data):
    data = [d.replace("\n","") for d in data]
    acc = 0
    idx = [0]
    retval = "corrupt file!"
    while len(set(idx)) == len(idx):#) and (idx[-1] != len(data)+1):
        op,arg = data[idx[-1]].split(" ")
        if op == "acc":
            acc += int(arg)
            idx.append(idx[-1]+1)
        elif op == "jmp":
            idx.append(idx[-1]+int(arg))
        elif op == "nop":
            idx.append(idx[-1]+1)
        if idx[-1] == len(data):
            print("woo!")
            retval = "valid"
            break
    return retval,acc

def fix_boot_code(data):
    data = [d.replace("\n","") for d in data]
    for i,d in enumerate(data):
        op,arg = d.replace("\n","").split(" ")
        drep = None
        if op == "nop":
            drep = "jmp " + arg
        elif op == "jmp":
            drep = "nop " + arg
        if drep != None:
            print(d,drep)
            tmp = data.copy()
            tmp.remove(d)
            tmp.insert(i,drep)
        else:
            tmp = data
        r,acc = read_boot_code(tmp)
        if r == "valid":
            return acc
        

def attack_xmas_data(x, l = 5):
    invalids = []
    for i in np.arange(l,len(x)):
        pset = x[i-l:i]
        target = x[i]
        if not any([sum(c)==target for c in itertools.combinations(pset,2)]):
            invalids.append(target)
    return invalids

def find_xmas_weakness(x,target):
    for rnum in np.arange(2,len(x)):
        # need to do sliding sum
        if any([sum(x[i-rnum:i]) == target for i in np.arange(rnum,len(x))]):
            print(rnum)
            seq = [x[i-rnum:i] for i in np.arange(rnum,len(x))]
            idx = np.where(np.array([sum(c) for c in seq]) == target)
            tmp = seq[idx[0][0]]
            return max(tmp) + min(tmp)


        