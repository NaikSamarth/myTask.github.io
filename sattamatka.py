# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random

print("1. Want to play Jodi number?")
print("2. Want to play Open to Close number?")

option = int(input("Press any of the above number and Press Enter: "))

if option == 1:
    print("========================================================================")
    print("**KALYAN JODI**")
    print("========================================================================")
    
    print()
    
    num = int(input("Enter the kalyan JODI number(0-99): "))
    money_jodi = int(input("Enter the amount(Rs) for JODI: "))
    kalyan_jodi = random.randrange(0,100)
    
    final_jodi_money = money_jodi * 90
    
    print("*****************")
    print(f"Kalyan JODI is {kalyan_jodi}")
    print("*****************")
    
    if num == kalyan_jodi:
        print(f"Congretulation!! Rs.{final_jodi_money}/- Tuka modko number({num}) laaglo")
    else:
        print("ooops!! Tuji  JODI number geli")
    
elif option == 2:
    print("========================================================================")
    print("**KALYAN OPEN TO CLOSE**")
    print("========================================================================")
    
    print()
    
    num1 = int(input("Enter the number for kalyan OPEN(0-9): "))
    money_open = int(input("Enter the amount(Rs) for OPEN: "))
    kalyan_open = random.randrange(0,10)
    
    final_open_money = money_open * 9
    
    print("*****************")
    print(f"Kalyan OPEN is {kalyan_open}")
    print("*****************")
    
    if num1 == kalyan_open:
        print("Congretulation!! Tuka modko laaglo")
    else:
        print("ooops!! Tujo OPEN number gelo")
    
    print()
    
    num2 = int(input("Enter the number for kalyan CLOSE(0-9): "))
    money_close = int(input("Enter the amount(Rs) for CLOSE: "))
    kalyan_close = random.randrange(0,10)
    
    final_close_money = money_close * 9
    
    print("*****************")
    print(f"Kalyan close is {kalyan_close}")
    print("*****************")
    
    if num2 == kalyan_close:
        print("Congretulation!! Tuka modko laaglo")
    else:
        print("ooops!! Tujo CLOSE number gelo")
        
    print()
    
    if num1 == kalyan_open and num2 == kalyan_close:
        print(f"Rs.{final_open_money+final_close_money}/- Congretulation!! Tuka OPEN & CLOSE({num1num2}) donui laaglo")
    elif num1 == kalyan_open:
        print(f"Rs.{final_open_money}/- Tuka OPEN number({num1}) laaglo pun CLOSE laaguna")
    elif num2 == kalyan_close:
        print(f"Rs.{final_close_money}/- Tuka CLOSE number({num2}) laaglo pun OPEN laaguna")
    else:
        print("Tuka aaiz modko laaguna")
        
else:
    print("**---YOU HAVE ENTERED WRONG NUMBER---**")


    
    
