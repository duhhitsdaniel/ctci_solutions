import random

import math

import itertools

import numpy as np

# 1.1 - determine if string has all unique characters

def unique_string(str):
    str = str.lower().replace(' ','')
    total = 0
    for char in str:
        total += str.count(char)
    if total > len(str):
        print("False")
    else:
        print("True")
            
        
# 1.2 - Given two strings, check if one is permuation of the other

def check_permutation(string_1, string_2):
    count = 0
    for char in string_2:
        if char in string_1:
            count += 1
    if count == len(string_1): 
        print("Count: {}/{}".format(count, len(string_1)))
        print("Is permuation")
    else:
        print("Count: {}/{}".format(count, len(string_1)))
        print("Is not permuation")
        
        
string_1 = 'ABC'
string_2 = 'CAB'
            

# 1.3 - URLify - replace ALL spaces in string with '%20'

def URLify(str):
    str = "%20".join(str.split())
    print(str)
    
    
# 1.4 - determine if given string is a permuation of a pallindrome

def if_pallindrome(str):
    str = str.replace(' ','')
    count_odd = 0
    count_even = 0
    pool = set(list(str))
    values = []
    for char in pool:
        value = str.count(char)
        values.append(value)
    for x in values:
        if not x % 2:
            count_even += 1
        else:
            count_odd += 1
    if count_even > 0 and count_odd < 2:
        print("Is permuation of pallindrome.")
    else:
        print("Is not permuation of pallindrome.")
        
        
# 1.5 - determine if 2 strings are 1 or 0 edits away from eachother

def one_away(string_1, string_2):
    count = 0
    for char in string_2:
        if char in string_1:
            count += 1
    if len(string_1) < len(string_2):
        result = count - len(string_2)
    else:
        result = count - len(string_1)
    if -1 <= result <= 0:
        print("True")
    else:
        print("False")
    print("# of Edits Away: {}".format(result * -1))
        
        
# 1.6 - compress string - ex: 'aabccccaaa' = 'a2b1c3a3'

def string_compress(string):
    string = string.replace(' ','')
    bustdown = list(string)
    letters = []
    counts = [sum(1 for _ in group) for _, group in itertools.groupby(bustdown)]
    for i in range(len(bustdown)):
        if i < len(bustdown) - 1:
            if bustdown[i + 1] == bustdown[i]:
                pass
            else:
                letters.append(bustdown[i])
        else:
            letters.append(bustdown[i])
    insert_count = 1
    for value in counts:
        letters.insert(insert_count, value)
        insert_count += 2
    output = "".join(map(str, letters))
    print(output)
    
    
# 1.7 rotate image defined as NxN matrix (N=4) 90 degrees - do in place if possible

def rotate_img_90(height=1, width=1, turns=0):  # clockwise = turns * -1
    img_matrix = np.arange(height*width).reshape(height, width)
    rotation = np.rot90(img_matrix, turns)
    print(rotation)
    

# 1.8 - if element in matrix == 0, set that row & column to 0's
    
def zero_matrix_v2(matrix):
    rows = []
    columns = []
    count = -1
    row_num = -1
    it = np.nditer(matrix, op_flags=['readwrite'])
    for x in it:
        count += 1
        if count % len(matrix[0]) == 0:
            row_num += 1
        col_num = count - (len(matrix[0]-1) * row_num)
        if x == 0:
            rows.append(row_num)
            columns.append(col_num)
    matrix[np.ix_(rows)] = 0
    for col in columns:
        matrix[:, col] = 0
    print(columns)
    print(rows)
    print(matrix)
    
                
matrix_1 = np.arange(30).reshape(5,6)
matrix_2 = np.array([
    [0,1,2,3,4,5],
    [6,7,8,9,10,11],
    [12,13,0,15,16,17],
    [18,19,20,21,22,23],
    [24,25,26,27,28,29],
    [30,31,32,33,34,0]
])
matrix_3 = np.array([[3,1,2],[3,4,5],[6,7,0]])


# 1.9 - check if one word is substring/rotation of the other using only one call to function

def is_substring(str_1, str_2):
    letters_1 = list(str_1)
    letters_2 = list(str_2)
    for letter in letters_2:
        letters_2.insert(0, letters_2[-1])
        letters_2.pop(-1)
        if letters_2 == letters_1:
            break
    if letters_1 == letters_2:
        print("Is Rotation")
    else:
        print("Is Not Rotation")

        
str_1 = "waterbottle"
str_2 = "terbottlewa"
