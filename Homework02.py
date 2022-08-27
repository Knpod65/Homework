import random # call module of random to use on this
N=int(input("How many sticks in the pile: ")) #number of sticks in pile
def prc(N, T): #define oncomputer turn what it plays.
    print("I, smart computer,  takes :",T) 
    N=N-T #set leftovers
    return N

if N>0: #check sticks to start
   print("There are",N,"sticks in the pile.")
   name=input("What is your name : ")
   print("---------------------------------")
   c=0 #set how many time to play that begin on zero (count)
   while N!=0: #play on if it is not enough.
       if c%2!=1: # if time to play is even, computer will play "first" 
            if N==1 or N==2 or (N>=5 and (N-4)%3==1): #logic in game if computer must pick only 1 stick
                T=1 #how many that you take it off (take)
                N = prc(N, T) #recall function of prc
            elif N==3 or (N>=6 and (N-4)%3==2): #logic in game if computer must pick 2 sticks
                T=2
                N = prc(N, T) #recall function of prc
            elif N==4 or (N>=7 and (N-4)%3==0): #on the another hand computer will random
                T=random.randint(1,2)
                if T==1 or T==2: #check rule of game
                    N = prc(N, T) #recall function of prc
            elif N==0: #Check to see if it's all left
                print("\n")
                break # finish of while loop
            if N >=2: #scan to see amount of sticks in pile left if it is more than 2 sticks, it will show...
                print("There are",N,"sticks in the pile.\n")
            else: #scan to see amount of sticks in pile left if it is only 1 stick, it will show...
                print("There are",N,"stick in the pile.\n")
            c+=1 #add how many times play on this game
       else: # if time to play is odd, player will play
           re=0 #set condition of how to player pick stick (redo)
           while re==0:  #this make to player picks again if It's not on condition, player will return to pick it again
                print(name, ", how many sticks you will take (1 or 2): ", end="")
                t=int(input()) #input the sticks is picked out by the player
                if t==1 or t==2: #check rule of game
                    N=N-t #set leftovers
                    re=1 #condition is True 
                    c+=1 #add how many times play on this game
                    if N==0: #Check to see if it's all left
                        print("\n")
                        break # out of while loop
                    if N >=2: #scan to see amount of sticks in pile left if it is more than 2 sticks, it will show...
                        print("There are",N,"sticks in the pile.\n")
                    else: #scan to see amount of sticks in pile left if it is only 1 stick, it will show...
                        print("There are",N,"stick in the pile.\n")
                elif t>N: #look over on count of sticks is picked more than leftovers
                    print("There are no enough sticks to take.\n")
                    re=1 #condition is True
                elif t==0: #check player who don't take it off
                    print(name," could take it out only 1 or 2.\n")
                    re=0 #condition is False 
                elif t>2: #monitor player who takes more than 2 sticks
                    print("No! ",name," can not take more than 2 sticks!\n")
                    re=0 #condition is False
                else: #anything else!
                    print("No! ",name," can not take less than 1 sticks!\n")
                    re=0 #condition is False
   if c%2==0: #assumtion of player
       print(name,", takes the last stick.")
       if c==1: #check time be used
           print("OK. There is no stick left in the pile. We spent",c,"time together.")
       else: #opposite there condition
           print("OK. There is no stick left in the pile. We spent",c,"times together.")
       print("I am smart computer and win  !!!!")
   else: #finally! if computer win, it will show...
       print("I am smart computer and takes the last stick.")
       print("OK. There is no stick left in the pile. We spent",c,"times together.")
       print(name," win ( I am smart computer and am sad TT_TT)")
else: #if number of stick is nonsense will show this
  print("OK. You do not have to play with me TT^TT")
  