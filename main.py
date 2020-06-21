from flask import Flask, render_template, request, redirect, jsonify, \
    url_for, flash

# from sqlalchemy import create_engine, asc, desc, \
#     func, distinct
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.serializer import loads, dumps


# from database_setup import Base, Things

import random
import string
import logging
import json
import httplib2
import requests


app = Flask(__name__)



# Display all things
@app.route('/')
def showMain():
    things = ["thing1", "thing2", "cat-in-the-hat"]

    return render_template('things.html', things=things)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
