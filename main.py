from flask import Flask

app = Flask("bhapi")

@app.route('/')
def hello_world():
    return 'Hello, World!'
