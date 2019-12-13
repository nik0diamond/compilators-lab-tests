LIST = "aaafbaaaaaffc%%aaa"

def list_of_elements(listing):
    elements = list(dict.fromkeys(listing))
    #print("The elements of list: " + str(elements))
    return elements

if __name__ == "__main__":
    n = 1
    repeat_count_list = []
    for i, j in enumerate(LIST[:-1]):
        if j == LIST[i+1]:
            n = n + 1
        else:
            repeat_count = {str(j): n}
            repeat_count_list.append(repeat_count)
            n = 1
            continue
    repeat_count = {str(j): n}
    repeat_count_list.append(repeat_count)

    keys_list = []
    for i in repeat_count_list:
        keys_list.append(list(i.keys()))

    answers = []
    for i in keys_list:
        dict_list = []
        for j in repeat_count_list:
            if i[0] in j:
                dict_list.append(j)
        seq = [x[i[0]] for x in dict_list]
        answers.append("The max value of " + str(i[0]) + " is " + str(max(seq)))

    for i in list_of_elements(answers):
        print(i)



