import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    # validate path
    working_path = os.path.abspath(working_directory)
    target_path = os.path.normpath(os.path.join(working_path, file_path))
    validTargetDir = os.path.commonpath([working_path, target_path]) == working_path
    if not validTargetDir:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    file_contents = ""
    try:
        with open(target_path, 'r') as f:
            file_contents = f.read(MAX_CHARS)
            test_string = f.read(1)
            if test_string != '':
                file_contents += f'[...File "{target_path}" truncated at {MAX_CHARS} characters]'
            return file_contents
    except Exception as e:
        return f'Error: {e}'



if __name__ == "__main__":
    print(get_file_content(os.getcwd(), "main.py"))