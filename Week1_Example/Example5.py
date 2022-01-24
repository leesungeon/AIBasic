inputs = "cat32dog16cow5"

def find_string(input):
    input = list(input)
    word = ""
    output = []
    for str in input:
        if(str.isdigit()):
            if word != "": output.append(word); word = ""
        else: word += str
    return output

string_list = find_string(inputs)
print(string_list)