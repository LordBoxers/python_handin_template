import csv

def print_file_content(file):
    with open(file) as file_object:
        contents = file_object.read()
        print(contents)

##print_file_content("/home/jovyan/python_handin_template/modules/week_2/country_codes.csv")

def write_list_to_file(output_file, lst):
    with open(output_file, 'w') as file_object:
        for l in lst:
            for e in l:
                file_object.write(e+"\n")

def read_csv(input_file):
    lst = []
    with open(input_file) as file_object:
        reader = csv.reader(file_object)
        header_row = next(reader)

        for row in reader:
            lst.append(row)
    return lst
        
