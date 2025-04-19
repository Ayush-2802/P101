from concurrent.futures import ThreadPoolExecutor
import time

def print_num(x):
    time.sleep(1)
    return f"Number : {x}"
 
number = [1,2,3,4,5,6,7,8,9,10]

with ThreadPoolExecutor(max_workers=3) as executor:
    res = executor.map(print_num,number)

for result in res:
    print(result)