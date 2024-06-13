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
    def __init__(self, country, population, area_sqr_km):
        self.country = country
        self.population = population
        self.area_sqr_km = area_sqr_km
        self.is_big = self.population > 250_000_000 or self.area_sqr_km > 3_000_000

    def compare_pd(self, other_country):
        self_pd = self.population / self.area_sqr_km
        other_pd = other_country.population / other_country.area_sqr_km
        
        if self_pd > other_pd:
            comparison = "larger"
        else:
            comparison = "smaller"
        return f"{self.country} has a {comparison} population density than {other_country.country}"


# Examples:
australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

print(australia.is_big)  # Expected: True
print(andorra.is_big)  # Expected: False
print(andorra.compare_pd(australia))  # Expected: "Andorra has a larger population density than Australia"
