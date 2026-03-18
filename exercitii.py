
#Tricky picture:
picture = [
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0]]
i=0
while(i!=6):
    print(picture[i])
    i=i+1


#ex 2

a=input("introduceti nota ")
a=int(a)
if(a>0 and a<11):
    if(a>=9 and a<= 10):
        print("excelent")
    if (a >= 7 and a < 9):
        print("bine")
    if (a >= 5 and a < 7):
            print("suficient")
    if (a < 5):
            print("reex")

else :
    print("introsuceti O nota in intervalul 1,10")

#ex3
import random
a=random.randint(1,50)
print(a)
ct=0
while(ct!=4):
    ct = ct + 1
    if (ct > 3):
        print("ai pierdut")
        break
    y = input("introdu numarul ")
    y = int(y)
    if(a==y) :
        print(f"ai ghicit din  {ct} incercari")
        break
    if(a>y):
        print("mai mare")
    if(a < y):
        print("mai mic")

#ex 4
i=1
list = ["sibiu","bucuresti","deva","apold"]
lista=enumerate(list)
for i, val in lista:
    print(i,". ",val)