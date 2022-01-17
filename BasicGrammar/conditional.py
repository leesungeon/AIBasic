# BASIC 1

print("Tell me your age?")
myage = int(input())
if myage < 30:
    print("Welcome to the Club")
else:
    print("Oh! No. You are not accepted.")

# EXAMPLE 1

print("당신이 태어난 년도를 입력하세요")
year = int(input())
age = 2021 - year + 1
if(age >= 20 and age <= 26):
    print("대학생")
elif(age >= 17 and age < 20):
    print("고등학생")
elif(age >= 14 and age < 17):
    print("중학생")
elif(age >= 8 and age < 14):
    print("초등학생")
else:
    print("학생이 아닙니다")