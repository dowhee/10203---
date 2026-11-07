arr = 1
while arr <= 30:
    if arr % 10 == 3:
        print("짝!")
        arr = arr + 1
    elif arr % 10 == 6:
        print("짝!")
        arr = arr + 1
    elif arr % 10 == 9:
        print("짝!")
        arr = arr + 1
    elif arr >= 30:
        print("짝!")
        break

    else:
        print(arr)
        arr = arr + 1




