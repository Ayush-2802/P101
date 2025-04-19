from concurrent.futures import ProcessPoolExecutor
import time

def sq_num(x):
    time.sleep(2)
    return f"Square:{x*x}"

number = [1,2,3,4,5,6,7,8,9,10]

if __name__=='__main__':
    with ProcessPoolExecutor(max_workers=3) as executors:
        res = executors.map(sq_num,number)

    for r in res:
        print(r)