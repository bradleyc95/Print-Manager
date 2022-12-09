# Bradley Cox, 10/12/2022
# PrintManager

# define a queue
class Queue:
    def __init__(self):
        self.items = []
    
    # checks to see if queue is empty, returns bool
    def isEmpty(self):
        return len(self.items) == 0
    
    # add an item to the queue
    def enqueue(self, item):
        self.items.insert(0, item)
    
    # remove an item from  the queue
    def dequeue(self):
        return self.items.pop()
    
    # return the size of the queue
    def size(self):
        return len(self.items)

# enqueue an item to be printed
def queuePrintJob(queue, document):
    queue.enqueue(document)

# run through the queue, printing each item and then dequeue them
def run(queue):
    while queue.isEmpty() == False:
        print(queue.dequeue())



q = Queue()

queuePrintJob(q, "First Document")
queuePrintJob(q, "Second Document")
queuePrintJob(q, "Third Document")

run(q)