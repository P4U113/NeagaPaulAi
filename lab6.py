
import functools

# # initializing list
# lis = [1, 3, 5, 6, 2]

# # using reduce to compute sum of list
# print("The sum of the list elements is : ", end="")
# print(functools.reduce(lambda a, b: a + b, lis))

# # using reduce to compute maximum element from list
# print("The maximum element of the list is : ", end="")
# print(functools.reduce(lambda a, b: a if a > b else b, lis))


# n=input("introduceti un numar ")
# def fib(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# print(fib(int(n)))

# import random
#ex1

# b = input(" jucatorul 1 alege piatra, hartie sau foarfeca ")
# a=input(" jucatorul 2 alege piatra, hartie sau foarfeca ")
# if (a == b):
#     print("egalitate")
# elif (a == "piatra" and b == "foarfeca"):
#     print(" piatra bate foarfeca,jucatorul 2 a castigat")
# elif (a == "hartie" and b == "piatra"):
#     print(" hartie bate piatra,jucatorul 2 a castigat")
# elif (a == "foarfeca" and b == "hartie"):
#     print(" foarfeca bate hartie,jucatorul 2 a castigat")
# elif (a == "foarfeca" and b == "piatra"):
#     print(" piatra bate foarfeca,jucatorul 1 a castigat")
# elif (a == "piatra" and b == "hartie"):
#     print(" hartie bate piatra,jucatorul 1 a castigat")
# elif (a == "hartie" and b == "foarfeca"):
#     print(" foarfeca bate hartie,jucatorul 1 a castigat")

#ex 2

# nume=["ana":5,"maria":10,"ion":15]

# def genereaza_factura(**kwargs):

#     for key, value in kwargs.items():
#         print("%s == %s" % (key, value))

# genereaza_factura(first='B', mid='to', last='C')

# ex 4
# Fibonacci

square_list = lambda lst: [x*x for x in lst]
my_list = [1, 2, 3]
print(square_list(my_list))

