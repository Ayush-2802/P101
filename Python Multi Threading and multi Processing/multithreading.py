import threading
import time

def print_num():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")

def print_letter():
    for i in "abcde":
        time.sleep(2)
        print(f"Letter:{i}")

# creating threads

t1 = threading.Thread(target=print_num)
t2 = threading.Thread(target=print_letter)



t=time.time()
# print_num()
# print_letter()

# starting the threads
t1.start()
t2.start()

# wait for threads to complete
t1.join()
t2.join()

ft = time.time()-t
print(ft)

