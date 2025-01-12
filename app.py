from tkinter import Tk, Label, Entry, Button, Text, Scrollbar, END, Frame
from parser import add_coordinates, convert_to_json, clear_all
from file_handler import export_json_file

coordinates_list = []

# update output coordinates list
def update_coordinates_output(lat, lng, url):
    output_coordinates.insert(END, f"Added: lat {lat}, lng {lng}\n")

# clear outputs
def clear_all_outputs():
    clear_all()

# Tkinter GUI
root = Tk()
root.title("Parse Google Maps Street View URL")

# URL Input
Label(root, text="Enter Google Maps URL:").pack(pady=5)
url = Entry(root, width=80)
url.pack(pady=5)

# Input Buttons: Add and Clear 
input_frame = Frame(root)
input_frame.pack(pady=5)

Button(input_frame, text="Add to List", command=lambda: add_coordinates(url.get(), coordinates_list, update_coordinates_output, url), bg="green", fg="white").pack(side="left", padx=5)
Button(input_frame, text="Clear All", command=clear_all_outputs, bg="red", fg="white").pack(side="left", padx=5)

# Output Frame
output_frame = Frame(root)
output_frame.pack(pady=10)

# Coordinates List
Label(output_frame, text="Coordinates List:").grid(row=0, column=0, padx=10)
output_coordinates = Text(output_frame, height=15, width=40, wrap="word")
output_coordinates.grid(row=1, column=0, padx=10)

scrollbar_coordinates = Scrollbar(output_frame, command=output_coordinates.yview)
output_coordinates.config(yscrollcommand=scrollbar_coordinates.set)
scrollbar_coordinates.grid(row=1, column=1, sticky="ns")

# JSON Output
Label(output_frame, text="JSON Output:").grid(row=0, column=2, padx=10)
output_json = Text(output_frame, height=15, width=40, wrap="word")
output_json.grid(row=1, column=2, padx=10)

scrollbar_json = Scrollbar(output_frame, command=output_json.yview)
output_json.config(yscrollcommand=scrollbar_json.set)
scrollbar_json.grid(row=1, column=3, sticky="ns")

Button(root, text="Convert to JSON", command=lambda: convert_to_json(coordinates_list, output_json), bg="blue", fg="white").pack(pady=5)
Button(root, text="Export JSON to File", command=lambda: export_json_file(coordinates_list), bg="orange", fg="white").pack(pady=5)

# Actually run Tkinter GUI
root.mainloop()