import folium
from src.data_loader import Dealer

class MapVisualizer:
    def __init__(self, center_coordinates, zoom_start=12):
        self.map = folium.Map(location=center_coordinates, zoom_start=zoom_start)

    def add_dealer_pin(self, dealer):
        color = self.get_pin_color(dealer.shipping_days)
        popup_text = f"{dealer.name} ({dealer.city})<br>Shipping Days: {dealer.shipping_days}"
        folium.Marker(
            location=dealer.coordinates,
            popup=popup_text,
            icon=folium.Icon(color=color)
        ).add_to(self.map)

    def get_pin_color(self, shipping_days):
        color_map = {
            "Mondays only": "blue",
            "Tues/Thurs": "green",
            "Mon/Wed": "purple",
            "Mon/Thur": "orange",
            "Wednesdays only": "red",
            "Wed/Fri": "darkred"
        }
        return color_map.get(shipping_days.strip(), "gray")

    def save_map(self, filepath):
        self.map.save(filepath)
