import sys
sys.path.append('../')
import warnings
warnings.filterwarnings('ignore')

import src.custom_notCritical as cnc
from icecream import ic
ic.configureOutput(prefix='icecream debug @ ')


# Dataframes, Series & Data Wrangling
import pandas as pd
import numpy as np
from datetime import datetime
import math

# APIs / CURL
import pycurl
import certifi

# Local / Data Access
import opendatasets as od
import glob
import os
import csv
from io import BytesIO
import json

# Databases
from influxdb_client import InfluxDBClient, Point, WritePrecision, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS
import pyodbc 
import pymysql
from sqlalchemy import create_engine

# EDA / DataViz
from tqdm import tqdm
import sweetviz as sv
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

print('Your favorite libraries have been loaded.')

# Pandas options
pd.set_option('max_columns', None)
pd.set_option('max_seq_item', None)

# pd.set_option(“max_colwidth”, None)
