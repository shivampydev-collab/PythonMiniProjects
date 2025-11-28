import os,time,datetime,json
from helper import nm
from colorama import Fore,Back,init,Style
init(autoreset=True)
class ExpenseManager:
 def __init__(self,file): 
  self.file=file
  self.expenses=self.load_expenses()
 def load_expenses(self):
  if os.path.exists(self.file):
   with open(self.file,"r") as f:
    data=json.load(f)
    return data
  else:
   return []
    
 def save_expenses(self):
  with open(self.file,"w") as f:
   json.dump(self.expenses,f,indent=4)
  
 def add_expenses(self,amount,category,note):
  self.amount=amount
  self.category=category
  self.note=note
  now=datetime.datetime.now()
  things={
   
    "amount":self.amount,
    "category":self.category,
    "note":self.note,
    "year":now.year,
    "month":now.month,
    "date":now.day,
    }
  
  
    
  self.expenses.append(things)
  self.save_expenses()
 def view_expenses(self):
  def view_menu():
   print("_____________________________________________")
   print("1)Monthly Expense")
   print("2)Yearly Expense")
   print("_____________________________________________")
  def monthly():
   while True:
    try:
     y=int(input("Enter Year : "))
     break
    except:
     print("Invalid Year")
   while True:
    try:
     m=int(input("Enter Month[1-12] : "))
     break
    except:
     print("Invalid Month!")
   os.system('cls')   
   print("_____________________________________________")
   count=0
   total=0
   print(f" <----{nm(m)}----> ".center(50))
   print("_____________________________________________")
   for e in self.expenses:
    if e["month"]==m and e["year"]==y :
     count +=1
     total += e["amount"]
     print(f"{count}) Rs.{Fore.RED+Style.BRIGHT}{e["amount"]}{Style.RESET_ALL} • {e["category"]} • {e["note"]} | {e["year"]}-{e["month"]}-{e["date"]}")
   print("_____________________________________________")
   print(Fore.GREEN+Style.BRIGHT+f"Total Expenses Of {nm(m)} :{Fore.RED+Style.BRIGHT} {total}{Style.RESET_ALL}")
   print(Fore.WHITE+Style.BRIGHT+"_____________________________________________")
   r=input("Enter to continue...")
   os.system('cls')
  def yearly():
   while True:
    try:
     y=int(input("Enter Year : "))
     break
    except:
     print("Invalid Year!")
   os.system('cls')
   
   print(Fore.WHITE+Style.BRIGHT+"_____________________________________________")
   count=0
   total=0
   print(f"<----{y}---->".center(50))
   print("_____________________________________________")
   for e in self.expenses:
    if e["year"]==y:
     count +=1
     total += e["amount"]
     print(f"{count}) Rs.{Fore.RED+Style.BRIGHT}{e["amount"]}{Style.RESET_ALL} • {e["category"]} • {e["note"]} | {e["year"]}-{e["month"]}-{e["date"]}")
   print(Fore.WHITE+Style.BRIGHT+"_____________________________________________")
   print(f"Total Expenses Of Year {y} : {Style.BRIGHT+Fore.RED}{total}")
   print(Fore.WHITE+Style.BRIGHT+"_____________________________________________")
   r=input(Fore.GREEN+Style.BRIGHT+"Enter to continue")
   os.system('cls')
  def view_main():
   view_menu()
   while True:
    try:
     v_response=int(input("Enter Command : "))
     break
    except:
     print(Fore.RED+Style.BRIGHT+"Invalid Command!")
   match v_response :
    case 1:
     monthly()
    case 2:
     yearly()
  view_main()
 def delete_expenses(self,index):
  if index !=0:
   index=index-1
  try : 
   del self.expenses[index]
   print(Fore.GREEN+Style.BRIGHT+"Successfully Deleted.")
  except:
   print(Fore.RED+Style.BRIGHT+"Invalid Index")
  self.save_expenses()
 

def menu():
 os.system('cls')
 print(" ")
 print(Fore.WHITE+"_____________________________________________")
 print(" ")
 print(Fore.WHITE+Style.BRIGHT+"Expenses Tracker".center(45))
 print(" ")
 print(Fore.CYAN+Style.BRIGHT+"Developer : Certified Human")
 print(Fore.WHITE+"_____________________________________________")
 print(Fore.CYAN+Style.BRIGHT+"1)Add expense")
 print(Fore.CYAN+Style.BRIGHT+"2)View Expenses")
 print(Fore.CYAN+Style.BRIGHT+"3)Delete Expenses")
 print(Fore.CYAN+Style.BRIGHT+"4)Exit")
 print(Fore.CYAN+Style.BRIGHT+"402)For First Time")
 print(Fore.WHITE+"_____________________________________________")

def main():
 appdata=os.getenv("APPDATA")
 folder=os.path.join(appdata,"ExpenseManager")
 os.makedirs(folder,exist_ok=True ) 
 data_file=os.path.join(folder,"daily.json")
 me=ExpenseManager(file=data_file)
 while True:
  while True:
   try:
    response=int(input(Style.BRIGHT+"Enter Your Choice : "))
    break
   except:
    print(Fore.RED+Style.BRIGHT+"Invalid Command")
  match response:
   case 402:
    
    
    with open(data_file,"w") as f:
     f.write("[]")
    os.system('cls')
    print("__________________________________________")
    print(f"filename {Style.BRIGHT+Fore.CYAN}daily.json{Style.RESET_ALL} created on current directory. ")
    print(f"Directory : {Style.BRIGHT+Fore.CYAN} C:/Users/<name>/AppData") 
    print(Fore.WHITE+Style.BRIGHT+"__________________________________________")
    r=input("Enter to continue...")
    os.system('cls')
   case 1:
    while True:
     try:
      amount=int(input("Amount : "))
      break
     except:
      print("Invalid Amount")
    while True:
     try :
      category=input("Category : ")
      break
     except:
      print(Fore.RED+Style.BRIGHT+"Inavlid Category")
    while True:
     try:
      note=input("Any Notes : ")
      break
     except:
      print(Fore.RED+Style.BRIGHT+"Invalid Notes")
    os.system('cls')
    print("___________________________________________")
    me.add_expenses(amount,category,note)
    print(Fore.CYAN+Style.BRIGHT+"Added Successfully!")
    print("___________________________________________")
    r=input("Enter to continue...")
    os.system('cls')
   case 2:

    me.view_expenses()
    
   case 3:
    while True:
     print("___________________________________________")
     try:
      index=int(input("Enter the index[numbers]:"))
      break
     except:
      print(Fore.CYAN+Style.BRIGHT+"Invalid Index ")
    me.delete_expenses(index)
    os.system('cls')    
    print(Fore.CYAN+Style.BRIGHT+"Deleted SuccessFully!") 
    print(Fore.WHITE+Style.BRIGHT+"___________________________________________")
    r=input("Enter to continue...")
    os.system('cls')
   case 4:
    os.system('cls')
    print(Fore.CYAN+Style.BRIGHT+"Thanks From Certified Human".center(45))
    break
  menu()


if __name__ == "__main__":
 os.system('cls')
 menu()
 main()
