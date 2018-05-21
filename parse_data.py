import csv

def read_csv(file_name):
    header = []
    data = []

    with open(file_name, newline='') as csvfile:
        data_reader = csv.reader(csvfile, delimiter=' ', quotechar = '"', lineterminator='\r\n', quoting=csv.QUOTE_MINIMAL)
        # Eventually will replace quoting=csv.QUOTE_MINIMAL with quoting=csv.QUOTE_NONNUMERIC
        header = data_reader.__next__()
        print(','.join(header))
        for row in data_reader:
            data.append(row)
        
        for row in data:
            print(','.join(row))

read_csv("/home/ander612/Downloads/data_econ470/total_suicide.csv")