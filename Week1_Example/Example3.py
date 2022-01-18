score = [(100, 100), (95, 90), (55, 60), (75, 80), (70, 70)]
student_score = [0, 0]

def get_score(scores):
    for student_score in scores:
        i = 0
        for subject in student_score:
            i += subject
        print(f"{scores.index(student_score) + 1}번, 평균 : {i / 2}")

get_score(score)