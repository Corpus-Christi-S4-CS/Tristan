fibonacci = [0, 1]

while True:
    next_number = fibonacci[-1] + fibonacci[-2]
    if next_number > 1000:
        break
    fibonacci.append(next_number)

print(fibonacci)
