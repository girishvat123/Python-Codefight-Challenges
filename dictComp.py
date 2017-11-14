def wordPower(word):
    num = dict([(chr(97+i),i+1) for i in  range(26)])
    return sum([num[ch] for ch in word])
