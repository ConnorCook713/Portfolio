from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from scapy.all import sniff, Ether, IP
from config import Config
import time
import threading
from dbclasses import NetworkData, query, source_func, des_func, smell, test_test

# in .venv virtual enviroment bc bottom left of python file allows you to select
# what environment you run your code in. Such as in this case a container that
# loads all libraries into a virtual environment then runs code in it

# from Holder.dbclasses import NetworkData


#### WARNING: Wireshark is installed, but cannot read manuf ! = Appears because of the import of the scapy.all module
## As long as static and templates folders that hold CSS and HTML have the name static and templates Flask knows where to find it by default
    # If you change the name of the folders it must be pointed to in the app variable config via static_folder= folder_name

### Design = app.py configs Flask app, config.py outline db directory path via config class, Network_moniotr.py will be a background process called from app.py and writing to 
    # scapy.db (change name to networkdata.db and call db class networkdata)

# __name__ = Flask special app that when python file the variable is in is run directly it is changed to __main__
app = Flask(__name__)

# Calls Flask app as app variable. Config script is called within the Flask app and the from_object function uses the Config class as an argument
app.config.from_object(Config)

# SQLAlchemy db instance is started in the Flask app
db = SQLAlchemy(app)

# initalize Flask app with SQLAlchemy db
# db.init_app(app) not needed ig

with app.app_context():
    db.create_all()
        # all function that involve writing things to a db via session must be placed indended under app.app_context()

# def network_function():
    # thread = threading.Thread(target=dbclasses)
    # thread.start()
# init SQLAlchemy db edit session with the Flask app

Session = sessionmaker(app)
session = Session()
thread = threading.Thread(target=smell)
print("running thread")
thread.daemon = True
thread.start()
print('starting thread')

@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        # Gets input from server_input. request.form.get variable must match ID and name of input field in HTML
        source_input = request.form.get('source_request')
        des_input = request.form.get('des_request')
        print('Source Input:', source_input)
        print('Des Input:', des_input)
# logic: have user input be what is queried from db. Use tuser input as an agrument to query for info.
# have function contained with app.py. Have error exception for when argument submitted to function
# is an invalid way to query the db.
        if source_input != '':
            source_output = source_func(source_input)
            return render_template("content.html", src_output_html=source_output)
        if des_input != '':
            des_output = des_func(des_input)
            return render_template("content.html", des_output_html=des_output)
        # database_input = request.form.get('database_input')
            # run function that takes user input and pass to function outside current function
                # use test_query to intake server_input input from website
                # import test_query pass server_input as argument for query
                    # if query is empty return None or return contents of query
            # query db and sift for user request
            # have return value be equal to server_input
            # source_input = 'Working'
        # source_output = query()
        print("Input Not Present in DB")
        #NetworkData.query.all()
        # Notes on this are in other Python Project
        #return render_template("content.html", CMD_result=CMD_result_app)

        # db_output point to where variable should be printed on the html page
        
    return render_template("content.html")

if __name__ == '__main__':
    
    app.run(debug=True)
    #dbclasses.query()
