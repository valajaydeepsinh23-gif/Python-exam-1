print("welcome to the interactive personal detail collector !")

name = input("please enter your name:- ")

age = input("please enter your age:- ")

height = input("please enter your height in cm:- ")

favorite_number = input("please enter your favorite number:- ")

current_year = 2026

birth_year = current_year - int(age)

print("thank you! here is the information we collected:")

print(f"name:- {name} (type:- {type(name)})")

print(f"age:- {age} (type:- {type(age)})")

print(f"height:- {height} (type:- {type(height)})")

print(f"favorite number:- {favorite_number} (type:- {type(favorite_number)})")

print(f"birth year:- {birth_year}")

print("thank you for using personal data collector. Goodbye!")