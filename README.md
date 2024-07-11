 
class WeDeliverSystem:
    #main menu function
    def main_menu(self):
        while True:
            print("Hello! Please enter: ")
            print("1. To go to drivers menu")
            print("2. To go to cities menu")
            print("3. To exit the system")
            choice= input("Enter your choice: ")
            if choice == '1':
                self.drivers_menu()
            elif choice == '2':
                self.cities_menu()
            elif choice == '3':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    #Driver Menu
    def drivers_menu(self):
        while True:
            print("\n Driver Menu:")
            print("1. To view all the drivers")
            print("2. To add a driver")
            print("3. To go back to main menu")
            choice =input("Enter yout choice: ")
            if choice == '1':
                self.view_all_drivers()
            elif choice == '2':
                self.add_driver()
            elif choice == 3:
                print("Thank you for using our software")
            else:
                print("Invalid choice !!#")
    #View all drivers
    #Add a driver
    #Cities MENU  
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
    #Show cities
    #Print neighboring cities 
    #Print Drivers delivering to city   
#Main function
if __name__ == "__main__":
    system = WeDeliverSystem()
    system.main_menu()   
     
