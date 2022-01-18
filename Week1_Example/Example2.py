sentence = "way a is there will a is there where"

def reverse_setence(stc):
    stc_arr = stc.split(" ")
    comment = ""
    for word in stc_arr:
        comment = word + " " + comment
    return comment.capitalize()

print(reverse_setence(sentence))