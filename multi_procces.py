from multiprocessing import Process, Value, Array, Lock, Queue
import time

def add_100(numbers, lock):
    for i in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            with lock:
                numbers[i] += 1

def square(numbers, queue):
    for i in numbers:
        queue.put(i*i)

def make_negative(numbers, queue):
    for i in numbers:
        queue.put(-1*i)
if __name__=="__main__":
    lock = Lock()

    shared_number = Value("i", 0)
    shared_array = Array("d", [0.0, 100.0, 200.0])
    print("Array at beggining is", shared_array[:])

    p1 = Process(target=add_100, args=(shared_array, lock))
    p2 = Process(target=add_100, args=(shared_array, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Array at end is", shared_array[:])
    time.sleep(3)

    numbers = range(1, 6)
    q = Queue()

    p3 = Process(target=square, args=(numbers, q))
    p4 = Process(target=make_negative, args=(numbers, q))

    p3.start()
    p4.start()

    p3.join()
    p4.join()

    while not q.empty():
        print(q.get())