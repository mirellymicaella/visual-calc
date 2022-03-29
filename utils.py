from math import *

FLOAT_TYPE = 'FLOAT'
INT_TYPE = 'INT'

def sort_numbers_size(a,b): 
    sorted_len = [len(a),len(b)]
    sorted_len.sort()

    numbers = (number(a),number(b))
    num_max =max(numbers)
    num_min =min(numbers)
    return (num_min,sorted_len[0]),(num_max,sorted_len[1])

def number_type (num):
    if "." in num:
        return FLOAT_TYPE
    else:
        return INT_TYPE
    
def number(num):
    if(number_type(num) == INT_TYPE):
        return int(num)
    else:
        return float(num)