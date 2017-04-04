# This example deals with the reading and writing of data from and to a CSV file.

import csv
#----------------------------------------------------------------------
def csv_reader(file_obj):
    """
    Read a csv file
    """
    reader = csv.reader(file_obj)
    for row in reader:
        print(" ".join(row))
#----------------------------------------------------------------------
if __name__ == "__main__":
    csv_path = "TB_data_dictionary_2014-02-26.csv"
    with open(csv_path, "rb") as f_obj:
        csv_reader(f_obj)

# Sample CSV file data below and save it as data.csv

# first_name,last_name,address,city,state,zip_code
# Tyrese,Hirthe,1404 Turner Ville,Strackeport,NY,19106-8813
# Jules,Dicki,2410 Estella Cape Suite 061,Lake Nickolasville,ME,00621-7435
# Dedric,Medhurst,6912 Dayna Shoal,Stiedemannberg,SC,43259-2273

import csv
#----------------------------------------------------------------------
def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        print(line["first_name"]),
        print(line["last_name"])
#----------------------------------------------------------------------
if __name__ == "__main__":
    with open("data.csv") as f_obj:
        csv_dict_reader(f_obj)



import csv
#----------------------------------------------------------------------
def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    with open(path, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)
#----------------------------------------------------------------------
if __name__ == "__main__":
    data = ["first_name,last_name,city".split(","),
            "Tyrese,Hirthe,Strackeport".split(","),
            "Jules,Dicki,Lake Nickolasville".split(","),
            "Dedric,Medhurst,Stiedemannberg".split(",")
            ]
    path = "output.csv"
    csv_writer(data, path)

## Now in order to convert the CSV output into a set of Tuples, 
## Please follow the below method.


    for values in data[1:]:
    inner_dict = dict(zip(fieldnames, values))
    my_list.append(inner_dict)


    