from __future__ import print_function
from flask import Flask, render_template, make_response
from flask import redirect, request, jsonify, url_for
from flask import Flask, render_template, request
import sys
#from wtforms import Form, FloatField, validators, StringField, ValidationError

#import pymysql

import io
import os
import uuid
#from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
#from matplotlib.figure import Figure
#import numpy as np

app = Flask(__name__)


@app.route('/')
def index():
    title = 'Coming Soon'
    return render_template('layouts/index.html',
                           title=title)

@app.route('/upcomingevents', methods=['GET'])
def upcomingevents():
    title = 'News and such'
    return render_template('layouts/upcomingevents.html',
                           title=title)

@app.route('/phases', methods=['GET'])
def phases():
    title = 'Game Phases'
    return render_template('layouts/phases.html',
                           title=title)


if __name__ == '__main__':
    app.run()
