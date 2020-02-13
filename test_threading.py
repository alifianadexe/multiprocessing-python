import logging
import threading
import time
import concurrent.futures

class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self, name):
        logging.info("Thread %s: starting update", name)
        logging.info("Thread %s: hold the lock", name)
        
        with self._lock:
            logging.debug("Thread %s has been Lock", name)
            local_copy = self.value
            local_copy += 1
            time.sleep(1)
            self.value = local_copy
            logging.debug("Thread %s about release lock", name)
        
        logging.debug("Thread %s after release", name)
        logging.info("Thread %s: finishing update", name)


def thread_function(name):
    logging.info("Thread %s : starting", name)
    time.sleep(2)
    logging.info("Thread %s : finished", name)

if __name__ == "__main__":
    format = "%(asctime)s - %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.getLogger().setLevel(logging.DEBUG)
    
    database = FakeDatabase()
    logging.info("Testing Update. Starting value is %d. ", database.value)
    
    # MultiThreading with ThreadPoolExecutor
    
    # with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    #     for index in range(2):
    #         executor.submit(database.update, index)
    
    

    # MultiThreading Conventional
    
    threads = list()
    for index in range(2):
        logging.info("Main : before creating thread %d ", index)
        x = threading.Thread(target=database.update, args=(index,))
        threads.append(x)
        x.start()
    
    for index, thread in enumerate(threads):
        logging.info("Main : before joining thread %d ", index)
        thread.join()
        logging.info("Main : thread %d done", index)

    logging.info("Testing update. Ending value is %d.", database.value)
    logging.info("Main : All Done")
