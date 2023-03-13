l1 = [2,4,3]
lr1 = []
LfN = 0
LfN2 = 0
for el in range(len(l1)):
    #print (l1[el])
    lr1.append(l1[el])
lr1.reverse()
for el in range(len(lr1)):
    LfN = LfN*10 + lr1[el]
print ("LfN",LfN)
for el in range(len(l1)):
    LfN2 = LfN2*10 + l1[el]
print ("LfN2",LfN2)
if LfN == LfN2:
    print("Palindrome")
else:
    print("Not palindrome")
