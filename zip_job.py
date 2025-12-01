import os
import zipfile

letters = ["a", "b", "c", "d"]

for letter in letters:
    filename = f"{letter}.txt"
    open(filename, "w").close()

for letter in letters:
    filename = f"{letter}.txt"
    if not os.path.exists(filename):
        raise Exception(f"{filename} was NOT created!")

version = os.environ.get("VERSION")
if version is None:
    raise Exception("VERSION environment variable is not set")

for letter in letters:
    txt_file = f"{letter}.txt"
    zip_file = f"{letter}_{version}.zip"
    with zipfile.ZipFile(zip_file, "w") as zipf:
        zipf.write(txt_file)

for letter in letters:
    zip_file = f"{letter}_{version}.zip"
    if not os.path.exists(zip_file):
        raise Exception(f"{zip_file} was NOT created!")
