def convertBin2Dec (bin_str):
    dec_num=0
    for i in bin_str :
        dec_num = dec_num * 2 + int (i)
    return dec_num
def xor_dec_with_Key (dec_num , key):
    X_prime=dec_num ^ key
    return X_prime
def convert_dec2bin (dec_num):
    bin_str = ""
    while dec_num > 0 :
        bin_str = str(dec_num % 2 )+ bin_str
        dec_num = dec_num // 2
    return bin_str


def fit2size (bin_str, size):
    bin_str_size = len(bin_str)
    if size > bin_str_size:
        diff = size - bin_str_size
        prefix = "0" * diff
    return prefix + bin_str



def left_shift(bin_str, shift_value):
    shifted_value=[]
    bin_str_arry=[]
    for i in bin_str :
        bin_str_arry.append (i)
    for i in range (shift_value):
        _=bin_str_arry.pop(0)
        bin_str_arry.append("0")
    return "".join (bin_str_arry)

