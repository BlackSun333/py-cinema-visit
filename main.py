from typing import List, Dict
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: List[Dict[str, str]],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_instances: List[Customer] = []

    for customer_data in customers:
        new_customer = Customer(customer_data["name"], customer_data["food"])
        customer_instances.append(new_customer)
        CinemaBar.sell_product(new_customer.food, new_customer)

    cleaner_instance = Cleaner(cleaner)
    hall_instance = CinemaHall(hall_number)

    hall_instance.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )
