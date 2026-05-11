from functions.get_files_info import get_files_info

def runfileInfo():
    # print("getting with no directory")
    print(get_files_info("calculator", "."))
    # print("getting with pkg dir")
    print(get_files_info("calculator", "pkg"))
    # print("getting with bin dir")
    print(get_files_info("calculator", "/bin"))
    # print("getting with ../ dir")
    print(get_files_info("calculator", "../"))

if __name__ == "__main__":
    runfileInfo()