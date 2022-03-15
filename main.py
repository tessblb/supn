from flask import Flask, request, render_template
import json
from server.queue import queue, enqueue, dequeue

app = Flask(__name__)

title="Antonio's Linear Data Structure"

@app.route('/', methods=['GET'])
def index():
  return render_template("index.html", my_queue=queue, title=title)

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
