from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from config import Config
import time
import threading
from dbclasses import NetworkData, Login, query, source_func, des_func, smell, test_test, user_login_username

# Run "pip install -r requirements.txt" to ensure libraries are installed for virtual environment to initalize.

## As long as static and templates folders that hold CSS and HTML have the name static and templates Flask knows where to find it by default
    # If you change the name of the folders it must be pointed to in the app variable config via static_folder= folder_name

### Design = app.py configs Flask app, config.py outline db directory path via config class, dbclasses.py outlines classes and contains all called functions from app.py
        ## Function = Application connects to database allowing user authentication to a frontend of the Scapy library to sniff packets between two IP address.
         # The sniffed packets will be collected and written to a database.

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

Session = sessionmaker(app)
session = Session()

# root login page
@app.route("/", methods=['GET', 'POST'])
def login():
    print(request.data)
    if request.method == 'POST':
        if request.content_type == 'application/json':

            input = request.json.get('username')
            login_validation = user_login_username(input)
            print(f'Login_Validation {login_validation}')

            # use 1 in username as test
            if login_validation == 'True':
                return jsonify({'message': 'a'})
            else:
                result = 'Invalid Login'
                return jsonify({'message': result})
    else:
        return render_template('login.html') 

# Page to go to after successful login. Where the Scapy frontend is located.
@app.route("/query", methods=['GET', 'POST'])
def index():
    print(request.data)
    if request.method == 'POST':
        if request.content_type == 'application/json':        

            # Retrieve the input data from the AJAX request
            input_data = request.json.get('source_input')
            print("input data ---", input_data)
            processed_result = source_func(input_data)

            # Return a response to the frontend
            debug = jsonify({'message': processed_result})
            print("debug", debug)
            return jsonify({'message': processed_result})
        else:
            # Return an error response if the content type is not JSON
            return jsonify({'error': 'Unsupported Media Type'}), 415
    else:
        # For GET requests, return the HTML template
        return render_template('content.html')

if __name__ == '__main__':
    
    app.run(debug=True)
