# Dictionary in List

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, visits, cities):
    new_country = {} # create a new empty dictionary
    # add the new key-value three pair
    new_country["country"] = country 
    new_country["visits"] = visits 
    new_country["cities"] = cities
    # add the new dictionary to the list
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)