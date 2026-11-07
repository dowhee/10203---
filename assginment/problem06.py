password = "python123"
user_input = input("비밀번호를 입력하세요")
if user_input == password:
    print("로그인 성공! 환영합니다.")
while user_input != password:
     user_input = input("비밀번호가 틀렸습니다. 다시 입력하세요.")

     if user_input == password:
         print("로그인 성공! 환영합니다.")





