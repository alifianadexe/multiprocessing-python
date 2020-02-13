import random
import logging

SENTINEL = object()

def producer(pipeline):
    """pretend we're getting a message from the network"""
    for index in range(10):
        message = random.randint(1, 101)
        logging.info("Producer Get Message : %s ", message)
        pipeline.set_message(message, "Producer")

    # Send a sentinel message to tell consumer
    pipeline.set_message(SENTINEL, "Producer")
