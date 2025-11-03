import os,json,random
from helper1 import get_input
from colorama import Fore,Style,init
init(autoreset=True)
class manager:
 def __init__(self,file="rule.json"):
  self.file=file
  self.rules=self.load_rule()
 def load_rule(self):
  if os.path.exists(self.file): 
   with open(self.file,"r") as f:
    return json.load(f)
  else :
   return []
 
 def add_rule(self):
  rule=get_input("Command The Rule : ")
  category=get_input("Enter the valid Category : ")
  n=str(len(self.rules)+1)
  things={
        "rule_number":n,
        "rule":rule,
        "category":category,
          }
  self.rules.append(things)
  with open(self.file,"w") as f:
   json.dump(self.rules,f,indent=4)
  os.system('clear')
  print(Fore.WHITE+Style.BRIGHT+"_______________________________________")
  print(Fore.CYAN+Style.BRIGHT+"Successfully Added!")
  print(Fore.WHITE+Style.BRIGHT+"_______________________________________")
  c=input("Enter to continue...")
  os.system('clear')
 def delete_rule(self):
  index=get_input("Enter the rule number : ",int)
  del self.rules[index]
  with open(self.file,"w") as f:
   json.dump(self.rules,f,indent=4)
  os.system('clear')
  print(Fore.WHITE+Style.BRIGHT+"_______________________________________")
  print(Fore.CYAN+Style.BRIGHT+"Successfully Deleted!!")
  print(Fore.WHITE+Style.BRIGHT+"_______________________________________")
  c=input("Enter to continue...")
  os.system('clear')
 def show_random(self):
  r=random.randint(1,len(self.rules))
  for data in self.rules:
   if data.get("rule_number")==str(r):
    os.system('clear')
    print(Fore.WHITE + Style.BRIGHT + "\n" + "_" * 50)
    print(" ")
    print(Fore.CYAN + Style.BRIGHT + f"✨  SYSTEM  RULE {r}".center(40))
    print(Fore.WHITE +Style.BRIGHT + "_" * 50 + "\n")
    print(Fore.CYAN + Style.BRIGHT + f"{data.get('rule')}\n")
    print(Fore.WHITE +Style.BRIGHT + "_" * 50)
    input(Fore.WHITE + "\nPress [Enter] to continue... ")
    os.system('clear')
    break
  
 def first_time(self):
  os.system('touch rule.json')
  os.system('clear')
  print(Fore.WHITE+Style.BRIGHT+"_______________________________________")
  print(f"file{Style.BRIGHT+Fore.CYAN} rule.json{Style.RESET_ALL} created..")
  print(f"Current directory :{Style.BRIGHT+Fore.CYAN} {os.getcwd()}{Style.RESET_ALL}")
  print(Fore.WHITE+Style.BRIGHT+"_______________________________________")
  c=input("Enter to continue...")
  os.system('clear')
  
def main():
 obj=manager()
 while True:
  menu()
  response=get_input("Command The System : ",int)
  match response:
   case 1:
    obj.show_random()
   case 2:
    obj.add_rule()
   case 3:
    obj.delete_rule()
   case 402:
    obj.first_time()
   case 4:
    os.system('clear')
    print(Fore.WHITE+Style.BRIGHT+"Thanks From Certified Human".center(50))
    break
  os.system('clear')
def menu():
 os.system('clear')
 print(" ")
 print(Fore.WHITE+Style.BRIGHT+"_______________________________________")
 print(" ")
 print(Fore.CYAN +Style.BRIGHT+"SYSTEM  RULE".center(40))
 print(" ")
 print(Fore.WHITE+Style.BRIGHT+"Developer : Certified Human")
 print(Fore.WHITE+Style.BRIGHT+"_______________________________________")
 print(" ")
 print(Fore.CYAN+Style.BRIGHT+"1)Daily Reminder")
 print(Fore.CYAN+Style.BRIGHT+"2)Add New Rules")
 print(Fore.CYAN+Style.BRIGHT+"3)Delete Specific Rules")
 print(Fore.CYAN+Style.BRIGHT+"4)Exit")
 print(Fore.CYAN+Style.BRIGHT+"402)For First Time")
 print(" ")
 print(Fore.WHITE+Style.BRIGHT+"_______________________________________")
 


if __name__=="__main__":
 main()

