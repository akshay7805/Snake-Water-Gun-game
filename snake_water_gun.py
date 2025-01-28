import random
def check(user,comp):
  if(comp==user):
    return 0
  if comp==0 and user==1:
    return -1
  if comp==1 and user==2:
    return -1
  if comp==2 and user==0:
    return -1
  return 1  
 


user=int(input("0 for Snake,1 for Water and 2 for Gun:"))
comp=random.randint(0,2)
print("You:", user)
print("Computer:", comp)  
score=check(user,comp)
if(score==0):
  print("Draw")
if(score==-1):
  print("You loose")
if(score==1):
  print("You Win ")