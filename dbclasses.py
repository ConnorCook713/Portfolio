# Find a way to put all db classes outside the main app.py script and create the dbs without cirular importing
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime
from config import Config
from scapy.all import sniff, Ether, IP
import threading
# imports .env file and load_dotenv function loads info from .env file
from dotenv import load_dotenv
load_dotenv()
import os

#engine = create_engine(Config.SQLALCHEMY_DATABASE_URI_Network)
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)


Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# db. must be removed and have network_monitor write its outputs to anther db within the Flask directory
# place decortaotr to query db then do something with output

def test_test():
    print("All running threads:")
for thread in threading.enumerate():
    print(thread.name)

class NetworkData(Base):
    __tablename__ = 'NetworkData'

    time = Column(String(250), primary_key=True, unique=False)
    source = Column(String(250), unique=False)
    destination = Column(String(250), unique=False)
    proto = Column(String(250), unique=False)
    print('Network Data Table init')

    def __init__(self, time, source, destination, proto):
        self.time = time
        self.source = source
        self.destination = destination
        self.proto = proto


class Login(Base):
    __tablename__ = 'Login'

    username = Column(String(45), primary_key=True, unique=False)
    password = Column(String(45), unique=False)
    print('Login Table init')

    def __init__(self, username, password):
        self.username = username
        self.password = password

Base.metadata.create_all(bind=engine)

# Sniffed packets are parsed and written to the database 
def packet_handler(packet):
    
    if IP in packet:
        try:
            time_ip = datetime.now()
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            proto_ip = packet[IP].proto
            entry = NetworkData(time=time_ip, source=src_ip, destination=dst_ip, proto=proto_ip)
            session.add(entry)
            session.commit()
        except IntegrityError as e:
            session.rollback()  # Rollback the transaction
        finally:
            print("IP section done")
            session.close()

    if Ether in packet:
        print("Ether running")
        try:
            time_ether = datetime.now()
            src_ether = packet[Ether].src
            dst_ether = packet[Ether].dst
            type_ether = packet[Ether].type
            entry = NetworkData(time=time_ether, source=src_ether, destination=dst_ether, proto=type_ether)
            session.add(entry)
            session.commit()
        except IntegrityError as e:
            session.rollback()  # Rollback the transaction
        finally:
            print("Ether section done")
            session.close()

# Sniffs packets between desired IPs
# count = how many packets you want to be sniffered
def smell():
    print("Sniffer is Sniffing")
    sniff(prn=packet_handler, count=10, timeout=None)
    print("Sniffing is Completed")

# Function called once Enter button is submitted on /query page
# Parsed data is returned to the frontend
def source_func(x):
    smell()
    print("Running source_func")
    source_result = session.query(NetworkData).filter_by(source=x).all()
    print("Source result -----", source_result)
    output_list = []
    for row in source_result:
        output = 'Date/Time: {}, Source: {}, Destination: {}, Protocol: {}'.format(row.time, row.source, row.destination, row.proto)
        output_list.append(output)
        print("output_list -----", output_list)
    result_string = '\n'.join(output_list)
    return result_string

def des_func(x):
    source_result = session.query(NetworkData).filter_by(destination=x).all()
    output_list = []
    for row in source_result:
        output = 'Date/Time: {}, Source: {}, Destination: {}, Protocol: {}'.format(row.time, row.source, row.destination, row.proto)
        output_list.append(output)
    result_string = '\n'.join(output_list)
    return result_string

def test_query():
    user_input = input()
    # Date/Time test data - 2024-04-10 17:03:14.573787
    # Destination test data - 52.182.143.215
    # Source test data - 10.0.22.67
    query_result = session.query(NetworkData).filter_by(destination=user_input).all()
    # print(query_result)
    output_list = []
    for row in query_result:
        output = 'Date/Time: {}, Source: {}, Destination: {}, Protocol: {}'.format(row.time, row.source, row.destination, row.proto)
        output_list.append(output)
    result_string = '\n'.join(output_list)
    print(result_string)

# Checks if inserted username is in the database. If so, True is returned.
def user_login_username(x):
    cred_query = session.query(Login).filter_by(username=x).all()
    output_list = [row.username for row in cred_query]
    print(cred_query)
    print(output_list)
    print("x value", type(x))
    print("output value", type(output_list))
    if x in output_list:
        return 'True'
    else:
        return 'False'