from faker import Faker
from tabulate import tabulate

faker = Faker()
persons = []
headers = ["Nom", "Email", "Ville"]
totalPersons = 10

for _ in range(totalPersons):
    persons.append([
        faker.name(),
        faker.email(),
        faker.city()
    ])

print(tabulate(persons, headers))
