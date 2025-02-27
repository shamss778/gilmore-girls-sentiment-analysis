import os

directory = 'PDF'

for filename in os.listdir(directory):
    if not filename.endswith('.pdf'):
        file_path = os.path.join(directory, filename)
        new_filename = filename + '.pdf'
        new_file_path = os.path.join(directory, new_filename)
        try:
            os.replace(file_path, new_file_path)
            print(f"Added .pdf extension: {filename} -> {new_filename}")
        except PermissionError:
            print(f"Permission denied for: {filename}")
        except Exception as e:
            print(f"Error adding extension to {filename}: {str(e)}")