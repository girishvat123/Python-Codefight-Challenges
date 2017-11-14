from collections import Counter

def frequencyAnalysis(encryptedText):
    return list(Counter(encryptedText).most_common(1))[0][0]
