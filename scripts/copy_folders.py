import shutil
import os


# defining the function to ignore the files
# if present in any folder
def ignore_files(dir, files):
    return [f for f in files if os.path.isfile(os.path.join(dir, f))]


# calling the shutil.copytree() method and
# passing the src,dst,and ignore parameter
shutil.copytree(
    "collections/B2", "collections/c1/", ignore=ignore_files, dirs_exist_ok=True
)
