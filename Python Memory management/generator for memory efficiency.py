# generators allow you to porduce one item at a time, using memory efficiency by only keeping one item in memory at a time

def gen_num(n):
    for i in range (n):
        yield i


for num in gen_num(100000):
    print(num)
    if num > 10:
        break