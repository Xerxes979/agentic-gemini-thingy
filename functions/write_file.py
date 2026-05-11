import os

def write_file(working_directory, file_path, content):
    # validate path
    working_path = os.path.abspath(working_directory)
    target_path = os.path.normpath(os.path.join(working_path, file_path))
    validTargetDir = os.path.commonpath([working_path, target_path]) == working_path
    if not validTargetDir:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(target_path):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    try:
        os.makedirs(os.path.dirname(target_path), exist_ok=True) # create all the folders up to the target file location not including the file itself
        with open(target_path, 'w') as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e}'



if __name__ == "__main__":
    print(write_file(os.getcwd(), "main.py"))