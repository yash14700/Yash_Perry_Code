from flask import Flask
from flask import *
import json
import wikipedia

#Set up
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def return_intro():
    get = request.args
    #Error: What if 'query' not in get request
    word = get['query']
    pages = wikipedia.search(word)
    #Error: What ig pages is empty
    page = pages[0]
    data = wikipedia.page(page)
    return jsonify(data.summary)

#Run
if __name__ == "__main__":
    app.debug = False
    app.run()
