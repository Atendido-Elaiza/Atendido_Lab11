#PSEUDOCODE
Item1 = 50.10
Item2 = 70.25
Item3 = 60.75
payment = 500
text = "Enter the amount of item"
total_amount = Item1 + Item2 + Item3
#process 
input(text)
input(Item2)
input(Item3)
print ("f*total amount: ${total_amount}")
#discount application
if (total_amount>100):
    discount = total_amount *0.10 
    total_amount = discount
    print (f"10% discount applied ${discount:2f} saved")
else:
    print("No discount applied.")
    
#discount total amount 
print (f"discount total amount: ${total_amount: .2f}")
#loyalty points application 
loyalty_points = total_amount / 10 #calculate loyalty points 
print(f"{loyalty_points:.2f} loyalty points received")

#payment & change
print(f"payment: ${payment}")
if (payment>total_amount):
    change = payment - total_amount     #subtract total amount to payment
    print(f"${change: .2f} change")
else:
    print("insufficient payment") 

