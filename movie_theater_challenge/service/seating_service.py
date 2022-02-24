from movie_theater_challenge.service.parser import FileParser


class MovieTheater:

    def __init__(self):
        self.rows = 10
        self.seats = 20
        self.theater_seating = [['1' for _ in range(self.seats)] for _ in range(self.rows)]
        self.remaining_seats = {key:20 for key in range(self.rows)}

    def get_theater_seating(self):
        return self.theater_seating

    def read_request_data(self, input_path):
        input_file = FileParser().read_file(input_path)
        for reservation in input_file:
            self.process_requests(reservation)

    def process_requests(self, reservation):
        if not reservation:
            print("ERROR: process_requests received invalid reservation")
        row = reservation[0]
        row_num = int(row[1:]) - 1
        group_size = int(reservation[1])
        if self.validate(row_num, group_size):
            booked_row = self.book_seats((row_num, row, group_size))
            if booked_row:
                self.theater_seating[row_num] = booked_row[:]
            else:
                print(f"ERROR: Not enough seats are open for row {row} to maintain social distancing measures for a "
                      f"group of size {group_size} ")

        else:
            print(f"INVALID INPUT: for row {row} and reservation size {group_size}")



    def write_theater_seating(self, output_path):
        FileParser().write_file(output_path, self.get_theater_seating())


    def validate(self, row, group_size):
        if group_size > 0:

            if row<0 or row>=10:
                print("ERROR: invalid row")
                return False
            if self.remaining_seats[row] >= group_size:
                return True
            else:
                print(f"ERROR: not enough seats in row {row} for {group_size} people")
                return False

        else:
            print("ERROR: process_requests received invalid reservation group size")
            return False

    def book_seats(self, reservation_data):
        row_num, row, group_size = reservation_data
        p1 = 0
        rng = 0
        copy_of_seating = self.theater_seating[row_num]
        while p1 < len(copy_of_seating) and group_size > 0:
            if copy_of_seating[p1] == '1':
                valid = True
                for i in range(p1 - 3, p1 + 1):
                    if 0 <= i < len(copy_of_seating):
                        if copy_of_seating[i] == 'X':
                            valid = False
                for i in range(p1, p1 + 3):
                    if 0 <= i < len(copy_of_seating):
                        if copy_of_seating[i] == 'X':
                            valid = False
                if valid:
                    p2 = p1
                    temp_group_size = group_size

                    while p2 < len(copy_of_seating) and copy_of_seating[p2] == '1':
                        rng += 1
                        p2 += 1
                        if rng == group_size:
                            for idx in range(p1, p1 + rng):
                                copy_of_seating[idx] = 'X'
                                temp_group_size -= 1
                            break
                    if temp_group_size == 0:
                        group_size = 0
                        break
                    rng = 0
                    p1 = p2 + 1
                else:
                    p1 += 1
            else:
                p1 += 1

        if group_size == 0:
            return copy_of_seating
        else:
            return []
