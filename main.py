from utils import *

a = "289" 
b = "3456"

def set_sum_position(a,b):
    (min_num,len_min),(max_num,len_max) = sort_numbers_size(a,b)

    size = len_max +2
    fst_line = ('{{0:>{}}}'.format(size))
    snd_line = ('+{{0:>{}}}'.format(size-1))
    print(fst_line.format(max_num))
    print(snd_line.format(min_num))
    
    for i in range(size):
        print('-', end = '')

set_sum_position(a,b)

