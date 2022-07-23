N=int(input("How many sticks in the pile: "))
if N>0:
  print("There are",N,"sticks in the pile.")
  name=input("What is your name :")
  x=1
  while N!=0:
    print(name, "how many sticks you will take (1 or 2): ", end="") 
    t=int(input())
    if t==1 or t==2:
      N=N-t
      if N==0:
        break
      print("There are",N,"sticks in the pile.")
      x+=1
    elif t>N:
      print("There are no enough sticks to take.")
    elif t==0:
      print("You could take it out only 1 or 2.")
    elif t>2:
      print("No! you can not take more than 2 sticks!")
    else:
      print("No! you can not take less than 1 sticks!")    
  if x==1:
    print("OK. There is no stick left in the pile. You spent",x,"time.")
  else:
    print("OK. There is no stick left in the pile. You spent",x,"times.")
else:
  print("OK. You do not have to play with me TT^TT")
  