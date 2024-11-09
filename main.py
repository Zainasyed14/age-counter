try:
    print("Age Counter")
    age=int(input("Enter your age : "))
    print("The age is a valid integer")
except ValueError:
    print("Please enter an integer")
finally:
    print("I am ALWAYS here")
