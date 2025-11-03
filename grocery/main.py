import sqlite3,datetime,os
from helper import number_input,string_input,interval
con=sqlite3.connect('data.db')
cursor=con.cursor()
 
class Products_Sales_Manager:
 def __init__(self):
  pass
 def first_time(self):
  """
  This function creates two tabeles(products,sales).
  \n Call this function for initialization
  
  """
  #create products table 
  cursor.execute("""
   CREATE TABLE IF NOT EXISTS products( 
   product_id INTEGER PRIMARY KEY
   AUTOINCREMENT,
   product_name text,
   category text,
   cost_price INTEGER,
   stock INTEGER  
     )
    """)
  con.commit()
  # create sales table 
  cursor.execute("""
   CREATE TABLE IF NOT EXISTS sales( 
   sale_id INTEGER PRIMARY KEY
   AUTOINCREMENT,
   product_id INTEGER,
   quantity_sold INTEGER,
   sale_rate INTEGER,
   date text,
   FOREIGN KEY (product_id) REFERENCES products(product_id)
  
     )
    """)
  con.commit()
  print("_"*60)
  print("File data.db created on your cwd.")
  print("SuccessFully Installed!")
  print("_"*60)
 def add_products(self):
  """
  This function adds the details of products to table products.  
  """
  print(" ")
  print("_"*40)
  n=number_input("How many products you want to add ? ")
  print("_"*40)
  products=[]
  for a in range(int(n)):
   print(f"Product {a+1}".center(36))
   print("_"*40)
   product_name=string_input("Name Of Product : ").lower()
   cost_price=number_input("Cost Price Of Product[each] : ")
   entered_stock=number_input("Number Of stocks  : ")
   cursor.execute("""
     SELECT product_id,stock 
     FROM products
     WHERE product_name=? AND cost_price=?  
      """,(product_name,cost_price))
   result=cursor.fetchone()
   if result:
    product_id,current_stock=result
    new_stock=current_stock+entered_stock
    cursor.execute("""
     UPDATE products
     SET stock=?
     WHERE product_id=?
      """,(new_stock,product_id,))
    print("_"*40)
    print("Product Stock Updated.")
    print("_"*40)
   else : 
    category=string_input("Category Of Product : ")
    print("_"*40)
     
    tup=(product_name,category,cost_price,entered_stock)
    products.append(tup)
    cursor.execute("""
     INSERT INTO products(product_name,category,cost_price,stock)
     VALUES(?,?,?,?) 
       """,tup)
    print("Product Added!")
    print("_"*40)
  con.commit()

 def add_sales(self):
  """
  This function add sales details to table sales.
  """
  print("")
  print("_"*40)
  n=number_input("How many sales you want to add : ")
  print("_"*40)
  for a in range(int(n)):
   print(f"Sales {a+1}".center(36))
   print("_"*40)
   product_id=number_input("Product ID : ")
   quantity_sold=number_input("Quantity Sold  : ")
   sale_rate=number_input("Rate : ")
   print("_"*40)
   now=datetime.datetime.now()
   date=f"{now.year}-{now.month}-{now.day}"
   cursor.execute(""" 
    SELECT products.stock from products
    WHERE product_id=?
      """,(product_id,))
   result=cursor.fetchone()
   if not result :
    print(f"Product Id with {product_id} not found!")
    print("_"*40)
    continue
   current_stock=result[0]
   if current_stock>=quantity_sold:
    new_stock=current_stock-quantity_sold
    cursor.execute(""" 
     UPDATE products
     SET stock=?
     WHERE product_id=?
     
     """,(new_stock,product_id,))
    sales=(product_id,quantity_sold,sale_rate,date,)
    cursor.execute("""
     INSERT INTO sales(product_id,quantity_sold,sale_rate,date)
     VALUES(?,?,?,?)
      """,sales)
    con.commit()
   else : 
    print(f"Not available stock for Product ID.{int(product_id)} ! \n Available stock : {current_stock}!")
    print("_"*40)
class View_Manager:
 def __init__(self):
  pass
 def view_one(self):
  """
  
  This function is normal view of sales and product table.\n
  Here,we combine both tables and show required columns .
  This filters :
   1)Single Product Or All Product
   2)Order By Oldest or Newest
   3)All Sales till now 
  """
  t=string_input("Single Product or All Product [S/A] : ")
  if t.upper()=="A":
   sql=" "
   params=()
  elif t.upper()=="S":
   id=number_input("Product ID : ")
   sql="WHERE products.product_id=?"
   params=(id,)
  order=string_input("Order by (newest/oldest) : ")
  if order.lower()=="newest":
   order_by="ASC"
  elif order.lower()=="oldest":
   order_by="DESC"
  else :
   print("Invalid Order!\nDirecting to newest.")
   order_by="DESC"
  cursor.execute(f"""
   SELECT products.product_id,products.product_name,sales.quantity_sold,
    sales.sale_rate,(sales.quantity_sold*sales.sale_rate) AS total_amount,
    sales.date   
   FROM products
   INNER JOIN sales ON products.product_id=sales.product_id
   {sql}
   ORDER BY sales.date {order_by}
   
     """,params)
  rows=cursor.fetchall()
  print("_"*85)
  print("Product_Id | Products            |   SOLD  |   RATE  |  AMOUNT  |   DATE    ")
  print("_"*85)
  grand_total =0
  if not rows:
   print("No records found!")
   print("_"*85)
   return
  for row in rows:
   product_id,product_name,quantity_sold,sale_rate,total_amount,date=row
   print(f"{product_id:<10} | {product_name:<20} | {quantity_sold:<6} | {sale_rate:<8} | {total_amount:<8} | {date:<12}")
   grand_total += total_amount
  print("_"*85)
  print(f"Total Amount : Rs.{grand_total}")
  print("_"*85)
  
 def view_two(self):
  """
  This view function filters : 
   1)Date Interval
   2)Oldest/Newest

  """
  
  order=string_input("Order by (newest/oldest) : ")
  tup=interval()
  start_date=tup[0]
  end_date=tup[1]
  params=(start_date,end_date)
  if order.lower()=="newest":
   order_by="ASC"
  elif order.lower()=="oldest" :
   order_by="DESC"
  else : 
   print("Invalid Order!\nDirecting to newest.")
   order_by="DESC"
  cursor.execute(f"""
    SELECT products.product_id,products.product_name,sales.quantity_sold,
     sales.sale_rate,(sales.quantity_sold*sales.sale_rate) AS total_amount,
     sales.date
     FROM products
    INNER JOIN sales ON products.product_id=sales.product_id
     WHERE  sales.date BETWEEN ? AND ?

     ORDER BY sales.date {order_by}
      """,params)
  rows=cursor.fetchall()
  print("_"*85)
  print("Product_Id | Products        | SOLD |  RATE   | AMOUNT |   DATE       ")
  print("_"*85)
  grand_total =0
  if not rows:
   print("No records found!")
   print("_"*85)
   return
  for row in rows:
   product_id,product_name,quantity_sold,sale_rate,total_amount,date=row
   print(f"{product_id:<10} | {product_name:<15} | {quantity_sold:<4} | {sale_rate:<8} | {total_amount:<7} | {date}")
   grand_total += total_amount 
  print("_"*85)
  print(f"Total Amount : Rs.{grand_total}")
  print("_"*85)
  
 def view_four(self):
  """
   This will filter :
   1)Most sold products based on total revenue or quantity sold.
   2)Date Interval
   
  """
  
  tup=interval()
  start_date=tup[0]
  end_date=tup[1]
  params=(start_date,end_date)
  t=string_input("Most Sold Product Filter[quantity/revenue] : ")
  if t.lower()=="quantity":
   t="total_sold"
  elif t.lower()=="revenue":
   t="total_revenue"
  else : 
   print("Invalid Input!\n Redirecting to quantity!")
   t="total_sold"
    
  cursor.execute(f""" 
     SELECT products.product_id,products.product_name,SUM(sales.quantity_sold) AS total_sold,
     SUM(sales.sale_rate*sales.quantity_sold) AS total_revenue 
     FROM products
     INNER JOIN sales ON  sales.product_id=products.product_id
     WHERE sales.date BETWEEN ? AND ?
     GROUP BY products.product_id,products.product_name 
     ORDER BY {t} DESC
     
         """,params)
  rows=cursor.fetchall()
  grand_total =0
  print("_"*60)
  print("PRODUCT_ID | PRODUCT_NAME     | SOLD     | TOTAL REVENUE ")
  print("_"*60)
  if not rows:
   print("No records found!")
   return
  for row in rows:
   product_id,product_name,total_sold,total_revenue=row
   grand_total += total_revenue
   print(f"{product_id:<10} | {product_name:<15} | {total_sold:<11} | {total_revenue:<10}")
  print("_"*60)
  print(f"Total Amount : Rs.{grand_total} ")
  print("_"*60)
   
 def low_stock(self):
   threshold=number_input("Enter the minimum quantity of stock : ")
   order_by=string_input("Order by[oldest/newest] : ")
   if order_by.lower()=="newest":
    order_by="ASC"
   elif order_by=="oldest":
    order_by="DESC"
   else : 
    print("Invalid Order!\nRedirecting to newest!")
    order_by="DESC"
   cursor.execute(f""" 
    SELECT product_id,product_name,cost_price,stock FROM products
    where stock < ?
    ORDER BY product_id  {order_by} 
     """,(threshold,))
   rows=cursor.fetchall()
   print("_"*60)
   print("Product ID | Product Name | Price[Per/Kg] | Stock |")
   print("_"*60)
   if not rows:
    print("All products have sufficient stock!")
   else:
    for row in rows:
     product_id,product_name,cost_price,stock=row
     print(f"{product_id:<10} {product_name:<19} {cost_price:<13} {stock:<5}")
   print("_"*60)

 def view_product(self):
  """
   This shows the existing products details and their stock.

  """ 
  order_by=string_input("Order by [oldest/Newest] : ")
  if order_by.lower()=="oldest":
   order_by="DESC"
  elif order_by.lower()=="newest":
   order_by="ASC"
  else :
   print("Invalid Order!\nRedirecting to newest..")
   order_by="ASC"
  cursor.execute(f""" 
   SELECT product_id,product_name,
   cost_price,stock
   from products
   ORDER BY product_id {order_by}
   """) 
  rows=cursor.fetchall()
  print("_"*60)
  print("Product ID | Product Name | Price[Per or Kg] | Stock |")
  print("_"*60)
  if not rows:
   print("No records available!")
   print("_")
  else:
   for row in rows:
    product_id,product_name,price,stock=row
    print(f"{product_id:<14} {product_name:<15} {price:<20} {stock}")
  print("_"*60)
 def view_three(self):
  """ 
  This function filters : 
  1)Oldest Or Newest
  2)Category
  3)Date Interval 
  """
  
   
  category=string_input("Enter the Category Of Product : ")
  order=string_input("Order by (newest/oldest) : ")
  tup=interval()
  start_date=tup[0]
  end_date=tup[1]
  params=(f"%{category}%",start_date,end_date)
  if order.lower()=="newest":
   order_by="ASC"
  else :
   order_by="DESC"
  cursor.execute(f"""
    SELECT products.product_id,products.product_name,sales.quantity_sold,
     sales.sale_rate,(sales.quantity_sold*sales.sale_rate) AS total_amount,
     sales.date
     FROM products
    INNER JOIN sales ON products.product_id=sales.product_id
     WHERE LOWER(products.category) LIKE LOWER(?)
     AND sales.date BETWEEN ? AND ? 
     
     ORDER BY sales.date {order_by}  
      """,params)
  rows=cursor.fetchall()
  print("_"*75)
  print("Product_Id | Products      | SOLD |  RATE   | AMOUNT |   DATE       ")
  print("_"*75)
  grand_total =0
  if not rows:
   print("No records found!")
   print("_"*75)
   return
  for row in rows:
   product_id,product_name,quantity_sold,sale_rate,total_amount,date=row
   print(f"{product_id:<10} | {product_name:<12} | {quantity_sold:<5} | {sale_rate:<7} | {total_amount:<10} | {date}")
   
   grand_total += total_amount
  
  print("_"*75)
  print(f"Total Amount : Rs.{grand_total}")
  print("_"*75)
 def view_profit_loss(self):
  tup=interval()
  params=(tup[0],tup[1],)
  cursor.execute(""" 
   SELECT SUM((sales.sale_rate-products.cost_price)*sales.quantity_sold) AS profit,
   SUM(sales.sale_rate*sales.quantity_sold) AS SP,
   SUM(products.cost_price*sales.quantity_sold) AS CP
   FROM products
   INNER JOIN sales ON products.product_id=sales.product_id
   WHERE sales.date BETWEEN ? AND ?
   
    """,params)
  rows=cursor.fetchone()
  total_profit=rows[0] if rows and rows[0] is not None else 0
  total_cp=rows[2] if rows and rows[2] is not None else 0
  total_sp=rows[1] if rows and rows[1] is not None else 0 
  print("_"*40)
  print(f"{tup[0]}  TO  {tup[1]}".center(40))
  print("_"*40)
  print(f"Total Investment   : Rs.{total_cp}")
  print(f"Total Sales Amount : Rs.{total_sp}")
  if total_profit >= 0 :
   print(f"Total Profit Made  : Rs.{total_profit}")
  elif total_profit < 0 :
   print(f"Total Loss Between {tup[0]} and {tup[1]} : Rs.{abs(total_profit)}")
  print("_"*40)
class Menu():
 def __init__(self):
  pass
 def menu_main(self):
  print("_"*40)
  print("GrocerySystem".center(35))
  print("_"*40)
  print("1)Product  Manager ")
  print("2)Sales Manager")
  print("3)Low Stock CheckUp")
  print("4)Profit/Loss Calculator")
  print("5)Logging First Time")
  print("6)Exit")
  print("_"*40)
 def menu_1(self):
  print("_"*40)
  print("ProductManager".center(36))
  print("_"*40)
  print("1)Add products in store")
  print("2)View Available Product")
  print("_"*40)
 def menu_2(self):
  
  print("_"*40)
  print("ViewSales".center(36))
  print("_"*40)
  print("1)Add Sales ")
  print("2)View All Sales ")
  print("3)View Sales With Date Interval")
  print("4)View Sales With Date Inteval and Category")
  print("5)Most Sold Products ")
  print("_"*40)

ps=Products_Sales_Manager()
v=View_Manager()
m=Menu()

def main():
 while True : 
  os.system('clear')
  m.menu_main()
  choice=number_input("Enter Command : ")
  match choice:
   case 1:
    os.system('clear')
    m.menu_1()
    choice=number_input("Enter Command : ")
    match choice : 
     case 1:
      os.system('clear')
      ps.add_products()
      
     case 2:
      os.system('clear')
      v.view_product()
   case 2:
    os.system('clear')
    m.menu_2()
    choice=number_input("Enter Command : ")
    match choice:
     case 1:
      os.system('clear')
      ps.add_sales()
     case 2:
      os.system('clear')
      v.view_one()
     case 3:
      os.system('clear')
      v.view_two()
     case 4:
      os.system('clear')
      v.view_three()
     case 5:
      os.system('clear')
      v.view_four()
   case 3:
    os.system('clear')
    v.low_stock()
   case 4:
    os.system('clear')
    v.view_profit_loss()
   case 5:
    os.system('clear')
    ps.first_time()
   case 6:
    os.system('clear')
    print("Thanks From GrocerySystem ".center(50))
    break
  try:
   key=input("Enter to continue : ")
  except :
   pass

if __name__=="__main__":
 main()
