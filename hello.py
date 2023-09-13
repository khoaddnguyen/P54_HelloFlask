from flask import Flask

app = Flask(__name__)

print(__name__)

@app.route("/")  # Python Decorator
def hello_world():
    return "Hello, World!"

@app.route("/bye")
def say_bye():
    return "Bye"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are {number} years old!"

# call app via terminal to add to env:
#  export FLASK_APP=hello.py
#  flask run

if __name__ == "__main__":
    app.run(debug=True)