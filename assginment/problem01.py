age = int(input("나이를 입력하세요"))
print(age)
if age < 8:
    print("무료입니다")
elif 8 <= age <= 19:
    print("10000원입니다")
elif 20 <= age <= 64:
    print("20000원입니다")
elif age > 64:
    print("5000원입니다")

