import pandas as pd

class Dealer:
    def __init__(self, name, city, coordinates, shipping_days):
        self.name = name
        self.city = city
        self.coordinates = coordinates
        self.shipping_days = shipping_days

    def __repr__(self):
        return f"{self.name} ({self.city}) - Coordinates: {self.coordinates} - Shipping Days: {self.shipping_days}"

def load_dealers(filepath):
    df = pd.read_csv(filepath)
    dealers = []
    for index, row in df.iterrows():
        dealer = Dealer(
            name=row['Dealer Name'],
            city=row['City'],
            coordinates=[row['X'], row['Y']],
            shipping_days=row['Shipping Days']
        )
        dealers.append(dealer)
    
    # Debug: Print out all loaded dealers
    for dealer in dealers:
        print(dealer)
    
    return dealers
