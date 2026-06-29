# # #control flow
# # print("Hello")
# # print("hello world")


# # marks = int(input("enter marks: "))
# # if marks >= 70:
# #     print("A Grade")
# # else:
# #     print("B Grade")


# #  #positive negative   
# # num = int(input("Enter number: "))
# # if(num > 0):
# #     print("positive")
# # elif(num == 0):
# #     print("zero")
# # else:
# #     print("negative")



# # #multiple 
# # num = int(input("Enter number: "))
# # if(num == 0):
# #     print("zero")
# # elif (num == 2):
# #     print("two")
# # elif (num == 5):
# #     print("five")
# # else:
# #     print("not found")



# # #nested
# #   age = int(input("Enter age: "))
# # if(age >= 18):
# #     if(age <= 40):
# #         print("you are eligible")

# # if(age >= 18 and age <= 40):
# #         print("you are eligible")



# #match
# # num = int(input("Enter number"))
# # match num:
# #     case 0:
# #         print("Zero")
# #     case 2:
# #         print("Two")
# #     case _:
# #         print("Not found")




# #loop c++
# # for(int i=0;i<50;i++){
# #     print("Jaswinder")
# # }
# # ending = value - 1

# # for i in range(10):
# #     print(i)


# # for i in range(10):
# #     print(i,end=" ")
# # starting value 
# # ending value 
# # step
# #even number
# # for i in range(0, 11, 2):
# #     print(i,end=" ")

# #while loop
# is_prime = True
# i = 1

# while(i <= 10):
#     print(i)
#     i += 1



# do while
# while True:
#     print(i)
#     i += 1
#     if(i>11):
#         print("yes")
#     else:
#         break


#jump statement 
# if i < 10:
#     pass
# * * * ---rows 
# * * *
# * * *
# num=int(input("Enter number: "))

# for i in range(0, num):  #rows 0 1 2
#     for j in range(num): #column
#         print("*",end=" ")
#     print()


#homework assingmnet
# *
# * *
# * * *
# * * * *
# for i in range(1, 5):
#     print("* " * i)


#largest among three
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a >= b and a >= c:
#     print("Largest number is:", a)
# elif b >= a and b >= c:
#     print("Largest number is:", b)
# else:
#     print("Largest number is:", c)



#factorial calculator********

#reverse multiplication
# n = int(input("Enter a number: "))

# for i in range(10, 0, -1):
#     print(n, "x", i, "=", n * i)

#pattern practice
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * *
# for i in range(5):
#     for j in range(5):
#         print("*", end=" ")
#     print()

#      *
#     * *
#    * * *
#   * * * *
#  * * * * * 
# for i in range(1, 6):
#     print(" " * (5 - i), "* " * i)

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
# 1 2 3 4 5 6 
# 1 2 3 4 5 6 7 
# 1 2 3 4 5 6 7 8 
# 1 2 3 4 5 6 7 8 9
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()