### Project Description: We Deliver - A System for a Delivery Company

#### Overview:
"We Deliver" is a software system designed to help a delivery company manage its drivers and the cities they deliver to. The system allows users to keep track of driver information, such as their worker ID, name, and starting city, as well as the cities served by the company and their connections.

#### Features:

1. **Main Menu:**
   - **Welcome Message:** Greets the user upon running the program.
   - **Options:**
     - **Drivers' Menu:** Allows access to driver management.
     - **Cities' Menu:** Allows access to city management.
     - **Exit:** Exits the system.

2. **Drivers' Menu:**
   - **View All Drivers:** Displays a list of all drivers, including their worker ID, name, and start city.
   - **Add a Driver:**
     - Prompts the user to enter the driver's name and start city.
     - Automatically generates a unique worker ID.
     - Validates the start city against the existing database.
     - Offers the option to add a new city to the database if the entered start city is not found.
   - **Go Back:** Returns to the main menu.

3. **Cities' Menu:**
   - **Show Cities:** Displays a list of all cities in the system.
   - **Print Neighboring Cities:**
     - Prompts the user to enter a city name.
     - Displays all cities that can be reached from the entered city.
   - **Print Drivers Delivering to City:**
     - Prompts the user to enter a city name.
     - Displays all drivers who deliver to the entered city, including those who reach it through different routes.

#### Key Functionalities:

- **Driver Management:**
  - **Automatic ID Generation:** Ensures each driver has a unique identifier.
  - **City Validation:** Confirms that drivers' start cities are in the database and offers to add new cities as needed.
  
- **City Management:**
  - **City Connectivity:** Manages which cities are connected and reachable from each other, potentially using algorithms like Breadth-First Search (BFS) or Depth-First Search (DFS).

#### Goals:
- **User-Friendly Interface:** Provides an easy-to-navigate menu system for managing drivers and cities.
- **Data Integrity:** Ensures that all data entered into the system is validated and consistent.
- **Scalability:** Allows the addition of new drivers and cities as the company expands.

#### Example Use Case:
1. A user runs the program and is greeted with the main menu.
2. The user selects the drivers' menu to add a new driver.
3. The system prompts for the driver's name and start city.
4. The system checks if the start city is in the database. If not, it asks if the user wants to add the city.
5. The system generates a unique ID for the driver and saves their information.
6. The user then selects the cities' menu to view all cities and their connections.
7. The user can also print drivers delivering to a specific city, ensuring efficient delivery management.

By implementing these features, "We Deliver" aims to streamline the delivery company's operations, making it easier to manage logistics and improve overall efficiency.
