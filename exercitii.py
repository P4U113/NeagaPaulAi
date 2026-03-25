
# #Tricky picture:
# picture = [
# [0,0,0,1,0,0,0],
# [0,0,1,1,1,0,0],
# [0,1,1,1,1,1,0],
# [1,1,1,1,1,1,1],
# [0,0,0,1,0,0,0],
# [0,0,0,1,0,0,0]]
# i=0
# while(i!=6):
#     print(picture[i])
#     i=i+1


# #ex 2

# # a=input("introduceti nota ")
# # a=int(a)
# # if(a>0 and a<11):
# #     if(a>=9 and a<= 10):
# #         print("excelent")
# #     if (a >= 7 and a < 9):
# #         print("bine")
# #     if (a >= 5 and a < 7):
# #             print("suficient")
# #     if (a < 5):
# #             print("reex")

# # else :
# #     print("introsuceti O nota in intervalul 1,10")

# #ex3
# import random
# a=random.randint(1,50)
# print(a)
# ct=0
# while(ct!=4):
#     ct = ct + 1
#     if (ct > 3):
#         print("ai pierdut")
#         break
#     y = input("introdu numarul ")
#     y = int(y)
#     if(a==y) :
#         print(f"ai ghicit din  {ct} incercari")
#         break
#     if(a>y):
#         print("mai mare")
#     if(a < y):
#         print("mai mic")

# #ex 4
# i=1
# list = ["sibiu","bucuresti","deva","apold"]
# lista=enumerate(list)
# for i, val in lista:
#     print(i,". ",val)

# #ex5
# import random

# #exercitiul 5
# print("Bine ai venit la Loteria Python!" )
# print("Alege 6 numere între 1 și 49.")
# a=[]
# b=[]
# ct=0
# k=1
# for i in range(6):
#     x = int(input(f"Introdu numarul {k} "))
#     a.append(x)
#     k=k+1

# for i in range(6):
#     x=random.randint(1,50)
#     b.append(x)

# for i in range(6):
#     for j in range(6):
#         if a[i]==b[j]:
#          ct=ct+1

# print(b)


# print(ct)
# if ct==3:
#     print("ai castigat 3 numere")
# if ct==4:
#     print("ai castigat 4 numere")
# if ct==5:
#     print("ai castigat 5 numere")
# if ct==6:
#     print("ai castigat 6 numere")
# if ct<3:
#     print("ai pierdut")

# #ex6
# import random
# print("stanga =1 si dreapta =0")
# ct=0
# list = ["Ai gasit comoara!!! Felicitari ai castigat!! ","Te-ai intalnit cu un urs si ai murit","Ai ajuns pe o campie continua aventura","Ai gasit o casa in padure si ai decis sa ramai peste noapte "]
# lista=enumerate(list)
# for i, val in lista:
#     print(i,". ",val)

# while(ct!=10):
#  a = int(input("Alege urmatoarea directie: "))
#  if(a==1):
#     print("Ai mers la stanga")
#  else:
#     print ("Ai mers la dreapta")
#  x=random.randint(0,3)
#  if(x==0):
#     print(list[0])  
#  if(x==1):
#     print(list[1])
#     print("Ai murit")
#     break
#  if(x==2):
#     print(list[2])
#  if(x==3):
#     print(list[3])
#  ct=ct+1


