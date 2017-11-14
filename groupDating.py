def groupDating(male, female):
    return [[i for i,j in zip(male,female) if  i!=j],[j for i,j in zip(male,female) if  i!=j]]
