import csv

filepath = "./data-01-test-score.csv"

class ReadCSV(object):
    def __init__(self, file_path, data = []):
        self.file_path = file_path
        self.data = data

    def read_file(self):
        f = open(self.file_path, "r")
        rdr = csv.reader(f)
        for line in rdr:
            self.data.append(line)
        f.close()
        return self.data

read_csv = ReadCSV(filepath)
print(read_csv.read_file())