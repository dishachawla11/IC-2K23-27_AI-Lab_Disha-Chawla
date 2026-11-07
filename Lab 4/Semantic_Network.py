# Semantic Network in AI

knowledge = {
    "Dog": {"is_a": "Animal", "has": "Four legs"},
    "Cat": {"is_a": "Animal", "can": "Meow"},
    "Animal": {"has": "Life"}
}

# Display semantic network
for node, relations in knowledge.items():
    for relation, value in relations.items():
        print(node, "----", relation, "---->", value)
