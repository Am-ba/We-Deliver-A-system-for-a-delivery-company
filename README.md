We Deliver: A Delivery Company Tracking System
Welcome to We Deliver, a comprehensive system designed with python language to help the delivery company We Deliver efficiently manage its drivers and the cities they deliver to. This program allows the company to keep track of its drivers, their unique worker IDs, names, and starting cities, as well as the cities within the delivery network and the connections between them.

Features
Main Menu
Upon running the program, users are greeted with the following options:

Drivers’ Menu: Manage and view drivers.
Cities’ Menu: Manage and view cities.
Exit: Exit the system.
Drivers’ Menu
In this menu, users can:

View all drivers: Display a list of all drivers with their details.
Add a driver: Add a new driver by providing their name and starting city.
Go back to the main menu: Return to the main menu.
View All Drivers
Displays a list of all drivers in the system, including their IDs, names, and starting cities. For example:

mathematica
Copy code
ID001, Max Verstappen, Akkar
ID002, Charles Leclerc, Saida
ID003, Lando Norris, Jbeil
Add a Driver
Allows the user to add a new driver by entering the driver’s name and starting city. The system automatically generates a unique ID for the new driver. If the entered start city is not in the database, the user is prompted to add it.

Go Back
Returns the user to the main menu.

Cities’ Menu
In this menu, users can:

Show cities: Display a list of all cities in the system.
Print neighboring cities: Display neighboring cities that can be reached from a specified city.
Print drivers delivering to a city: Display drivers delivering to a specified city.
Show Cities
Prints a list of all cities within the system.

Print Neighboring Cities
Prompts the user to enter a city name and then displays all neighboring cities that can be reached from the specified city.

Print Drivers Delivering to a City
Prompts the user to enter a city name and then displays all drivers delivering to that city, including drivers who may have to go through different cities to reach the destination.
