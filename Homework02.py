from itertools import count

import random
N=int(input("How many sticks in the pile: "))
if N>0:
   print("There are",N,"sticks in the pile.")
   name=input("What is your name : ")
   c=1
   while N!=0:
       if c%2==1:
           print(name, ", how many sticks you will take (1 or 2): ", end="")
           t=int(input())
           if t==1 or t==2:
               N=N-t
               if N==0:
                   break
               print("There are",N,"sticks in the pile.")
           elif t>N:
               print("There are no enough sticks to take.")
           elif t==0:
               print(name," could take it out only 1 or 2.")
           elif t>2:
               print("No! ",name," can not take more than 2 sticks!")
           else:
               print("No! ",name," can not take less than 1 sticks!")
           c+=1
       else:
           if N>=2:
               T=random.randint(1,2)
               if T==1 or T==2:
                   print("I, smart computer,  takes :",T)
                   N=N-T
                   if N==0:
                       break
               print("There are",N,"sticks in the pile.")
               c+=1
           if N==1:
               T=1
               if T==1:
                   print("I, smart computer,  takes :",T)
                   N=N-T
               if N==0:
                   break
               print("There are",N,"sticks in the pile.")
               c+=1
   if c%2==1:
       
       print(name,", takes the last stick.")
       if c==1:
           print("OK. There is no stick left in the pile. We spent",c,"time together.")
       else:
           print("OK. There is no stick left in the pile. We spent",c,"times together.")
       print("I am smart computer and win  !!!!")
   else:
       print("I am smart computer and takes the last stick.")
       print("OK. There is no stick left in the pile. We spent",c,"times together.")
       print(name," win ( I am smart computer and am sad T_T)")
else:
  print("OK. You do not have to play with me TT^TT")
  