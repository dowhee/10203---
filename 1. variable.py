고윤정 = 422

print(고윤정)

고윤정= "고윤정"
print(고윤정)

a= 123+123
print(a)

a=[123, "hi", 523]
print(a)

고윤정=422
김도휘=829
a=고윤정+김도휘
print(a)

input_var = input("숫자를 입력하세요")
print(input_var)

# dictionary: {key1: value1}

questions1 = {"no":1, "question" : "답을 구하여라" , "answer":422, "score": 5, "isMultipleChoice":False}

print("questions 1의 답은" ,questions1["answer"])


# 배열은 0부터 시작
questions = [{"no":2, "question" : "답으로 올바른 것을 고르시오" , "answer":422, "score": 3, "isMultipleChoice":True, "example": [50, 30, 35, 20, 40]},
             {"no":3, "question" : "답을 구하여라" , "answer":422, "score": 4, "isMultipleChoice":False},
             {"no":4, "question" : "답을 구하여라" , "answer":422, "score": 4, "isMultipleChoice":False}]

print(questions[0])
print(questions[0]["example"][0])