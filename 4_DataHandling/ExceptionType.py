#IndexError / NameError / ZeroDivisionError / ValueError .... etc
for i in range(10):
    try:
        result = 10 // i
        print(result)
    except ZeroDivisionError:
        print("Not divided by 0")