from fastapi import APIRouter
from pydantic import BaseModel
from db.connection import con
import datetime

router = APIRouter()

class ReadingRequest(BaseModel):
    temperature: float
    device_id: int

class Reading(ReadingRequest):
    created_at: str


class ListReadingsResponse(BaseModel):
    data: list[Reading]

@router.post("/readings")
def create_reading(reading: ReadingRequest):
    connection = con()
    connection.execute('''
        INSERT INTO readings ('device_id', 'temperature', 'created_at')
        VALUES (?, ?, ?)
        ''', (reading.device_id, reading.temperature, datetime.datetime.now().replace(microsecond=0).isoformat())
    )
    connection.commit()
    return None

@router.get("/readings")
def fetch_readings():
    connection = con()
    response = {}
    for row in connection.execute("SELECT id, name from devices"):
        query = '''
            SELECT temperature, created_at
            FROM readings
            WHERE device_id = {}
        '''.format(row['id'])

        response[row['name']] = connection.execute(query).fetchall()

    return {"data": response}



@router.get("/readings_plotly")
def fetch_readings():
    connection = con()
    response = {}
    for row in connection.execute("SELECT id, name from devices"):
        query = '''
            SELECT temperature, created_at
            FROM readings
            WHERE device_id = {}
        '''.format(row['id'])

        response[row['name']] = connection.execute(query).fetchall()

    # transform data to be easily graphed by plotly
    # var trace1 = {
    #   x: [1, 2, 3, 4],
    #   y: [10, 15, 13, 17],
    #   mode: 'lines',
    #   name: 'device 1'
    # };
    #
    # var trace2 = {
    #   x: [1, 2, 3, 4],
    #   y: [16, 5, 11, 9],
    #   mode: 'lines',
    #   name: 'device 2'
    # };
    #
    # var data = [trace1, trace2];

    return_response = []
    for name, data in response.items():
        trace = {
            "name": name,
            "mode": 'scatter',
            "x": [el['created_at'] for el in data],
            "y": [el['temperature'] for el in data]
        }
        return_response.append(trace)

    return {"data": return_response}
