import threading
import random
import logging

from pipeline import Pipeline


SENTINEL = object()

def producer(pipeline):
    """pretend we're getting a message from the network"""
    for index in range(10):
        message = random.randint(1, 101)
        logging.info("Producer Get Message : %s ", message)
        pipeline.set_message(message, "Producer")

    # Send a sentinel message to tell consumer
    pipeline.set_message(SENTINEL, "Producer")

def consumer(pipeline):
    """Pretend we are saving number in database"""
    message = 0
    while message is not SENTINEL:
        message = pipeline.get_message("Consumer")
        if message is not SENTINEL:
            logging.info("Consumer storting message: %s ", message)

if __name__ == "__main__":
    format = "%(asctime)s - %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    pipeline = Pipeline()
    
    exec_producer = threading.Thread(target=producer, args=(pipeline,))
    exec_consumer = threading.Thread(target=consumer, args=(pipeline,))    
    executor.start()
    executor.start()
    
    executor.join()
    
    
    
