from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

session = Session(bind=engine)
Measurement = Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)

@app.route("/api/v1.0/")
def home():
    return(
        f"Available  Routes:</br>"
        f"/api/v1.0/precipitation: Query for the dates and temperature observations from the last year.<br/>"
        f"/api/v1.0/stations: Return a json list of stations from the dataset.<br/>"
        f"/api/v1.0/tobs: Return a list of Temperature Observations for the previous year<br/>"
        f"/api/v1.0/start and /api/v1.0/start/end: Return a list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.<br/>"
        )

@app.route("/api/v1.0/precipitation")
def precipitation():
    last12m_data = session.query(Measurement).filter(Measurement.date >= '2016-08-23')
    prcp_results = []
    for rows in last12m_data:
        prcp_results_dict = {}
        prcp_results_dict['date'] = rows.date
        prcp_results_dict['prcp'] = rows.prcp
        prcp_results.append(prcp_results_dict)
    return jsonify(prcp_results)

@app.route("/api/v1.0/stations")
def stations():
    stations_data = session.query(Station).all()
    station_results = []
    for row in stations_data:
        station_results_dict = {}
        station_results_dict['station'] = row.station
        station_results.append(station_results_dict)
    return jsonify(station_results)

@app.route("/api/v1.0/tobs")
def tobs():
    last12m_data = session.query(Measurement).filter(Measurement.date >= '2016-08-23')
    tobs_results = []
    for row in last12m_data:
        tobs_dict = {}
        tobs_dict['station'] = row.station
        tobs_dict['tobs'] = row.tobs
        tobs_results.append(tobs_dict)
    return jsonify(tobs_results)

@app.route("/api/v1.0/<start>")
def start_query(start):
    start_q = session.query(Measurement.date, func.min(Measurement.tobs).label("Temp Min"), func.max(Measurement.tobs).label("Temp Max"),func.avg(Measurement.tobs).label("Temp Max"))\
    .filter(Measurement.date >= start).group_by(Measurement.date).all()
    start_list = []
    for row in start_q:
        test_dict = {}
        test_dict['Date'] = row.date
        test_dict['Temps (Min, Max, Average)'] = row[1:]
        start_list.append(test_dict)
    return jsonify(start_list)

@app.route("/api/v1.0/<start>/<end>")
def start_end_query(start,end):
    start_end_q = session.query(Measurement.date, func.min(Measurement.tobs).label("Temp Min"), func.max(Measurement.tobs).label("Temp Max"),func.avg(Measurement.tobs).label("Temp Max"))\
    .filter(Measurement.date >= start).filter(Measurement.date <= end).group_by(Measurement.date).all()
    start_end_list = []
    for row in start_end_q:
        test_dict = {}
        test_dict['Date'] = row.date
        test_dict['Temps (Min, Max, Average)'] = row[1:]
        start_end_list.append(test_dict)
    return jsonify(start_end_list)

if __name__ == "__main__":
    app.run(debug=True)
    raise NotImplementedError()
