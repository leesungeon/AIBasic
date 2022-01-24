import csv

filepath = "./data-01-test-score.csv"

class ReadCSV(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        data = []
        row_list = []

        f = open(self.file_path, "r")
        rdr = csv.reader(f)
        for line in rdr:
            for val in line:
                row_list.append(int(val))
            data.append(row_list)
            row_list = []
        f.close()

        return data
    
    def merge_list(self):
        merge_list = []
        data = self.read_file()
        for dt in data:
            merge_list.append(sum(dt))
        
        return merge_list

read_csv = ReadCSV(filepath)
print(read_csv.read_file())
print(read_csv.merge_list())