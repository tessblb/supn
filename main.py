from flask import Flask, request, render_template
import json, time

app = Flask(__name__)

my_queue = ["A", "B", "C"]

@app.route('/', methods=['GET'])
def index():
  return render_template("index.html", my_queue=my_queue)

@app.route('/enqueue', methods=['GET'])
def enqueue():
  item = request.args.get('item')
  if item:
    my_queue.append(item)
  return json.dumps(my_queue)


@app.route('/dequeue', methods=['GET'])
def dequeue():
  print("dequeue...")
  if my_queue != []:
    my_queue.pop(0)
  return json.dumps(my_queue)

if __name__ == '__main__':
  app.config['TEMPLATES_AUTO_RELOAD'] = True
  app.run(debug=True, port=8000)
