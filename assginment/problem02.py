number1 = input("첫 번째 숫자")
number2 = input("두 번째 숫자")
opreator = input("연산자를 입력하세요")
if number1.isdigit() and number2.isdigit():
    if opreator == "+":
        print(int(number1) + int(number2))
    elif opreator == "-":
        print(int(number1) - int(number2))
    elif opreator == "*":
        print(int(number1) * int(number2))
    elif opreator == "/":
        print(int(number1) * int(number2))
else: print("잘못된 입력입니다")
