import json
import os
from datetime import datetime

FILENAME = "data.json"
def load_records():
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_records(records):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(records, file, ensure_ascii=False, indent=4)




