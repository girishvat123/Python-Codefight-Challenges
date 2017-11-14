def coolPairs(a, b):
    uniqueSums = { aa+bb for aa,bb in[(i,j) for i in a for j in b if (i*j)%(i+j)==0]}
    return len(uniqueSums)
