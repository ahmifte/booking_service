
class FileParser:

    def read_file(self, file_path):
        bookings = []
        temp = __file__
        temp = temp.split("/")
        temp.pop()
        path = '/'.join(temp) + "/input/"+file_path
        with open(path, 'r') as reader:
            line = reader.readline()
            while line != '':
                line = line.strip().split()
                bookings.append(line)
                line = reader.readline()
            reader.close()
        if not bookings:
            error = "Error: Input file is empty"
            raise error
        else:
            return bookings


    def write_file(self, file_path, output_data):
        formatting = {}
        row_labels = "ABCDEFGHIJ"
        for row in range(len(output_data)):
            for seat in range(len(output_data[row])):
                if output_data[row][seat] == 'X':
                    formatting[row] = formatting.get(row, []) + [row_labels[row] + str(seat + 1)]
        if not formatting:
            print("ERROR: invalid seat arrangement provided to write_file")
        temp = __file__
        temp = temp.split("/")
        temp.pop()
        path = '/'.join(temp) + "/output/"+file_path
        print(path)
        with open(path, 'w') as writer:
            for row in formatting:
                writer.write(f"R{str(row).zfill(3)} " + ','.join(formatting[row]) + '\n')
            writer.close()

