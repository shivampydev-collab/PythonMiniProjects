from datetime import datetime
def string_input(prompt,data_type=str,msg="Invalid Input!"):
 while True:
  try : 
   print(prompt)
   a = input().strip()
   if a!= "":
    return a
    
  except : 
   print(msg)
def number_input(prompt,msg="Invalid Input!",compare=0):
 while True :
  try:
   print(prompt)
   n=input().strip()
   n=float(n)
   if n>=compare:
    return n
   else:
    print("Inavlid Input!")
   
  except : 
   print("Invalid Input!")

def interval():
 while True :
  try :  
   start_date_str=input("Starting Date AD  [YYYY-MM-DD] : ").strip()
   end_date_str=input("Ending Date AD [YYYY-MM-DD] : ").strip()
   start_date=datetime.strptime(start_date_str,"%Y-%m-%d")
   end_date=datetime.strptime(end_date_str,"%Y-%m-%d")
   if end_date < start_date : 
    print("Ending Date should be greater than Starting Date!")
    continue
   else :
    break
  except ValueError: 
   print("Invalid Date! Enter Value in YYYY-MM-DD FORMAT : ")
 tup=(start_date_str,end_date_str)
 return tup
