import json
from tkinter.filedialog import asksaveasfilename

# export JSON file
def export_json_file(coordinates_list):
    if not coordinates_list:
        return

    try:
        json_output = json.dumps(coordinates_list, indent=4)
        
        file_path = asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        
        if file_path:
            with open(file_path, 'w') as f:
                f.write(json_output)
            return
    except Exception as e:
        return
