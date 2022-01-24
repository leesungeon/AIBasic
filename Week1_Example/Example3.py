score = [(100, 100), (95, 90), (55, 60), (75, 80), (70, 70)]

def get_score(scores):
    for i, student_score in enumerate(scores, start=1):
        print("{0} 번, 평균 : {1}".format(i, sum(student_score) / 2))
#    for i in zip(*scores):
#        print(i)

get_score(score)