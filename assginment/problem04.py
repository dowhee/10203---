numbers = [12,7,19,20,33,42,8,15,26,31]
count = 0
for number in numbers:
    if number % 2 == 0:
        count = count + 1
        print("짝수:", number)
    else:
        count = count

print("짝수의 총 개수:",count )