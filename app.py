from flask import Flask
import numpy as np
import pandas as pd
import datetime

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

base = automap_base()

base.prepare(engine, reflect=True)

Measurement = base.classes.measurement
Station = base.classes.station

session = Session(engine)

app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available routes."""
    return(
        f"Available Routes:<br/>"

        f"/api/v1.0/precipitation<br/>"

        f"/api/v1.0/stations<br/>"

        f"/api/v1.0/tobs<br/>"

        f"/api/v1.0/<start><br/>"

        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the JSON representation of your dictionary"""
    precip_12months = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date > '2016-08-23').\
    order_by(Measurement.date).all()


@app.route("/api/v1.0/stations")
def stations():
    """Return a JSON list of stations """
    results = session.query(Station.name).all()

@app.route("/api/v1.0/tobs")
def temperature():
    """Return a JSON list of temperature observations (TOBS) for that year."""
    station_query2 = "SELECT date, tobs FROM measurement WHERE station = 'USC00519281' AND date > '2016-08-23'"

@app.route("/api/v1.0/<start>")
def start(start):
    """Return a JSONified dictionary of min, max, and avg temperatures."""


@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    """Return a JSONified dictionary of min, max, and avg temperatures."""