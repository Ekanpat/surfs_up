from flask import Flask 

#Create a New Flask App Instance
app = Flask(__name__)
#Create Flask Routes
## define the starting point, also known as the root
@app.route('/')

#create a function called hello_world()
@app.route('/')
def hello_world():
    return 'Hello world'

#Run a Flask App

