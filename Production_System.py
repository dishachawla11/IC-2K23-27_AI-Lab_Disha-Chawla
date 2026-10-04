# Facts
facts = ["rain", "cloudy"]

# Production rules
rules = [
    (["rain"], "carry umbrella"),
    (["cloudy"], "weather may change"),
    (["rain", "cloudy"], "it may rain heavily")
]

# Apply rules
for conditions, conclusion in rules:
    if all(condition in facts for condition in conditions):
        print("IF", " AND ".join(conditions), "THEN", conclusion)
