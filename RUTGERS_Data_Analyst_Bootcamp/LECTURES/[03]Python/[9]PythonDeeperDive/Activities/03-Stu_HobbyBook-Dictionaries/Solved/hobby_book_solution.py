# Dictionary full of info
my_info = {"name": "Wilian",
           "occupation": "Student",
           "age": 24,
           "hobbies": ["drawing", "coding", "gym", "guitar"],
           "wake-up": {"Mon": 8, "Friday": 5, "Saturday": 5, "Sunday": 5}}

# Print out results are stored in the dictionary
print(f'Hello I am {my_info["name"]} and I am a {my_info["occupation"]}')
print(f'I have {len(my_info["hobbies"])} hobbies!')
print(f'On the weekend I get up at {my_info["wake-up"]["Saturday"]}')
