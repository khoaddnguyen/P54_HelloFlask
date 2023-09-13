from flask import Flask

app = Flask(__name__)

print(__name__)

@app.route("/")  # Python Decorator
def hello_world():
    return ("<h1 style='text-align: center'>Hello, World!</h1>"
            "<p>This is a paragraph.</p>"
            "<img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTV7IwlGEQkFsd_NT-s6ySpDTVcnmzDYlhqG1GrqCcEAISWitfyn7wjRj-oR0ESU4pVW6w&usqp=CAU'>"
            "</br>"
            "<img src='https://media3.giphy.com/media/XtydbjSSwkC7K2zBTH/giphy.gif?cid=ecf05e478bo0w6jbwr87h10ie4puy0yi1t4mzwh5247qxvyo&ep=v1_gifs_gifId&rid=giphy.gif&ct=g' width=300>")

def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return "<em>" + function() + "</em>"
    return wrapper_function

def make_underline(function):
    def wrapper_function():
        return "<u>" + function() + "</u>"
    return wrapper_function


@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
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