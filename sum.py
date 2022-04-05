from utils import *

a = "289" 
b = "3456"

def print_sum_position(a,b, carry_line, result_line):
    (min_num,len_min),(max_num,len_max) = sort_numbers_size(a,b)

    size = len_max +2
    
    fst_line = ('{{0:>{}}}'.format(size))
    snd_line = ('+{{0:>{}}}'.format(size-1))

    print(fst_line.format(carry_line))
    
    print(fst_line.format(max_num))
    print(snd_line.format(min_num))

    print('-' * size)
    
    print(fst_line.format(result_line))
    
def sum_one(a,b, index, carry_in):
    num_a = "0"
    num_b = "0"
    
    index_a = len(a) - index
    index_b = len(b) - index
    
    if index_a >= 0:
        num_a = a[index_a]

    if index_b >= 0:
        num_b = b[index_b]
    
    result = number(num_a) + number(num_b)
    
    if bool(carry_in.strip()) :
        result += number(carry_in)
    
    result_str = str(result)
    carry_out = ""
    
    if len(result_str)>1:
        carry_out = result_str[0]
        result_str = result_str[1]

    
    return (result_str, carry_out)    
    



def main():
    
    num_max_len = len_max(a,b)

    carry_arr = [" "] * num_max_len
    result_arr = [""] * num_max_len

    carry = "".join(carry_arr)
    result = "".join(result_arr)


    index = 1
    while(index <= num_max_len+1):
        
        print_sum_position(a,b, carry, result)

        result_arr[num_max_len-index], carry_arr[num_max_len-index-1]= sum_one(a,b,index,carry_arr[num_max_len-index])
        carry = "".join(carry_arr)
        result = "".join(result_arr)
        
        index +=1
        
        print("\n")

if __name__ == "__main__":
    main()