## DealerLocator 

An interactive map application for locating dealers/distributors. Designed for small manufacturing companies or vendors who handle their own shipping to distributors. This application allows users to search for dealers in specific cities, 
view their locations on an interactive map, and edit dealer details, all within the browser. 

**_Note from the developer:_**  _DealerLocator was designed for a very specific use for Marco Metals LLC, the company at which I have worked for many years. It was intended to only be used on a **local network only**. This project is **not** designed for use on the internet and 
does not meet cybersecurity standards. Significant changes to how the database is handled and accessed would need to be made to make this project suitable for non-local network use._

## Features

### In-browser Map Visualization
- Displays dealer locations on an interactive map.
- Pins are color-coded based on shipping days.
- Each pin is clickable, showing dealer information including name, city, and shipping schedule.
- Users can search for a city to center the map.

### Dealer Search Functionality
- Search for dealers by entering a city name in the search bar.
- The map automatically centers on the searched city.
  
### Dealer Management (Edit Page)
- **Add/Edit Dealers**: Users can add new dealers or edit existing dealer information (name, city, coordinates, shipping days).
- The form is auto-populated when an existing dealer is selected, allowing easy modification.
- **Delete Dealers**: Select and delete a specific dealer from the list.

## Technologies Used
- **Python (Flask)** – Backend framework for routing and handling logic.
- **Folium** – For creating the interactive map.
- **Pandas** – Used to load and process dealer data from a CSV file.
- **HTML/CSS/JavaScript** – For building the user interface and rendering the map.

## Setup and Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/DealerLocator.git
    cd DealerLocator
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv dealer_locator_env
    source dealer_locator_env/bin/activate  # For Linux/Mac
    dealer_locator_env\Scripts\activate  # For Windows
    ```

3. **Install required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    flask run
    ```

    The application will be accessible at `http://127.0.0.1:5000/` in your browser.

