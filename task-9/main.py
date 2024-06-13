# Class: Country
# Objective: Enhance the `Country` class to include an attribute `is_big` and a method to compare population density with another country.
# Details:
# - The `is_big` attribute should be set to True if either of the following criteria are met:
#   - The population is greater than 250 million.
#   - The area is larger than 3 million square km.
# - The class should also include a method `compare_pd` that compares the population density of the country with another country object.
# - The `compare_pd` method should return a string in the following format: "{country} has a {smaller / larger} population density than {other_country}".
# - Population density is calculated as the population divided by the area.

class Country:
    pass

# Examples:
australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

print(australia.is_big)  # Expected: True
print(andorra.is_big)  # Expected: False
print(andorra.compare_pd(australia))  # Expected: "Andorra has a larger population density than Australia"
