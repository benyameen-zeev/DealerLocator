from geopy.distance import geodesic
from src.data_loader import Dealer

class SearchEngine:
    def __init__(self, dealers):
        """
        Initialize the search engine with a list of dealers.
        
        :param dealers: List of Dealer objects.
        """
        self.dealers = dealers

    def find_dealers_by_city(self, city_name):
        """
        Find dealers in or around a specified city.
        
        :param city_name: The name of the city to search for.
        :return: List of dealers located in or near the specified city.
        """
        return [dealer for dealer in self.dealers if dealer.city.lower() == city_name.lower()]

    def sort_dealers_by_proximity(self, reference_coordinates):
        """
        Sort a list of dealers by proximity to a reference point.
        
        :param reference_coordinates: Tuple of (latitude, longitude) to sort by proximity to.
        :return: List of dealers sorted by proximity to the reference coordinates.
        """
        return sorted(self.dealers, key=lambda dealer: geodesic(reference_coordinates, dealer.coordinates).miles)

if __name__ == "__main__":
    # Example usage:
    from src.data_loader import load_dealers
    
    # Load dealers from CSV
    dealers = load_dealers('data/dealers.csv')
    
    # Initialize the search engine with loaded dealers
    search_engine = SearchEngine(dealers)
    
    # Find dealers in a specific city
    city_dealers = search_engine.find_dealers_by_city("New York")
    print("Dealers in New York:", city_dealers)
    
    # Sort dealers by proximity to a given location (e.g., New York City coordinates)
    sorted_dealers = search_engine.sort_dealers_by_proximity((40.7128, -74.0060))
    print("Dealers sorted by proximity to New York City:", sorted_dealers)
