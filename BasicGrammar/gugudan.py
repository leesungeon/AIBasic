print("구구단 몇 단을 계산할까요(1~9)?")
dan = int(input())
i = 1

while(dan != 0):
    while(i < 10):
        print(f"{dan} x {i} = {dan * i}")
        i += 1
    print("구구단 몇 단을 계산할까요(1~9)?")
    dan = int(input())
    i = 1
print("구구단 게임을 종료합니다.")