def insertion_sert(l):
    for i in range(1, len(l)):
        value = l[i]
        while i>0 and l[i-1] > value:
            l[i] = l[i-1]
            i = i-1
        l[i] = value
    return l