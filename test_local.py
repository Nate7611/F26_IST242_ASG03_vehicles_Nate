import pytest
from manufacturer import Manufacturer

class TestManufacturer:
    def test_manufacturer_init(self):
        manufacturer = Manufacturer("Ford", "USA")
        assert manufacturer._name == "Ford"
        assert manufacturer._country == "USA"
        
    def test_manufacturer_getter(self):
        manufacturer = Manufacturer("Honda", "Japan")
        assert manufacturer.get_name == "Honda"
        assert manufacturer.get_country == "Japan"