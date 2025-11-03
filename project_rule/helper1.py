def get_input(prompt,cast_type=str,msg="Invalid Input!"):
 while True:
  try : 
   return cast_type(input(prompt))
  except : 
   print(msg)


