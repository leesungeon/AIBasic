from xml.etree.ElementTree import Comment


sentence = "way a is there will a is there where"

def reverse_setence(stc):
    arr = stc.split(" ")
    arr.reverse()
    return " ".join(arr).capitalize()

print(reverse_setence(sentence))