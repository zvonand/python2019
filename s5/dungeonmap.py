weg = {}            #{"name" : set(_where_to_go_)}
inp = input()

while " " in inp:
    p = inp.split()
    if p[0] in weg.keys():
        weg[p[0]].add(p[1])
    else:
        weg[p[0]] = set([p[1]])

    if p[1] in weg.keys():
        weg[p[1]].add(p[0])
    else:
        weg[p[1]] = set([p[0]])

    inp = input()

entr, ext = inp, input()


access = weg[entr]
modified = True
while weg and modified:
    if ext in access:
        break
    modified = False
    for i in access.copy():
        if i in weg.keys():
            access.update(weg[i])
            weg.pop(i)
            modified = True

if ext in access:
    print ("YES")
else:
    print("NO")
