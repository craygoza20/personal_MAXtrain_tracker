import requests
from pprint import pprint
from app_id import app_id

alerts_url = 'https://developer.trimet.org/ws/v2/alerts'
vehicles_url = 'https://developer.trimet.org/ws/v2/vehicles'
arrivals_url = 'https://developer.trimet.org/ws/v2/arrivals'
route_config_url = 'https://developer.trimet.org/ws/V1/routeConfig'
stop_location_url = 'https://developer.trimet.org/ws/V1/stops'
trip_planner_url = 'https://developer.trimet.org/ws/V1/trips/tripplanner'
payload = {'appID':app_id, 'json':'true'}

def get_alerts(payload):
    r = requests.get(alerts_url,params=payload)
    r = dict(r.json())
    return r

def get_vehicles(payload):
    r = requests.get(vehicles_url,params=payload)
    r = dict(r.json())
    return r

def get_arrivals(payload):
    r = requests.get(arrivals_url,params=payload)
    r = dict(r.json())
    return r

def get_route_config(payload):
    r = requests.get(route_config_url,params=payload)
    r = dict(r.json())
    return r

def get_stop_location(payload):
    r = requests.get(stop_location_url,params=payload)
    r = dict(r.json())
    return r


alerts = get_alerts(payload)
vehicles = get_vehicles(payload)
