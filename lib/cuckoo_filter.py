import utils

class MyCuckooFilter:
    def __init__(self, size):
        self.arr_size = 2 ** size - 1
        self.size=size
        self.arr_one = [0] * self.arr_size
        self.arr_two = [0] * self.arr_size
        self.template=[]
    def insert(self, item):
        K=10
        x_value = utils.xor_dec_with_Key(item, K)
        fit = utils.fit2size(utils.convert_dec2bin((x_value)))
        x_prime = utils.convertBin2Dec(utils.left_shift(fit))
        i1 = utils.xor_dec_with_Key(utils.convertBin2Dec(utils.left_shift(fit)), K)
        self.insert_arr_one(i1,x_prime)
        # print("i1", i1)
        # i2 = xor_dec_with_Key(i1, my_hash(self.size, x_prime))
        # print("i2", i2)

    def insert_arr_one(self, index,x_prime):
        if self.arr_one[index] != 1:
            self.arr_one.insert(index, 1)
        else:
            print ("i1 inedx = ", index)
            x_prime = x_prime + 1
            # print ("i1 occupied need to implement fix")
            i2 = utils.xor_dec_with_Key(index, utils.my_hash(self.size, x_prime))
            print("i2 inedx = ", i2)
            self.insert_arr_tow(i2,x_prime)

    def insert_arr_tow(self, index,x_prime):
        if self.arr_two[index] !=1:
            self.arr_two.insert(index, 1)
        else:
            print("i2 inedx = ", index)
            x_prime=x_prime+1
            i1=utils.xor_dec_with_Key(index,utils.my_hash(self.size,x_prime))
            self.insert_arr_one(i1,x_prime)
            print("i1 inedx = ", i1)

    def get_arr_one(self):
        return self.arr_one
    def get_arr_two(self):
        return self.arr_two

    def gen_template(self):
        for i in range (self.arr_size):
            self.template.append(utils.xor_bin(self.arr_one[i],self.arr_two[i]))






cuckoo = MyCuckooFilter(8)
cuckoo.insert(5)
cuckoo.insert(5)
cuckoo.insert(5)
cuckoo.insert(5)
cuckoo.insert(5)
cuckoo.insert(5)
#print(cuckoo.get_arr_one())


#print ("-----------------------------------------------------------------------------")
#print(cuckoo.get_arr_two())
cuckoo.gen_template()
print (cuckoo.template)



