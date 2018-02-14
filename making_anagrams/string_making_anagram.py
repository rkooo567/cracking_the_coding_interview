def number_needed(a, b):
    # save data in the dictionary
    a_dic = lst_to_dic(list(a))
    b_dic = lst_to_dic(list(b))
    for key in a_dic.keys():
        # subtract the appearance of common words
        a_dic[key], b_dic[key] = subtract_min_num(a_dic[key], b_dic[key]), subtract_min_num(b_dic[key], a_dic[key])
    deletion = 0
    for a_element in a_dic.keys():
        deletion += a_dic[a_element]
    for b_element in b_dic.keys():
        deletion += b_dic[b_element]
    return deletion

def lst_to_dic(lst):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    dic = {}
    for letter in letters:
        dic[letter] = 0
    for element in lst:
        if element in dic.keys():
            dic[element] +=1
    return dic
                
def subtract_min_num(a, b):
    """ subtract the minimum number of a and b"""
    return abs(a - min(a, b))

a = input().strip()
b = input().strip()

print(number_needed(a, b))
