import threading

class Pipeline:
    """
        Class to allow a single element pipeline between and consumer
    """
    def __init__(self):
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()
    
    def get_message(name):
        logging.info('%s: is about to get an lock', name)
        
        self.consumer_lock.acquire()
        logging.debug('%s: have a lock', name)
        
        message = self.message
        logging.debug('%s: about to release setlock', name)
        
        self.producer_lock.release()
        logging.debug("%s: setlock released", name)
        
        return message
    
    def set_message(self, message, name):
        logging.debug("%s:about to acquire setlock", name)
         
        self.producer_lock.acquire()
        logging.debug("%s:have setlock", name)

        self.message = message
        logging.debug("%s:about to release getlock", name)
        
        self.consumer_lock.release()
        logging.debug('%s:getlock released',name)
