#!/usr/bin/python3
# -*-coding:iso-8859-15-*-
# -*- coding: utf-8 -*-
# -*- coding: 850 -*-
# -*- coding: cp1252 -*-
from pymongo import MongoClient
from Backend.functions.seed_data import load_initial_data
import sys
dbconn = None

# MongoDB
# Server
strConnection = "mongodb://localhost:27017"
strDBConnection = "SkillsMS"


# Import MongoClient from pymongo and create a connection to the database
# This helps to avoid circular imports and ensures that the database connection is established only once.
client = MongoClient(strConnection)
dbconn = client[strDBConnection]

# Function to load initial data into the database
load_initial_data()