from itertools import takewhile,permutations,product

def crackingPassword(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return sorted([ i for i in [createNumber(value) for value in list(product(digits,repeat=k))] if int(i)%d==0 ])
