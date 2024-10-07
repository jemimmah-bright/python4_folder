#Control flow Structures are just a way to specify flow of control in programs.
#they determine the order in which a program can be exsecuted basing on loops or conditions
#TYPES
#conditional statements
#e.g "if" "elif" "else" 
#QN create a programm that asks a user for the food type bought from the market
#  the programm should print we bought chicken if the user eneters chicken
#the programm should print we bought liver if the user eneters liver
# else the program should print fish
food_type= input("Enter the food type bought: ").lower()
if food_type == "chicken":
  print(f"you bought chicken from the market")
elif food_type == "liver":
  print(f"you bought liver form the market")
elif food_type == "fish":
  print(f"you bought fish form the market")  
else:
   print(f"please choose from fish,liver or chicken option")

#APPROACH 2
if food_type!='chicken' or food_type!='fish':
   print(f"please choose from fish,liver or chicken option")
elif food_type == "chicken":
  print(f"you bought chicken from the market")
elif food_type == "liver":
  print(f"you bought liver form the market")
else:
   print(f"you bought fish form the market")  

   #USING LOGICAL OPERATORS ("or" and )


  
   