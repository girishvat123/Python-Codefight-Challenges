def pressureGauges(morning, evening):
    return map(lambda x,y:min(x,y),morning ,evening),map(lambda x,y:max(x,y),morning ,evening)
