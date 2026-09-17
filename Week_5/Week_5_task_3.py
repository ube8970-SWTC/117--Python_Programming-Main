# multiple text assignment 
# listed in plain text format, csv format, and json format

name, age, city = "John Doe", 30, "New York"
# text example I will be using for the assignment

import json

print(json.dumps({"name": name, "age": age, "city": city}))
# json format

print(f"Name: {name}, Age: {age}, City: {city}")
# plain text format

print(f"{name}, {age}, {city}")
# csv format

# I think the plain text and csv formats are more readable and easier to understand for people, while the json format is more structured and better suited for data interchange between systems.
# I think the json format is more difficult to read and understand because it uses brackets and quotes. However it is more structured and can be easily read by machines. 
# A larger application may require the use of json format for data storage and retrieval, while a smaller application may be able to get by with plain text or csv formats.