class WeDeliverSystem:
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

    def view_all_drivers(self):
        if not self.drivers:
            print("No drivers available.")
        else:
            for driver_id, driver_info in self.drivers.items():
                print(f"{driver_id}, {driver_info['name']}, {driver_info['start_city']}")

    def add_driver(self):
        name = input("Enter the name of the driver: ")
        start_city = input("Enter the start city of the driver: ")
        if start_city not in self.cities:
            add_city = input(f"{start_city} is not in the database. Do you want to add it? (yes/no): ")
            if add_city.lower() == 'yes':
                self.cities[start_city] = []
            else:
                print("Driver not added.")
                return
        driver_id = f"ID{self.driver_id_counter:03}"
        self.drivers[driver_id] = {'name': name, 'start_city': start_city}
        self.driver_id_counter += 1
        print(f"Driver {name} added with ID {driver_id}.")

    def show_cities(self):
        if not self.cities:
            print("No cities available.")
        else:
            for city in self.cities:
                print(city)

    def print_neighboring_cities(self):
        city = input("Enter the city name: ")
        if city in self.cities:
            neighbors = self.cities[city]
            if not neighbors:
                print(f"No neighboring cities for {city}.")
            else:
                for neighbor in neighbors:
                    print(neighbor)
        else:
            print(f"{city} is not in the database.")

    def print_drivers_delivering_to_city(self):
        city = input("Enter the city name: ")
        if city in self.cities:
            delivering_drivers = []
            for driver_id, driver_info in self.drivers.items():
                if self.can_reach_city(driver_info['start_city'], city):
                    delivering_drivers.append(driver_info['name'])
            if not delivering_drivers:
                print(f"No drivers can deliver to {city}.")
            else:
                for driver in delivering_drivers:
                    print(driver)
        else:
            print(f"{city} is not in the database.")

    def can_reach_city(self, start, destination):
        visited = set()
        return self.bfs(start, destination, visited)

    def bfs(self, start, destination, visited):
        from collections import deque
        queue = deque([start])
        while queue:
            current = queue.popleft()
            if current == destination:
                return True
            visited.add(current)
            for neighbor in self.cities.get(current, []):
                if neighbor not in visited:
                    queue.append(neighbor)
        return False

if __name__ == "__main__":
    system = WeDeliverSystem()
    system.main_menu()
