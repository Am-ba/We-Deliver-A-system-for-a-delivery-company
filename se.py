# Main Menu
# Display the welcome message
# Prompt the user to enter:
# 1. For the drivers' menu
# 2. For the cities' menu
# 3. To exit the system

# If user selects option 1, go to Drivers' Menu
# If user selects option 2, go to Cities' Menu
# If user selects option 3, exit the system

# Drivers' Menu
# Display the drivers' menu options
# Prompt the user to enter:
# 1. To view all the drivers
# 2. To add a driver
# 3. To go back to the main menu

# If user selects option 1, display all drivers and their details
# If user selects option 2, prompt the user to enter the name and start city of the driver
#    - Validate if the start city is in the database
#    - If not, ask the user if they want to add it to the database
#    - Generate a unique worker ID for the new driver and save the details
# If user selects option 3, return to the main menu

# Cities' Menu
# Display the cities' menu options
# Prompt the user to enter:
# 1. To show all cities
# 2. To print neighboring cities
# 3. To print drivers delivering to a city

# If user selects option 1, display the list of all cities
# If user selects option 2, prompt the user to enter a city name
#    - Display all cities that can be reached from the entered city
# If user selects option 3, prompt the user to enter a city name
#    - Display all drivers that are delivering to the entered city

# Helper Functions
# Create a function to generate a unique worker ID
# Create a function to validate if a city is in the database
# Create a function to add a new city to the database
# Create a function to add a new driver to the database
# Create a function to display all drivers
# Create a function to display all cities
# Create a function to find neighboring cities using BFS or DFS
# Create a function to find drivers delivering to a specific city
