import pytest
from manufacturer import Manufacturer


class TestManufacturer:
    def test_manufacturer_init(self):
        manufacturer = Manufacturer("Ford", "USA")
        assert manufacturer._name == "Ford"
        assert manufacturer._country == "USA"

    def test_manufacturer_getters(self):
        manufacturer = Manufacturer("Honda", "Japan")
        assert manufacturer.name == "Honda"
        assert manufacturer.country == "Japan"