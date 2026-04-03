class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: list,
            cleaning_staff: any
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
