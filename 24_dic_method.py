d = {"name": "Ram", "age": 20}

# dict()
d1 = dict(city="Rajkot")
print(d1)

# len()
print(len(d))

# get()
print(d.get("name"))

# keys()
print(d.keys())

# values()
print(d.values())

# items()
print(d.items())

# copy()
x = d.copy()
print(x)

# update()
d.update({"city": "Ahmedabad"})
print(d)

# pop()
d.pop("age")
print(d)

# popitem()
d.popitem()
print(d)

# clear()
d.clear()
print(d)