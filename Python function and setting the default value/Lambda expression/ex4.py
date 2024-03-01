people = [{"name": "hola", "age": 30}, {"name": "sjsjk", "age": 25}, {"name": "dan", "age": 35}]
sorted_people = sorted(people, key=lambda x: x["age"])
print(sorted_people)