import os

def get_files_info(working_directory, directory="."):
    # validate path
    workingPath = os.path.abspath(working_directory)
    targetPath = os.path.normpath(os.path.join(workingPath, directory))
    validTargetDir = os.path.commonpath([workingPath, targetPath]) == workingPath
    if not validTargetDir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    else:
        # check if the requested working directory is a directory
        if not os.path.exists(targetPath):
            return f'Error: "{directory}" is not a directory'

        # iterate through target directory items and get info
        if directory == ".":
            outString = "Result for current directory: \n"
        else:
            outString = f"Result for '{directory}' directory: \n"
        try:
            for item in os.listdir(targetPath):
                # print("item is: ", item)
                itemString = f"- {item}: file_size={os.path.getsize(os.path.join(targetPath, item))} bytes, is_dir={os.path.isdir(os.path.join(targetPath, item))}"
                outString += itemString + "\n"
        except Exception as e:
            outString = f'Error: {e}'
        return outString



if __name__ == "__main__":
    get_files_info(os.getcwd())