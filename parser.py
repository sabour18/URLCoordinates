import json
from urllib.parse import urlparse
from tkinter import END

# parse URL, get coordinates
def add_coordinates(url, coordinates_list, update_coordinates_output, url_input):
    url = url.strip()
    if not url:
        return

    try:
        parsed_url = urlparse(url)
        path = parsed_url.path
        if "@" in path:
            coordinates = path.split("@")[1].split(",")[:2]
            lat, lng = coordinates
            lat, lng = float(lat), float(lng)
            coordinates_list.append({"lat": lat, "lng": lng})
            update_coordinates_output(lat, lng, url)
            url_input.delete(0, END)
        else:
            return
    except Exception as e:
        return

# convert coordinates to JSON
def convert_to_json(coordinates_list, output_json):
    if not coordinates_list:
        return

    try:
        wrapped_coordinates = {"customCoordinates": coordinates_list}
        json_output = json.dumps(wrapped_coordinates, indent=4)        
        output_json.delete("1.0", END)
        output_json.insert(END, json_output)
    except Exception as e:
        return

# clear all data and outputs
def clear_all(coordinates_list, output_coordinates, output_json):
    coordinates_list.clear()
    output_coordinates.delete("1.0", END) 
    output_json.delete("1.0", END)
