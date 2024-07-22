#Pyramids

def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0 and value <= 8:
                return value
            else:
                print("Please enter a positive integer between 1 and 8.")
        except ValueError:
            print("Please enter a valid integer.")

def print_pyramid(height):
    for i in range(1, height + 1):

        print(" " * (height - i), end="")

        print("#" * i, end="")
    
        print("  ", end="")
        
        print("#" * i)

def main():
    height = get_int("Height of the half-pyramids: ")
    print_pyramid(height)


main()