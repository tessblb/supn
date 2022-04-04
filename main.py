from flask import Flask, request, render_template
import json
from server.queue import queue, enqueue, dequeue
from server.tree import tree
from server.sort import bubbleSort, quickSort, mergeSort

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  return render_template("index.html", my_queue=queue, title="AA-1 Home Page")

@app.route('/tree', methods=['GET'])
def treeRoute():
  title="Tree Data Structure"
  return render_template("tree.html", title=title)

@app.route('/getTree', methods=['GET'])
def getTreeRoute():
  return tree

@app.route('/queue', methods=['GET'])
def queueRoute():
  title="FIFO Data Structure"

@app.route('/sort', methods=['GET'])
def sortRoute():
  return render_template("sort.html", my_queue=queue)

@app.route('/bubbleSort', methods=['GET'])
def bubbleSortRoute():
  items = request.args.get('items').split(',')
  return json.dumps(bubbleSort([int(x) for x in items]))

@app.route('/quickSort', methods=['GET'])
def quickSortRoute():
  items = request.args.get('items').split(',')
  return json.dumps(quickSort([int(x) for x in items]))

@app.route('/mergeSort', methods=['GET'])
def mergeSortRoute():
  items = request.args.get('items').split(',')
  return json.dumps(mergeSort([int(x) for x in items]))

@app.route('/enqueue', methods=['GET'])
def enqueueRoute():
  item = request.args.get('item')
  return json.dumps(enqueue(item))

@app.route('/dequeue', methods=['GET'])
def dequeueRoute():
  return json.dumps(dequeue())

if __name__ == '__main__':
  app.config['TEMPLATES_AUTO_RELOAD'] = True
  app.run(debug=True, port=8000)
