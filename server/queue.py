queue = []

def enqueue(item):
  queue.append(item)
  return queue

def dequeue():
  if queue == []:
    return queue
  queue.pop(0)
  return queue

