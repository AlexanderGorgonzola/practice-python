from threading import Thread, Lock
from queue import Queue
import time
database_value = 0

def increase(lock):
    global database_value

    lock.acquire()
    """I can also use with lock and get rid of lock.release"""
    local_copy = database_value
    local_copy += 1
    time.sleep(0.1)

    database_value = local_copy
    lock.release()

if __name__ == "__main__":
    lock = Lock()
    print("start value", database_value)

    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    """OHHHHH, I DID SOMETHING WRONG"""
    print("end value", database_value)

    print("End Main")




"""New stuff"""

if __name__=="__main__":

    q = Queue()
    q.put(1)
    q.put(2)
    q.put(3)

    first = q.get()
    print(first)
    
    q.task_done()
    q.join()

    """q.empty checks if its empty"""
    print("end main")