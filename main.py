#main.py

# Import the Flask module that has been installed.
from flask import Flask, jsonify, request
from newspaper import Article;

# Createing a "books" JSON / dict to emulate data coming from a database.
books = [
    {
        "id": 1,
        "title": "Harry Potter and the Goblet of Fire",
        "author": "J.K. Rowling",
        "isbn": "1512379298"
    },
    {
        "id": 2,
        "title": "Lord of the Flies",
        "author": "William Golding",
        "isbn": "0399501487"
    }
]

# Creating a new "app" by using the Flask constructor. Passes __name__ as a parameter.
app = Flask(__name__)

# Annotation that allows the function to be hit at the specific URL.
@app.route("/")
# Generic Python function that returns "Hello world!"
def index():
    return "Enter the params!"

# Annotation that allows the function to be hit at the specific URL with a parameter. Indicates a GET HTTP method.
@app.route("/extract-content/", methods=["GET"])
# This function requires a parameter from the URL.
def get_content():
    url = request.args.get('url')
    item = request.args.get('item')
    result = {}
    article = Article(url)
    article.download()
    article.parse()
    if(item=='title'):
        result=article.title
    if(item=='content'):
        result=article.text
    return result
    
# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
    # Runs the Flask application only if the main.py file is being run.
    app.run()