import csv
import json


def csv_to_json(csv_file_path, json_file_path, selected_headers=None):
    """Convert a CSV file to a JSON file."""
    with open(csv_file_path, encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        header = None
        for row in csv_reader:
            if row and row[0].strip().startswith("Country Name"):
                header = row
                break
        if header is None:
            raise ValueError("Header row starting with 'Country Name' not found.")
        if selected_headers is None:
            selected_headers = header
        header_indexes = {name: header.index(name) for name in selected_headers}
        data = []
        for row in csv_reader:
            row_data = {
                name: row[idx] if idx < len(row) else ""
                for name, idx in header_indexes.items()
            }
            data.append(row_data)
    with open(json_file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)
    return data
