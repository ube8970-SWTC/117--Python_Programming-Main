# List of owned trucks
owned_trucks = [
    "Red Chevy Silverado: 2002 3/4 ton",
# Nicknamed Clifford
    "Black Chevy Silverado: 2002 1/2 ton",
# Nicknamed Alice
    "White GMC Sierra: 2004 3/4 ton",
# Nicknamed Toolbox
    "White Chevy Tahoe: 2002 1/2 ton",
# Nicknamed Panda
    "Maroon Chevy Silverado: 2000 1/2 ton"
# Nicknamed Junior
# Nicknames matter due to line 25 
]

# Trucks parked at home
trucks_at_home = [truck for truck in owned_trucks]

# Display trucks at home
print("Trucks parked at home:")
for truck in trucks_at_home:
    print(f"  - {truck}")

# Allow user to enter which trucks are not home 
# Tried to add ability to use the trucks nicknames but it didn't work out and has been removed. Will revisit this feature in the future.
not_home_input = input("\nEnter trucks not at home (separated by commas): ")
not_home = [truck.strip() for truck in not_home_input.split(",") if truck.strip()]

# If no input was entered, use the automatic comparison instead
if not not_home:
    not_home = [truck for truck in owned_trucks if truck not in trucks_at_home]

# Show which trucks are not at home
print("\nTruck(s) not at home:")
for truck in not_home:
    if truck in owned_trucks:
        print(f"  - {truck}")
    else:
        print(f"  - {truck} (not in owned trucks)")