#반복문
#for -> 배열, data type
arr = ["apple", "banana", "cherry"]

print("과일 리스트")
for item in arr:
    print(item)
print("--------------------")
print("과일 리스트")
sale_list = {"apple": 1, "banana": 2, "cherry": 3}
for key in sale_list:
    if sale_list[key] == 0:
        print(key, "sold out")
    else:
        print(key, sale_list[key])

for i in range(10):
    print(i)
'''
# while문으로 실행하려면
a = 0
while a < 10:
    print(a)
    a += 1 # a = a + 1
'''



print("----------")
ex_arr = [num * 2 for num in range(10)]
print(ex_arr)