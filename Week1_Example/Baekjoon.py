#a, b = map(int, input().split())
a = int(input())

for i in range(1, a+1):
    print(" " * (a - i) + "*" * i)