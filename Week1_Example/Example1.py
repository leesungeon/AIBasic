def get_odd_num(numList):
    arr = []
    for number in numList:
        if number % 2 == 1 :
            arr.append(number)
    return arr

num_list = [1, 5, 7, 15, 16, 22, 28, 29]

print(get_odd_num(num_list))