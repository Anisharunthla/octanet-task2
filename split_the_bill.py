import math
print("Looking to split the cost of a group purchase?\nWelcome tp our recepit calculator!\n We will as you a few question about you purchase(s)to calculate the totel cost per person.")

price_all = eval(input("Step1: Please input the cost of each meakl/product.\n(Note: Eliminate the '$' sign instead seperate with a '+'.)"))

tax_p = float(input("Step2: What is the sales tax in your area?\n(Note: Eliminate the '%' sign.)"))

tip_p = float(input("Step3: What percentage would you like to give as a tip?\n(Note: Eliminate the '%'sign.)"))

split = float(input("Step4: How many people are you splitting the bill with?\n(Note: If you are not splittin the bill with anyone,just type '1'.)"))

total_p =(price_all + (price_all*(tax_p/100.0)) + (price_all*(tip_p/100.0)))/split

final_p = round(total_p,2)

print("Total cost per person is : $",final_p,".")
