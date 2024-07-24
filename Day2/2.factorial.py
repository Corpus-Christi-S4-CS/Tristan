def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    number = int(input("Enter a number to calculate the factorial: "))
    print("Factorial:", factorial(number))

main()