from service.seating_service import MovieTheater


def main():
    theater = MovieTheater()
    theater.read_request_data("input.txt")
    theater.write_theater_seating("output.txt")


if __name__ == "__main__":
    main()
