def make_shirt(size="Large", message="I love Python"):
    print(f"The shirt size is {size} and the message is: '{message}'.")

# A large shirt with default message
make_shirt()

# A medium shirt with default message
make_shirt(size="Medium")

# Any size with a different message
make_shirt(size="Small", message="Python is fun!")


def describe_city(city, country="Iceland"):
    print(f"{city} is in {country}.")

# Three different cities
describe_city("Reykjavik")           # Default country
describe_city("Akureyri")            # Default country
describe_city("Tokyo", "Japan")      # Different country
