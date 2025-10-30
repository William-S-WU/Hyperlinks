import os

directory = os.getcwd()  # Working directory
print("Working Directory:", directory)

def get_filenames_without_extension(directory):
    filenames = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            filenames.append(os.path.splitext(filename)[0])
    return filenames


def process_files(directory):
    #directory = os.path.join(directory, "Staging")
    for filename in os.listdir(directory):
        if filename.lower().endswith((".txt")):  # find text file
            print(f"Processing: {filename}")
            
            file_path = os.path.join(directory, filename)
            print("filepath is:", file_path)
            return(file_path, filename)
"""
def double_check(file_list, file_path):
    matrix = np.genfromtxt(file_path, delimiter='\t', dtype=None, encoding=None, invalid_raise=False) 
    first_column = matrix[:, 0]
    return(first_column)
"""
#############
def double_check(file_list, file_path):
    values_list = []

    with open(file_path, 'r') as file:
        for line in file:
            # Split the line by comma and append the resulting list to values_list
            values_list.append(line.strip().split('\t'))
    return(values_list)

def compair(values_list, file_list):
    issue_files = []
    check1 = 1
    for i in range(len(values_list)):
        if check1 == 0:
            print("everything is good, ... not their is an issue")
            print(values_list[i-1])
            issue_files.append(values_list[i-1])
        else:
            print("everything is good for real this time")
        value1 = values_list[i]
        check1 = 0
        for j in range(len(file_list)):

            value2 = file_list[j]
            #print(value1)
            #print(value2)
            #print(" file from list is :  ", file_list[j], "file from txt is :    ", values_list[i])
            if value1 == value2:
                check1 = 1
                break
        h = i
    if check1 == 0:
        print("everything is good, ... not their is an issue")
        print(values_list[h])
        issue_files.append(values_list[h])
    else:
        print("everything is good for real this time")
    value1 = values_list[h]
    return(issue_files)


def write_file(directory, issue_files):

    file_path = os.path.join(directory, 'output.txt')

    # Open file for writing
    with open(file_path, 'w') as file:
        for issue in issue_files:
            file.write(f"{issue}\n")


#############
    
file_path, filename = process_files(directory)
#print(file_path)
file_list = get_filenames_without_extension(directory)
values_list = double_check(file_list, file_path)
values_list2 = [item[0] for item in values_list]
#print(file_list)
#print(values_list)
issue_files = compair(values_list2, file_list)
print("missing or correpted files are:      ", issue_files)
write_file(directory, issue_files)
"""
print(values_list)
print(type(values_list))
print(values_list2[0])
print(file_list[0])
print(type(values_list2[0]))
"""
