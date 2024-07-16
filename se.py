class WeDeliverSystem:
    #constructor
    def __init__(self):
        self.drivers = {
            "ID001": {"name": "Max Verstappen", "start_city": "Beirut"},
            "ID002": {"name": "Charles Leclerc", "start_city": "Tripoli"},
            "ID003": {"name": "Lando Norris", "start_city": "Saida"},
            "ID004": {"name": "Lewis Hamilton", "start_city": "Zahle"},
            "ID005": {"name": "Sebastian Vettel", "start_city": "Byblos"},
        }
        self.driver_id_counter = 6  # Next ID will be ID006

        self.cities = {
            "Beirut": ["Tripoli", "Saida", "Byblos"],
            "Tripoli": ["Beirut", "Jounieh"],
            "Saida": ["Beirut", "Tyre"],
            "Zahle": ["Baakleen", "Baalbek"],
            "Byblos": ["Beirut", "Batroun"],
            "Jounieh": ["Tripoli", "Batroun"],
            "Tyre": ["Saida", "Naqoura"],
            "Baalbek": ["Zahle", "Hermel"],
            "Batroun": ["Byblos", "Jounieh"],
            "Naqoura": ["Tyre"]
        }
    #Main menu
    def main_menu(self):
        while True:
            print("Hello! Please enter:")
            print("1. To go to the drivers' menu")
            print("2. To go to the cities' menu")
            print("3. To exit the system")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.drivers_menu()
            elif choice == '2':
                self.cities_menu()
            elif choice == '3':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    #driver menu
    def drivers_menu(self):
        while True:
            print("\nDrivers' Menu:")
            print("1. To view all the drivers")
            print("2. To add a driver")
            print("3. To go back to main menu")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.view_all_drivers()
            elif choice == '2':
                self.add_driver()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")
    #View all driver function
    def view_all_drivers(self):
        if not self.drivers:
            print("No drivers available.")
        else:
            for driver_id, driver_info in self.drivers.items():
                print(f"{driver_id}, {driver_info['name']}, {driver_info['start_city']}")
    #add driver function
    #city menu
    def cities_menu(self):
        while True:
            print("\nCities' Menu:")
            print("1. Show cities")
            print("2. Print neighboring cities")
            print("3. Print drivers delivering to city")
            print("4. To go back to main menu")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.show_cities()
            elif choice == '2':
                self.print_neighboring_cities()
            elif choice == '3':
                self.print_drivers_delivering_to_city()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")
        #show cities function
        #print neighboring cities function
        #orint driver delivering to city