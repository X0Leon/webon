# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask_nav.elements import *
from flask_nav import Nav

import json
import pandas as pd
import pygal

nav = Nav()

nav.register_element('top', Navbar(
    View('Home.', 'index'),
    View('Table', 'table'),
    View('Graph', 'graph'),
    ))


df = pd.read_csv('d:/thinkquant/Data/2016-2016/A.csv', header=0, index_col=0, parse_dates=True)
df['datetime'] = df.index
data = df.iloc[:100].to_dict('records')


app = Flask(__name__)

@app.route('/')
def index():
    """ render svg graph """
    return 'Hello! Go to /table/ or /graph/.'

@app.route('/table/')
def table():
    return render_template("table.html", data=data)

@app.route('/graph/')
def graph():
    """ render svg on html """
    bar_chart = pygal.Bar()
    bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
    bar_chart = bar_chart.render_data_uri()
    return render_template('graph.html', title='Hello Graph', chart=bar_chart)

nav.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)