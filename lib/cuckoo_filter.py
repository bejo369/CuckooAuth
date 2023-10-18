class MyCuckooFilter:
    def __init__(self, size):
        arr_size = 2 ** size - 1
        self.arr_one = [0] * arr_size
        self.arr_two = [0] * arr_size

    def insert_arr_one(self, index):
        self.arr_one.insert(index, 1)

    def insert_arr_tow(self, index):
        self.arr_two.insert(index, 1)

    def get_arr_one(self):
        return self.arr_one
    def get_arr_two(self):
        return self.arr_two
    def hash(self):
        pass

cuckoo = MyCuckooFilter(8)
cuckoo.insert_arr_one(58)
cuckoo.insert_arr_one(0)
print(cuckoo.get_arr_one())

