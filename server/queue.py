queue = ['A', 'B', 'C']

def enqueue(item):
  if item:
    queue.append(item)
  return queue

def dequeue():
  if queue != []:
    queue.pop(0)
  return queue
