a = float(input("What was the total bill?"))
b = float(input("What percentage tip would you like to give? 10, 12 or 15?"))
tip = float(1+b/100)
#twelve_percent_on_totalbill = a*percentage
#tip= twelve_percent_on_totalbill+a
#instead of doing above 3 line code we can just use total bill multiplied with 1.12 ,here 1 is considered as totalbill and 0.12 is the percentage of tip that we got 12/10
total = float(a*tip)
d = float(input("How many people to split the bill?"))
c = float(total/d) 
#print(round(c,3))      
 #simply use formula of a= tip/100*bill + bill,b=a/number of people to split
 #to round off exactly we use format ,method
final_amount="{:.3f}".format(c)
print(f"each person should pay:${final_amount}")