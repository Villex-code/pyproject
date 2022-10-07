def reduction_for_now(x,mod):
    return x % mod

def remove_uneeded_zeros(mylist):
    counter = -1
    while True:
        if mylist[counter] == 0 and len(mylist) > 1:
            mylist.pop(counter)
        else:
            break 
    return mylist

def poly_multiplication(p1,p2,mod):
    # p1 and p2 are lists
    final = [0] * (len(p1) + len(p2))
    p1_c = 0
    for i in p1:
        p2_c = 0
        for j in p2:
            final[p1_c + p2_c] += i * j
            p2_c += 1
        p1_c += 1
    
    for i in range(len(final)):
        final[i] = reduction_for_now(final[i],mod)
    
    final = remove_uneeded_zeros(final)
    
    return final
        

g = [
        6,
        1,
        2,
        4,
        5,
        4
    ]

f = [
        6,
        2,
        2
    ]

print(poly_multiplication(f,g,7))