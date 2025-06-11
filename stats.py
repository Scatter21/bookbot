def count_words(text):
    return len(text.split())

def char_counter(text):
    char_dict = {}
    for char in text.lower():
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def dic_sorter(dic):
    dic_list=[]
    for entry in dic:
        new_dic = {}
        if entry.isalpha():
            new_dic["char"] = entry
            new_dic["num"] = dic[entry]
            dic_list.append(new_dic)
    dic_list.sort(reverse=True, key = lambda new_dic: new_dic["num"])
    return dic_list