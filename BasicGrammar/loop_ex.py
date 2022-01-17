#EXAMPLE 1

i = 1
print("구구단 몇단을 계산할까요?")
num = int(input())
print(f"구구단 {num}단을 계산합니다.")

while i < 10:
    print(f"{num} x {i} = {num * i}")
    i += 1

#EXAMPLE 2

demical = int(input("십진수를 입력해주세요 : "))
result = ""

while demical > 0:
    remainder = demical % 2
    demical = demical // 2
    result = str(remainder) + result
    print(demical)
print(result)