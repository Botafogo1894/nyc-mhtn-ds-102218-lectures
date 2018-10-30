class Flight:
    def __init__(self, number):
        self._number = number

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number

    def add_airline(self, airline):
        self._airline = airline

    def get_airline(self):
        return self._airline

# Build the following getter and setter methods For airline: name, year (ie. the year of incorporation) For flight: name
#
# (To do the following, look up class methods and class attributes in Python)
#
# Airline.all() -> should return all of the Airlines that have been initialized
# Flight.all() -> should return all of the flights that have been initialized
