import json
import glob
import os

uploaded_file_path = "courses.json"

with open(uploaded_file_path) as json_file:
    words = json.load(json_file)

for word_dict in words:
    word_name = word_dict["name"]
    word_id = str(word_dict["publ_id"])

    for file in glob.glob("audio/*"):
        path, filename = os.path.split(file)
        filename = filename.removesuffix(".ogg")
        if filename == word_id:
            new_file_name = os.path.join("audio", f"{word_name}.ogg")
            os.rename(file, new_file_name)
