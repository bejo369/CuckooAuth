SIZE = 6
SHIFT = 4
def convertBin2Dec (bin_str):
    dec_num=0
    for i in bin_str :
        dec_num = dec_num * 2 + int (i)
    return dec_num
def xor_dec_with_Key (dec_num , key):
    """
    This method return xor values of 2 given decimals
    :param dec_num: given decimal num1
    :param key:
    :return: xor value (int)
    """
    xor_value = dec_num ^ key
    return xor_value

def convert_dec2bin (dec_num):
    bin_str = ""
    while dec_num > 0 :
        bin_str = str(dec_num % 2 )+ bin_str
        dec_num = dec_num // 2
    return bin_str


def fit2size (bin_str, size=SIZE):
    bin_str_size = len(bin_str)
    if size > bin_str_size:
        diff = size - bin_str_size
        prefix = "0" * diff
    return prefix + bin_str



def left_shift(bin_str, shift_value=SHIFT):
    bin_str_arry=[]
    for i in bin_str :
        bin_str_arry.append (i)
    for i in range (shift_value):
        _=bin_str_arry.pop(0)
        bin_str_arry.append("0")
    return "".join (bin_str_arry)

def my_hash(column_size, x_prime):
    """
        Hash (x ̃) = count x ̃ as ASCII code and convert to decimal value then do summation of all numbers mod 2mbit-1
        ASCII  Decimal
         48   52 56
       = 52+56
       = 108 mod 2^8-1
       = 108 mod 128
       = 108

        :return:
    """
    sum_value = 0
    arr_size = 2 ** column_size - 1
    for i in str(x_prime):
        sum_value += ord(i)
    return sum_value % arr_size

def xor_bin (value1,value2):
    return value1^value2

