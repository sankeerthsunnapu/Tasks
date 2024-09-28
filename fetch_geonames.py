import requests
import mysql.connector

# Step 1: Connect to MySQL Database
def connect_to_db():
    connection = mysql.connector.connect(
        host="localhost",          # Your MySQL host (use localhost if local)
        user="root",      # Replace with your MySQL username
        password="Sankeerth@1710",  # Replace with your MySQL password
        database="cities_db"       # Database name
    )
    return connection

# Step 2: Function to Insert City Data into MySQL
def insert_city_data(city):
    connection = connect_to_db()
    cursor = connection.cursor()

    # SQL Query for Inserting Data
    sql = """
    INSERT INTO cities (toponymy_name, population, latitude, longitude)
    VALUES (%s, %s, %s, %s)
    """
    # Extracting required fields from JSON
    values = (
        city['toponymName'], 
        int(city.get('population', 0)),  # Handle missing population
        float(city['lat']), 
        float(city['lng'])
    )
    
    # Execute SQL query and commit changes
    cursor.execute(sql, values)
    connection.commit()

    # Close connection
    cursor.close()
    connection.close()

# Step 3: Function to Fetch and Process JSON Data from API
def fetch_and_process_data():
    # Step 3.1: Fetch data from GeoNames API
    url = "http://api.geonames.org/searchJSON?country=IN&featureClass=P&maxRows=100&username=srirampalika23"
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Step 3.2: Extract cities data
        cities = data['geonames']  # The city data is in the 'geonames' key
        
        # Step 3.3: Iterate over the cities and insert into the database
        for city in cities:
            insert_city_data(city)
            print(f"Inserted city: {city['toponymName']}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

# Main Program to Run the Script
if __name__ == "__main__":
    # Fetch data from API and insert into database
    fetch_and_process_data()
