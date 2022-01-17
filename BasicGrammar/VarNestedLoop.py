import random

print("숫자를 맞춰보세요(1 ~ 100)")
rand_num = random.randint(1, 100)

number = int(input())

while(rand_num != number):
        if(rand_num > number):
            print("숫자가 너무 작습니다")
        elif(rand_num < number):
            print("숫자가 너무 큽니다.")
        else:
            break

        number = int(input())

print(f"정답입니다. 입력한 숫자는 {number}입니다.")
