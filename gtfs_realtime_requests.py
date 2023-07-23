import requests
from pprint import pprint
from app_id import app_id
from datetime import datetime

alerts_url = 'https://developer.trimet.org/ws/v2/alerts'
vehicles_url = 'https://developer.trimet.org/ws/v2/vehicles'
arrivals_url = 'https://developer.trimet.org/ws/v2/arrivals'
route_config_url = 'https://developer.trimet.org/ws/V1/routeConfig'
stop_location_url = 'https://developer.trimet.org/ws/V1/stops'
trip_planner_url = 'https://developer.trimet.org/ws/V1/trips/tripplanner'
default_payload = {'appID':app_id, 'json':'true'}
#orenco station to hillsboro id = 9836
#to portland = 9835
stop_ids = [9835, 9836]


def get_alerts(payload:dict):
    r = requests.get(alerts_url,params=payload)
    r = dict(r.json())
    return r

def get_vehicles(payload:dict):
    r = requests.get(vehicles_url,params=payload)
    r = dict(r.json())
    return r

def get_arrivals(payload:dict):
    r = requests.get(arrivals_url,params=payload)
    r = dict(r.json())
    # times are in milliseconds since epoch, so converting them to more reasonable format
    
    for arrival in r['resultSet']['arrival']:
        try:
            converted_estimated = {'estimated':datetime.fromtimestamp(int(arrival['estimated'])/1000).strftime('%Y-%m-%d %H:%M')}
            converted_scheduled = {'scheduled':datetime.fromtimestamp(int(arrival['scheduled'])/1000).strftime('%Y-%m-%d %H:%M')}
            arrival.update(converted_scheduled)
            arrival.update(converted_estimated)
        except:
            pass
    
    return r['resultSet']['arrival']

def get_route_config(payload:dict):
    r = requests.get(route_config_url,params=payload)
    r = dict(r.json())
    return r

def get_stop_location(payload:dict):
    r = requests.get(stop_location_url,params=payload)
    r = dict(r.json())
    return r

def get_MAX_routes(route_config_json:dict) -> dict:
    MAX_LINES = {}
    for route in route_config_json['resultSet']['route']:
        if 'MAX' in route['desc']:
            MAX_LINES[route['desc']] = route
    return MAX_LINES

if __name__ == '__main__': 
    alerts = get_alerts(default_payload)

    route_config_json = get_route_config(default_payload)
    max_payload = {'routes':'190','appID':app_id, 'json':'true'}
    arrivals_payload = {'locIDs':'9836,9835','appID':app_id, 'json':'true' }
    vehicles = get_vehicles(max_payload)
    MAX_LINES = get_MAX_routes(route_config_json)
    #pprint(MAX_LINES)
    #pprint(vehicles['resultSet']['vehicle'])
    for arrival in get_arrivals(arrivals_payload)['resultSet']['arrival']:
        pprint(arrival)
        print('<----------------->')


