from sys import exit
inp = input ()
msk = input ()

if len (msk) > len (inp):
    print (-1)
    exit()
pos = -1
for i in range (len(inp) - len(msk) + 1):
    fits = True
    for j in range (len(msk)):
        if (inp[i+j] != msk[j]) and (msk[j] != '@'):
            fits = False
            break
    if fits:
        pos = i
        break
print (pos)
