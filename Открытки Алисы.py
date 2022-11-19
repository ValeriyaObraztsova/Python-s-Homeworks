postcards = {
    "Maria": "London",
    "Lorenzo": "Milan",
    "Oleg": "Canberra",
    "Hans": "Calgary",
    "Mark": "Milan",
    "Alex": "Krakow",
    "Julia": "Murmansk"
}

postcards["Petr"] = "Paris"
postcards["Ivan"] = "Moscow"
print(postcards)

print(postcards["Oleg"])
postcards["Oleg"] = "Sydney"
print(postcards["Oleg"])
print(postcards)

postcards_values = list(postcards.values())
print(postcards_values)
print(set(postcards_values))
print(len(set(postcards_values)))