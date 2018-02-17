def ransom_note(magazine, ransom):
    """
    if the magazine has all words that are required to create ransom note, return true
        otherwise return false
    """
    magazine_history = {}
    for word in magazine:
        if word not in magazine_history.keys():
            magazine_history[word] = 1
        else:
            magazine_history[word] += 1
    for word in ransom:
        if word in magazine_history.keys():
            magazine_history[word] -= 1
            if magazine_history[word] < 0:
                return False
    return True

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
    