import os

directory = 'PDF'

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    print(file_path)
    if os.path.isfile(file_path):
        new_filename = filename[32:38]
        new_file_path = os.path.join(directory, new_filename)
        os.replace(file_path, new_file_path)
        print(f"Renamed: {filename} -> {new_filename}")

