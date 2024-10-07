# NO1  Write a program that takes two numbers as input and display their sam, diffrence,product and their quotient
#number_1=input("enter the first number") then cast the value to float or an integer
#sum
number_1=int(input("enter the first number"))
number_2=int(input("enter the second number")) 
sum= number_1 + number_2
print(f"the sum of {number_1 } and {number_2} is : {sum}")
# #diffrence
diffrence = number_1 - number_2
print(f"the diffrence of {number_2} and {number_1} is : {diffrence}")
# #product
product = number_1* number_2
print(f"the product of {number_1} and {number_2} is : {product}")
# #division/quotient
division= number_2/number_1
print(f"the division of {number_2} and {number_1} is :{division}")
# #modulus
modulus=number_2% number_1
print(f"the modulus of {number_2} and {number_1} is : {modulus}")
# #floor division
floor_division = number_2 // number_1
print(f"the floor_division of {number_2} and {number_1} is : {floor_division}")


# # NO2  Write a program that compairs two integers and prints whether the first number is greater than less than or equal to the second number
#here we work with an "if loop"
if number_2>number_1 :
          print(f"{number_2} is greater than {number_1}")
elif number_2<number_1 :
         print(f" {number_2} is less than {number_1}")
else : 
    print (f"they are equal")


# # NO3  wRITE A PROGRAM THAT CHECKS IF a given number is between 10 or 20 ( where by 20 is inclusive) using logical operators

given_number = int(input("enter the given number:"))
if 10 < given_number <= 20 :
     print(f"{given_number} is between ")
else:print(f"{given_number} is not between")


# # NO4  Write a program that prints the squars of all integers from 1-10 using a for loop
for integers in range (1,11):
      print(f"The square of {integers} is: {integers**2}")

# #NO5  Write a simple program that asks a user for their age if the age is greater or equal to 18 is  print your an adult your qualified else tell them your ot qualified

Age= int(input("enter given age :"))
if Age>=18:
      print("your an adult")
else:
     print("your not qualified")
     
# we have the following student details and marks enter these details
#  from the keyboard
studentName= "Ritah Liz"
studentNumber= "SEP23/BCS/14"
programming = 78
DataScience= 89
ComputerApplications= 55


StudentName= input("Enter your student name: ")
StudentNumber= input("Enter your student number: ")
programing= int(input("Enter marks stored in programing : "))
DataScience=int(input("Enter your Data science mark : "))
ComputerApplication= int(input("Enter the mark assigned to  computer application : "))
sum= programing + DataScience + ComputerApplication
NumberOfSubjects=3  
average = round((sum/NumberOfSubjects,3))
print(f"average of {StudentName} and number is {StudentNumber} and average is : {average}")

#NO5 Write a program that converts celicius temp to fahrenhiet 
# the program should ask the user to enter the temp in degrees celius


celsius=int(input ("\nEnter temperature in celsius degrees:"))
Fahrenheit=(celsius * 1.8) + 32
print(f"{celsius} degree celsius is equal to :  {Fahrenheit} degree fahrenheit", end="\n\n")


#NO6Acars mile per gallton can be calculate with the
#  following formular(MPG=Milesdrive/gallons of gas uesd)
#  it should calculate the cars miles per gallon and display the result


miles_driven=float(input("\nEnter the number of miles :"))
gallons_of_gas_used = float(input("Enter gallons of gas used :"))
MPG=miles_driven/gallons_of_gas_used
print("cars mile per gallons=", MPG, end="\n\n")
