def my_generator(val):
    for i in range(val):
        yield i + 1


my_range = my_generator(3)
for i in my_range:
    print(i) # 1 2 3
    
