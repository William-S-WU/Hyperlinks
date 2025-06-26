import os
import re

def find_missing_files(directory):
    print("Starting search for missing files.")

    # Find the input text file in the directory
    input_text_file = None
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            if input_text_file is not None:
                raise ValueError("Multiple text files found. There should be only one text file.")
            input_text_file = file

    if input_text_file is None:
        raise ValueError("No text file found in the directory.")

    input_text_file_path = os.path.join(directory, input_text_file)
    output_log_file_path = os.path.join(directory, f"{os.path.splitext(input_text_file)[0]}_output.txt")

    # Read names from the text file (only the part before the tab)
    expected_files = []
    with open(input_text_file_path, "r", encoding="utf-8") as f:
        for line in f:
            name = line.split('\t')[0].strip()  # Extract the name part before the tab
            expected_files.append(name)

    print(expected_files)
    missing_files = []


    for i in range(len(expected_files)):
        k = 0
        for file in os.listdir(directory):
            print(file)
            file = os.path.splitext(file)[0]
            if expected_files[i] == file:
                k = 1
                break
        if k == 0:
            missing_files.append(file)
    print("missing files")
    print(missing_files)
        
            


directory = os.getcwd()  # Working directory
print("Working Directory:", directory)
find_missing_files(directory)
