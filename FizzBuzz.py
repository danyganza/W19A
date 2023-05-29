import random

def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")

# list of random numbers
numbers = random.sample(range(1, 101), 15)

# Call the fizz_buzz function to show each number in the list
for number in numbers:
    fizz_buzz(number)

