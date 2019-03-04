from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Now the python is working! :D'

if __name__ == '__main__':
  app.run()
