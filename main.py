from flask import Flask, request, render_template
import json
from server.queue import queue, enqueue, dequeue
from server.tree import tree

app = Flask(__name__)

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
  return render_template("queue.html", my_queue=queue, title=title)

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
