# List of owned trucks
owned_trucks = [
    ("Red Chevrolet Silverado: 2002 3/4 ton", "Clifford"),
    ("Black Chevrolet Silverado: 2002 1/2 ton", "Alice"),
    ("White GMC Sierra: 2004 3/4 ton", "Toolbox"),
    ("White Chevrolet Tahoe: 2002 1/2 ton", "Panda"),
    ("Maroon Chevrolet Silverado: 2000 1/5 ton", "Junior")
]

# Trucks parked at home
    [truck for truck, owner in owned_trucks if owner in ["Clifford", "Alice", "Toolbox", "Panda"]]
    truck for truck, owner in owned_trucks if truck in [t[0] for t in owned_trucks if t[1] in ["Clifford", "Alice", "Toolbox", "Panda"]]
]

# Display trucks at home
print("Trucks parked at home:")
for truck in trucks_at_home:
    print(f"  - {truck}")

# Allow user to enter which trucks are not home
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

