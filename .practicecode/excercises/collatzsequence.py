def collatz(number):
    while number > 1:
        if number % 2 == 0:
            evenres = print(number // 2)
        elif number % 2 == 1:
            oddres = print( 3 * number + 1)

data = int(input("Enter number: "))



collatz(data)


