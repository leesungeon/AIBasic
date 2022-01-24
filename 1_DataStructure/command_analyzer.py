import csv

#정렬을 위한 함수
def getKey(item):
    return item[1]

#파일 읽어오기
command_data = []
with open("command_data.csv", "r", encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        command_data.append(row)

# dict 생성, 아이디를 key값, 입력줄수를 value값
command_counter = {}
for data in command_data:
    if data[1] in command_counter.keys():
        command_counter[data[1]] += 1
    else:
        command_counter[data[1]] = 1

#dict를 list로 변경
dictlist = []
for key, value in command_counter.items():
    temp = [key, value]
    dictlist.append(temp)

sorted_dict = sorted(dictlist, key=getKey, reverse=True)

# 상위 10개 값만 출력
print(sorted_dict[:10])