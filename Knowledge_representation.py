# Knowledge Representation using a dictionary

knowledge = {
    "Dog": {
        "is_a": "Animal",
        "has": "Four legs",
        "can": "Bark"
    },
    "Cat": {
        "is_a": "Animal",
        "has": "Four legs",
        "can": "Meow"
    }
}

# Display knowledge
for animal, information in knowledge.items():
    print(animal)
    print("Is a:", information["is_a"])
    print("Has:", information["has"])
    print("Can:", information["can"])
    print()
