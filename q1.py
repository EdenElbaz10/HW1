def trifeca(word: str) ->bool:
    l = len(word)
    if l >= 6:
        x = 0
        for i in range(0, l-1, 2):
            if word[i] == word[i + 1]:
                x += 1
            else:
                x = 0
            if x == 3:
                return True
        x = 0
        for i in range(1, l-1, 2):
            if word[i] == word[i + 1]:
                x += 1
            else:
                x = 0
            if x == 3:
                return True
    return False

print(trifeca('taabbcdd'))



