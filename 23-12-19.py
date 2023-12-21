# Create a simple bank account class, BankAccount, with the following specifications:

# The BankAccount class should have an attribute balance which starts at 0.
# It should have an instance method deposit that allows an amount to be added to the balance.
# It should have an instance method withdraw that allows an amount to be taken from the balance.
# If the balance is less than the withdrawal amount, print a message that says "Insufficient funds".
# Add a class method from_balance that takes a starting balance as an argument and returns a new BankAccount instance with that starting balance.
# Add a static method transfer that takes two BankAccount instances and an amount as arguments.
# It should withdraw the amount from the first account and deposit it into the second account.

# Sukurkite paprastą banko sąskaitos klasę "BankAccount" su šiomis specifikacijomis:

# Banko sąskaitos klasė turėtų turėti atributų balansą, kuris prasideda nuo 0.
# Jame turėtų būti egzemplioriaus metodo indėlis, leidžiantis pridėti sumą prie balanso.
# Jame turėtų būti egzemplioriaus metodas, leidžiantis iš likučio paimti sumą.
# Jei likutis yra mažesnis už išėmimo sumą, atsispausdinkite pranešimą, kuriame parašyta "Nepakanka lėšų".
# Pridėkite klasės metodą from_balance, kuris užima pradinis balansas kaip argumentas ir grąžina naują banko sąskaitos egzempliorių su tuo pradiniu balansu.
# Pridėkite statinio metodo pervedimą, kuriam reikia dviejų banko sąskaitos egzempliorių ir sumos kaip argumentų.
# Ji turėtų išimti sumą iš pirmosios sąskaitos ir įnešti ją į antrąją sąskaitą.


class BankAccount:
    def __init__(self, balanc: float = 0.0) -> None:
        self.balanc = balanc

    def deposit(self, amount: float) -> None:
        self.balanc += amount

    def withdraw(self, amount: float) -> None:
        if self.balanc < amount:
            print("Insufficient funds")

        else:
            self.balanc -= amount

    @classmethod
    def from_balance(
        cls,
        str_balanc,
    ) -> "BankAccount":
        balanc = str_balanc
        return cls(balanc)

    @staticmethod
    def transfer(acount_1: "BankAccount", acount_2: "BankAccount", amount):
        acount_1.withdraw(amount)
        acount_2.deposit(amount)


acount_1 = BankAccount.from_balance(2000.0)
acount_2 = BankAccount()

BankAccount.transfer(acount_1=acount_1, acount_2=acount_2, amount=20)
print(acount_1.balanc)
print(acount_2.balanc)


# 5 task
#
#
# Create a SpaceStation class with the following specifications:

# The SpaceStation class should have an attribute astronauts which is a list of dictionaries. Each dictionary represents an astronaut and has keys: name, nationality, and mission_duration.
# It should have an instance method add_astronaut that takes a name, nationality, and mission duration, creates a new astronaut dictionary, and adds it to the astronauts list.
# It should have an instance method find_astronaut that takes a name and returns the astronaut dictionary with that name, or None if no such astronaut is found.
# Add a class method from_astronaut_list that takes a list of astronauts (each represented as a dictionary) and returns a new SpaceStation instance with those astronauts.
# Add a static method is_long_term_mission that takes an astronaut dictionary and returns True if the astronaut's mission duration is more than 6 months, and False otherwise.
# Add an instance method remove_astronaut that takes a name and removes the astronaut with that name from the astronauts list.

from typing import List, Dict, Optional, Type

class Astronaut:
    def __init__(self, name: str, nationality: str, mission_duration: int) -> None:
        self.name = name
        self.nationality = nationality
        self.mission_duration = mission_duration

class SpaceStation:
    def __init__(self, astronauts: List[Astronaut]) -> None:
        self.astronauts = astronauts

    def add_astronaut(self, name: str, nationality: str, mission_duration: int) -> None:
        astronaut = Astronaut(name, nationality, mission_duration)
        self.astronauts.append(astronaut)

    def find_astronaut(self, name: str) -> Optional[Astronaut]:
        for astronaut in self.astronauts:
            if astronaut.name == name:
                return astronaut
        return None

    @classmethod
    def from_list(cls: Type['SpaceStation'], astronauts: List[Dict[str, str]]) -> 'SpaceStation':
        astronaut_objects = [Astronaut(**astronaut) for astronaut in astronauts]
        return cls(astronaut_objects)

    @staticmethod
    def is_long_term_mission(astronaut: Astronaut) -> bool:
        return astronaut.mission_duration > 6

    def remove_astronaut(self, name: str) -> None:
        self.astronauts = [astronaut for astronaut in self.astronauts if astronaut.name != name]



