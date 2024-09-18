from flask import render_template, request, redirect, url_for, send_from_directory
from app import app
from src.data_loader import load_dealers, Dealer
from src.search_engine import SearchEngine
from src.map_visualizer import MapVisualizer
import csv

# Path to the CSV file
filepath = 'data/dealers.csv'

@app.route('/', methods=['GET', 'POST'])
def index():
    dealers = load_dealers(filepath)
    search_engine = SearchEngine(dealers)

    if request.method == 'POST':
        city_name = request.form.get('city')
        found_dealers = search_engine.find_dealers_by_city(city_name)
        if found_dealers:
            center_coordinates = found_dealers[0].coordinates
        else:
            center_coordinates = (38.4496, -78.8689)  # Default to Harrisonburg, VA if city is invalid

        visualizer = MapVisualizer(center_coordinates=center_coordinates, zoom_start=10)
    else:
        visualizer = MapVisualizer(center_coordinates=(38.4496, -78.8689), zoom_start=10)

    for dealer in dealers:
        visualizer.add_dealer_pin(dealer)

    visualizer.save_map('app/static/dealers_map.html')

    return render_template('index.html', map_generated=True)

@app.route('/edit', methods=['GET'])
def edit_page():
    dealers = load_dealers(filepath)
    return render_template('edit.html', dealers=dealers)

@app.route('/add_edit_dealer', methods=['POST'])
def add_edit_dealer():
    original_name = request.form.get('original_name')
    name = request.form.get('name')
    coordinates = request.form.get('coordinates')
    city = request.form.get('city')
    shipping_days = request.form.get('shipping_days')

    lat, lon = map(float, coordinates.split(','))

    dealers = load_dealers(filepath)

    if original_name:  # Editing an existing dealer
        for dealer in dealers:
            if dealer.name == original_name:
                dealer.name = name
                dealer.city = city
                dealer.coordinates = [lat, lon]
                dealer.shipping_days = shipping_days
                break
    else:  # Adding a new dealer
        new_dealer = Dealer(name=name, city=city, coordinates=[lat, lon], shipping_days=shipping_days)
        dealers.append(new_dealer)

    # Rewrite the CSV file with the updated list
    with open(filepath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Dealer Name', 'City', 'X', 'Y', 'Shipping Days'])
        for dealer in dealers:
            writer.writerow([dealer.name, dealer.city, dealer.coordinates[0], dealer.coordinates[1], dealer.shipping_days])

    return redirect(url_for('edit_page'))

@app.route('/delete_dealer', methods=['POST'])
def delete_dealer():
    selected_dealer = request.form.get('delete')

    if not selected_dealer:
        return redirect(url_for('edit_page'))

    # Split the combined value into its components
    selected_dealer_name, selected_dealer_city, selected_dealer_coordinates, selected_dealer_shipping_days = selected_dealer.split('|')
    selected_dealer_coordinates = [float(coord) for coord in selected_dealer_coordinates.split(',')]

    # Load the current dealers list
    dealers = load_dealers(filepath)
    
    # Filter out the dealer to be deleted based on all fields
    dealers = [dealer for dealer in dealers if not (
        dealer.name == selected_dealer_name and 
        dealer.city == selected_dealer_city and 
        dealer.coordinates == selected_dealer_coordinates and 
        dealer.shipping_days == selected_dealer_shipping_days)]

    # Rewrite the CSV file with the updated list (without the deleted dealer)
    with open(filepath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Dealer Name', 'City', 'X', 'Y', 'Shipping Days'])
        for dealer in dealers:
            writer.writerow([dealer.name, dealer.city, dealer.coordinates[0], dealer.coordinates[1], dealer.shipping_days])

    return redirect(url_for('edit_page'))


@app.route('/dealers_map.html')
def dealers_map():
    return send_from_directory('static', 'dealers_map.html')
