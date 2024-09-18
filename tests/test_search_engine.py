import unittest
from src.data_loader import Dealer
from src.search_engine import SearchEngine

class TestSearchEngine(unittest.TestCase):

    def setUp(self):
        # Setup some test data
        self.dealers = [
            Dealer("MetalCorp", "New York", [40.7128, -74.0060], "Mondays only"),
            Dealer("SteelWorks", "Boston", [42.3601, -71.0589], "Tues/Thurs"),
            Dealer("IronForge", "Philadelphia", [39.9526, -75.1652], "Mon/Wed"),
            Dealer("CopperKing", "New York", [40.7306, -73.9352], "Wed/Fri")
        ]
        self.search_engine = SearchEngine(self.dealers)

    def test_find_dealers_by_city(self):
        # Test searching by city name
        new_york_dealers = self.search_engine.find_dealers_by_city("New York")
        self.assertEqual(len(new_york_dealers), 2)
        self.assertEqual(new_york_dealers[0].name, "MetalCorp")
        self.assertEqual(new_york_dealers[1].name, "CopperKing")

        boston_dealers = self.search_engine.find_dealers_by_city("Boston")
        self.assertEqual(len(boston_dealers), 1)
        self.assertEqual(boston_dealers[0].name, "SteelWorks")

        # Test searching with a city that doesn't exist
        no_dealers = self.search_engine.find_dealers_by_city("Chicago")
        self.assertEqual(len(no_dealers), 0)

    def test_sort_dealers_by_proximity(self):
        # Test sorting by proximity to New York City coordinates
        sorted_dealers = self.search_engine.sort_dealers_by_proximity([40.7128, -74.0060])
        self.assertEqual(sorted_dealers[0].name, "MetalCorp")  # Closest to New York
        self.assertEqual(sorted_dealers[1].name, "CopperKing")  # Second closest to New York
        self.assertEqual(sorted_dealers[2].name, "IronForge")  # Third closest to New York (IronForge in Philadelphia)
        self.assertEqual(sorted_dealers[3].name, "SteelWorks")  # Farthest from New York (SteelWorks in Boston)


if __name__ == '__main__':
    unittest.main()
