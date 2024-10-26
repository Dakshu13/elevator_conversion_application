# Create an application for the user for elevator floor conversion application
#Provide a print statement to welcome the viewers of the application
print("Welcome to elevator floor conversion application!")
# Basically, there are two types of elevators
# type 1 : US based floor - 0
# type 1 : Europe based floor - 1

#Now, ask input from the user for the conversion of US floor to europe floor
us_floor = input("Enter the floor conversion value:\n")
europe_floor = int(us_floor) + 1
#print the conversion value from US to europe
print(f"The conversion value is {europe_floor}.")

#If the user want to convert back from europe floor conversion to us floor conversion
#us_floor = europe_floor - 1
#print the conversion value from europe to us
print(f"The conversion value is {us_floor}.")