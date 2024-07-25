array = [12,76, 3, 4, 35, 2, 10, 8 ]
print(array)

for i in range (len(array)-1):
    print(array[i], "compated to ", array[i+1])
    if array[i] > array[i+1]:
        array[i], array[i+1] = array[i+1], array[i]
        print("swapped array", array)
    print("partially sorted array:")
    print(array)

    #Repeat to properly sort

for i in range (len(array)-1):
    print(array[i], "compated to ", array[i+1])
    if array[i] > array[i+1]:
        array[i], array[i+1] = array[i+1], array[i]
        print("swapped array", array)
    print("partially sorted array:")
    print(array)

for i in range (len(array)-1):
    print(array[i], "compated to ", array[i+1])
    if array[i] > array[i+1]:
        array[i], array[i+1] = array[i+1], array[i]
        print("swapped array", array)
    print("partially sorted array:")
    print(array)

for i in range (len(array)-1):
    print(array[i], "compated to ", array[i+1])
    if array[i] > array[i+1]:
        array[i], array[i+1] = array[i+1], array[i]
        print("swapped array", array)
    print("partially sorted array:")
    print(array)