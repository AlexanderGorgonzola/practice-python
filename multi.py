from multiprocessing import Process
from threading import Thread
import os
import time
"""Read about these packages later"""

def square_numbers():
    for i in range(100):
        """Simple stuff"""
        i * i
        time.sleep(0.1)

print("Start process")
processes = []
num_processes = os.cpu_count()

for i in range(num_processes):
    p = Process(target=square_numbers) #insert args as a tuple
    processes.append(p)

"""Start"""
for p in processes:
    p.start()

"""Join"""
for p in processes:
    p.join()

print("End process")


print("Start thread")
threads = []
num_threads = 10

for i in range(num_threads):
    t = Thread(target=square_numbers)
    threads.append(t)

"""Start"""
for t in threads:
    t.start()

"""Join"""
for t in threads:
    t.join()

print("End thread")


