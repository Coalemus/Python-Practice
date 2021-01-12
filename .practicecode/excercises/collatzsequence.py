def collatz(number):
    while number > 1:
        if number % 2 == 0:
            return number // 2
        elif number % 2 == 1:
            return 3 * number + 1


data = int(input("Enter number: "))

try:
    collatz(data)
except ValueError as er:
    print("Please enter an integer.")
