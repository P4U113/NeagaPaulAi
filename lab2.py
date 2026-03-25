import random
print("Bine ai venit la Loteria Python!" )
print("Alege 6 numere între 1 și 49.")
a=[]
b=[]
ct=0
k=1
for i in range(6):
    x = int(input(f"Introdu numarul {k} "))
    a.append(x)
    k=k+1

for i in range(6):
    x=random.randint(1,50)
    b.append(x)

for i in range(6):
    for j in range(6):
        if a[i]==b[j]:
         ct=ct+1

print(b)


print(ct)
if ct==3:
    print("ai castigat 3 numere")
if ct==4:
    print("ai castigat 4 numere")
if ct==5:
    print("ai castigat 5 numere")
if ct==6:
    print("ai castigat 6 numere")
if ct<3:
    print("ai pierdut")
