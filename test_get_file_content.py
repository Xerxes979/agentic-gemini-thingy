from functions.get_file_content import get_file_content

def test_file_content():
    full_output = get_file_content("calculator", "lorem.txt")
    if "truncated at" in full_output:
        print(f"output truncated properly, size is {len(full_output)} chars")

    print(get_file_content("calculator", "main.py"))
    print(get_file_content("calculator", "pkg/calculator.py"))
    print(get_file_content("calculator", "/bin/cat"))
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

if __name__ == "__main__":
    test_file_content()