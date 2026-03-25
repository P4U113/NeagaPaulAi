import random
print("stanga =1 si dreapta =0")
ct=0
list = ["Ai gasit comoara!!! Felicitari ai castigat!! ","Te-ai intalnit cu un urs si ai murit","Ai ajuns pe o campie continua aventura","Ai gasit o casa in padure si ai decis sa ramai peste noapte "]
lista=enumerate(list)
for i, val in lista:
    print(i,". ",val)

while(ct!=10):
 a = int(input("Alege urmatoarea directie: "))
 if(a==1):
    print("Ai mers la stanga")
 else:
    print ("Ai mers la dreapta")
 x=random.randint(0,3)
 if(x==0):
    print(list[0])  
 if(x==1):
    print(list[1])
    print("Ai murit")
    break
 if(x==2):
    print(list[2])
 if(x==3):
    print(list[3])
 ct=ct+1

