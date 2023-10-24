def neutralise(s1, s2):
    S = ""
    for char1,char2 in zip(s1,s2):
        if char1 == char2:
            S = S + char1
        else:
            S = S + "0"
    return S
S = neutralise("--++--","++--++")
print(f"{S}")
S = neutralise("-+-+-+","-+-+-+")
print(f"{S}")
S = neutralise("-++-","-+-+")
print(f"{S}")