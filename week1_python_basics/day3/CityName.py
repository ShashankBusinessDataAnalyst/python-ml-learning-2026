def city_country(city, country):
    return f'"You have provided {city.title()}, {country.upper()}"'

city = input("Enter city name: ")
country = input("Enter country name: ")

print(city_country(city, country))