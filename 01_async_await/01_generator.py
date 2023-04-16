class MyGenerator:
    def __init__(self, val):
        self.counter = 0
        self.max_value = val
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter == self.max_value:
            raise StopIteration
        self.counter += 1
        return self.counter


my_range = MyGenerator(10)
for i in my_range:
    print(i) # 1 ... 10
    
