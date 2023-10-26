"""
here we are looking for the principle of threads in python
"""

# Imports
import threading
import concurrent.futures as cf
from utils import mean_timer, timer
from time import sleep
import random


# classes

class CustomThread(threading.Thread):
    def __init__(self, target_function, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_function = target_function
        # self.value can be access doing this.value

    def run(self):
        self.target_function()


# Functions

def task():
    thread = threading.current_thread()
    sleep(1)
    print(f"We have processed the task in the thread {thread.name}({thread.ident},{thread.daemon})")

def list_threads():
    print("listing threads")
    for thread in threading.enumerate():
        print(f"thread {thread.name}({thread.ident},{thread.daemon})")
    print("end listing threads")

def local_task():
    thread_local = threading.local()
    thread_local.value = random.randint(0, 100)
    print(f"thread {threading.current_thread().name} has value {thread_local.value}")

def first_test(task):
    first_thread = threading.Thread(target=task, name="first_thread")
    first_thread.start()
    thread = threading.Thread(target=list_threads)
    first_thread.join()  # wait for the thread to finish, if this line is before the other start, the enumeration will not show the first_thread
    thread.start()
    thread.join()
    main_thread = threading.main_thread()
    print(f"back in the main thread {main_thread.name}({main_thread.ident},{main_thread.daemon})")

def lock_task(lock):
    with lock:
        print(f"thread {threading.current_thread().name} has the lock")
        sleep(1)
        

def rlock_task(rlock):
    with rlock:
        print(f"thread {threading.current_thread().name} has the lock")
        lock_task(rlock)

def second_test():
    lock = threading.RLock() # if it's a lock, the thread will be blocked, if it's a rlock, the thread will not be blocked
    thread = threading.Thread(target=rlock_task, args=(lock,), name="lock_thread")
    thread.start()
    thread.join()

@mean_timer()
def countdown(n):
    while n>0:
        n -= 1

@mean_timer()
def countdown_with_thread(n):
    t1 = threading.Thread(target=countdown, args=(n//2,))
    t2 = threading.Thread(target=countdown, args=(n//2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

@mean_timer(1)
def sleep_with_thread(n):
    t1 = threading.Thread(target=sleep, args=(n,))
    t2 = threading.Thread(target=sleep, args=(n,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


def name(name):
    print(f"thread {name} has started")
    sleep(2)
    print(f"thread {name} has finished")
    
def concurrent_future():
    with cf.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(name, range(3))


def create_list(n):
    res = []
    for i in range(n):
        res.append(i)
    return res
@mean_timer(1)
def run2(nb):
    with cf.ThreadPoolExecutor(max_workers=2) as executor:
        for res in executor.map(create_list, [nb, nb+1]):
            pass

def task_sleep():
    sleep(1)

@mean_timer(1)
def task_sleep_cf():
    with cf.ThreadPoolExecutor(max_workers=2) as executor:
        for res in executor.map(task_sleep):
            pass

def main():
    #first_test(task=task)
    #second_test()
    # countdown(500000)
    # countdown_with_thread(500000)
    # sleep_with_thread(1)
    #concurrent_future()
    #create_list(100000)
    #run2(100000)
    task_sleep_cf()
    #task_sleep()
    pass




# Main
if __name__ == "__main__":
    main()