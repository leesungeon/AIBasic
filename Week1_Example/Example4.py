dict_first = {'사과' : 30, '배' : 15, '감': 10, '포도': 10}
dict_second = {'사과' : 5, '배' : 15, '감': 25, '귤': 25}

def merge_dict(first, second):
    for key_f in first:
        for key_s in second:
            if key_f == key_s : first[key_f] += second[key_s]
    second.update(first)
    second = dict(sorted(second.items()))
    print(second)

merge_dict(dict_first, dict_second)
