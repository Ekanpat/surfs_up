#Set Up the Database and Flask

from flask import Flask 
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Set Up the Database
engine = create_engine("sqlite:///hawaii.sqlite")
#reflect the database into our classes
Base = automap_base()
#code to reflect the database
Base.prepare(engine, reflect=True)
#create a variable for each of the classes
Measurement = Base.classes.measurement
Station = Base.classes.station
#create a session link from Python to our database
session = Session(engine)

#Set Up Flask
app = Flask(__name__)

# #Create the Welcome Route
@app.route("/")

# 1. Define the welcome route 
# # #create a function welcome() with a return statement
def welcome(): 
    return(             # # add the precipitation, stations, tobs, and temp routes
    '''                     
    Welcome to the Climate Analysis API! 
    Available Routes:
    /api/v1.0/precipitation
    # /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# 2. Precipitation Route
@app.route("/api/v1.0/precipitation")

# # create the precipitation function
# ## add the line of code that calculates the date one year ago from the most recent date in the database
# ### write a query to get the date and precipitation for the previous year.
# #### use jsonify() to format our results into a JSON structured file
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

# 3. Stations Route
## defining the route and route name
@app.route("/api/v1.0/stations")
# create a new function called stations()
### create a query that will allow us to get all of the stations in our database
###se thefunction np.ravel(), with results as our parameter
##convert our unraveled results into a list (use the list function, which is list(), 
# and then convert that array into a list)
# Lastly, jsonify the list and return it as JSON. The final code below:
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# 5. Monthly temperature route

# Monthly Temperature Route
# The goal is to return the temperature observations for the previous year
# define the code
@app.route("/api/v1.0/tobs")

# create a function called temp_monthly()
## calculate the date one year ago from the last date in the database
###query the primary station for all the temperature observations from the previous year
#### , unravel the results into a one-dimensional array and convert that array into a list
#### jsonify the list and return our results
#### Add the return statement to the end of the code

def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
# 5. Statistics Route(report on the minimum, average, and maximum temperatures)

# start by providing both a starting and ending date
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

#create a function called stats()
# add parameters to our stats()function: a start parameter and an end parameter. set them bot to None
##create a query to select the min, avg, and max temps from SQLite db;
### by creating a list called 'sel'
###dd an 'if-not' statement to our code
### Take note of the asterix which indicate there will be multiple results for our query
### use the sel list, which is simply the data points we need to collect.
### final code below

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)


# run our code



