people = [
    ("Alice", "Smith"),
    ("Bob", "Jones"),
    ("Cathy", "Brown"),
    ("David", "Jones"),
    ("Eve", "Jones")
]

jones_family = list(filter(lambda name: name[1] == "Jones", people))
print("People with last name Jones:", jones_family)
