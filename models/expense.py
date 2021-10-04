from typing import List
from models.person import Person


class Expense:
    def __init__(self, name: str, amount: float, paid: List[Person], split: List[Person]) -> None:
        self.name = name
        self.amount = amount
        self.paid = paid
        self.split = split