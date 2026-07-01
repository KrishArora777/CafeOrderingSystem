print("======= Welcome To Python Cafe ========")

name=input("Enter Your Full Name : ")
age=int(input("Enter Your Age : "))
name = name.strip()
name = name.title()

firstname=name.split()[0]

print("Hey!!",firstname)

menu="Burger","Pizza","Pasta","Garlicbread","Tea","Coffee"
print("Today's Menu:",menu)
item=input("what Would You Like To Order? ")
item= item.title()

if item in menu:
    quantity=int(input("How Many Would You Like :"))
    print("Awesome ! Calculating Your Bill....")
    price=150
    total=price*quantity

    if age<18 or quantity >5:
        final_bill=total-total*0.1
    elif age>60:
        final_bill=total-total*0.2
    else:
        final_bill=total
        
else:
    print("Sorry, that item is not available.")

if final_bill>500:
    if firstname.startswith("A") or firstname.startswith("S"):
        print("VIP CUSTOMER")

for i in range(1,10):
    for j in range(0,i):
        print("*",end="")

print("                         ")

print("RECEIPT")

print( "Name: ",name)
print("Item: ",item)
print("Final Bill: ",final_bill)

for i in range(1,10):
    for j in range(0,i):
        print("*",end="")
       





