class Manufacturer:
    def __init__(self, name, country):
        self._name = name
        self._country = country
    
    
    def __str__(self):
        return f"({self._name, {self._country}})"