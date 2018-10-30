class Airline:
    _all =[]

    def __init__(self, name, year = None):
        Airline._all.append(self)
        self._name = name
        self._year = year

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        self._year = year

    @classmethod
    def all(cls):
        return AirLine._all

#this sets all = the class method
