#Number Guessing Game
#Coder : Shivam Yadav
#Satyam Vs You

import os,random
 

class game:
 
 def __init__(self):
  self.rank=1
  self.name=yourname
  
 def byebye(self):
  os.system('clear')
  print("Thanks For Playing!".center(50))
 def cover(self,yourname):
  os.system('clear')
  print("-----------------------------")
  print("Number Guessing Game[1-20])")
  print("-----------------------------")
  print(f"Hello {yourname}")
  print("-----------------------------")

 def maingame(self):

#Computer generates a random number 
  rand_by_pc=random.randint(1,20)
  satyam_guess=0
  user_near=None
  satyam_near=None
  self.rank=0
  while True:
      
   if (user_near==None):
    pass
   elif (user_near==0):
    print("For Player : Guess Down")
   elif (user_near==1):
    print("For Player : Guess Upward")
   while True:
    try:
     user_guess=int(input("Guess a number[1-20] [quit-0] :"))
     break
    except:
     print("Hey Murkh Manab, Mughe Ek Number Do String Nahi")
  
   if(satyam_near==None):
    satyam_guess=random.randint(1,20)
   elif(satyam_near==0):
    satyam_guess=random.randint(1,satyam_guess)
   elif(satyam_near==1):
    satyam_guess=random.randint(satyam_guess,20)
#for value updataion of each time
   match user_guess : 
    case _ if rand_by_pc>user_guess :
     user_near=1
    case _ if rand_by_pc<user_guess :
     user_near=0
   match satyam_guess :
    case _ if rand_by_pc>satyam_guess :
     satyam_near=1
    case _ if rand_by_pc<satyam_guess :
     satyam_near=0
   self.rank +=1
   if(user_guess==0):
    break
   elif(user_guess==rand_by_pc):   
     if(satyam_guess==rand_by_pc):
      print(f"Your Guess : {user_guess}")
      print(f"Satyam Guess : {satyam_guess}")
      
      print(f"You and Satyam Won on {self.rank} times")
      print("---------------------------")      
      break
     elif(satyam_guess!=rand_by_pc):
      print(f"Your Guess : {user_guess}")
      print(f"Satyam Guess : {satyam_guess}")
      
      print(f"User Win on {self.rank} times and Satyam Loose")
      print("----------------------------")
      break
   elif(user_guess!=rand_by_pc):
     if(satyam_guess==rand_by_pc):
      print(f"User Guess : {user_guess}")
      print(f"Satyam Guess : {satyam_guess}")
      
      print(f"Satyam Won On {self.rank} times and You Loose ")
      print("----------------------------")
      break
     elif(satyam_guess!=rand_by_pc):
      print(f"Your Guess: {user_guess}")
      print(f"Satyam Guess: {satyam_guess}")
      print("Both are wrong.")
      print("----------------------------")
   
   
import os,random

yourname=input("Enter Your Name : ")
a=game()
a.cover(yourname)
while True:

 a.maingame()
 while True:
  confirm=3
  try:
   confirm=int(input("Wanna Play Again ? [ 1 for Yes, 0 for No] "))
   if confirm==0 or confirm==1 :
    break
  except:
   print("Hey Murkh Manab, 1 or 0 enter karo")

 
 if(confirm==0):
  break
os.system('clear')
a.byebye()

