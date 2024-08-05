import glob
import os

yaml_file_names = sorted(glob.glob("./collections/**/*.yaml", recursive=True))

for i, file in enumerate(yaml_file_names):
    print(
        "Processing file {} of {} file name: {}".format(
            i + 1, len(yaml_file_names), file
        )
    )
    path, filename = os.path.split(file)
    new_filename = filename[3:]
    new_file_path = os.path.join(path, new_filename)
    os.rename(file, new_file_path)
