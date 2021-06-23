import sys

class CsvReader:
    def __init__(self):
        self.input_file = sys.argv[1]
        self.output_file = sys.argv[2]
        self.task = []
        self.lines = self.read_file()
        for change in sys.argv[3:]:
            self.task.append(change.split(","))

    def __str__(self):
        return f"Input file: {self.input_file}; output file: {self.output_file}; changes: {self.task}"

    def read_file(self):
        lines = []
        with open(self.input_file, "r") as file:
            for line in file.readlines():
                tmp = line.split("\n")[0].split(",")
                lines.append(tmp)
        return lines

    def modify_file(self):
        for change in self.task:
            self.lines[int(change[0])][int(change[1])] = change[2]

    def save_file(self):
        with open(self.output_file, "w") as file:
            for line in self.lines:
                for element in line[:-1]:
                    file.write(str(element) + ",")
                file.write(str(line[-1]) + "\n")


read = CsvReader()
read.read_file()
print(read.lines)
read.modify_file()
print(read.lines)
read.save_file()