from flask import Flask, render_template
from data import items


app = Flask(__name__)


data_items = items()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/items')
def items():
    return render_template('items.html', items=data_items)

@app.route('/item/<string:id>/')
def item(id):
    return render_template('item.html', id=id)

if __name__ == "__main__":
    app.run(debug=True)
