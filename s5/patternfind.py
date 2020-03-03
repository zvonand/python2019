from sys import exit
inp, msk = input (), input()

if len (msk) > len (inp):
    print (-1)
    exit()
pos = -1
for i in range (len(inp) - len(msk) + 1):
    for j in range (len(msk)):
        if (inp[i+j] != msk[j]) and (msk[j] != '@'):
            break
    else:
        pos = i
        break
print (pos)
