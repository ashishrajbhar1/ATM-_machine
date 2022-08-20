import time

print("welcome to Mini Bank")

time.sleep(1)

password = 1234

pin=int(input("Enter Your ATM Pin :- "))

balance = 5000

if pin==password:
    while True:
        print('''
        
        1 == balance
        2 == whithraw ammount
        3 == exit
        
        
        ''')
        
        try:    
             
            option = int(input("Please enter your choise "))
        except:
            print("Please enter valid option")        
        
        
        
        if option==1:
            print(f"your balance is {balance}")
        
        if option==2:
            withraw_amount=int(input("enter the amount"))
            
            balance = balance-withraw_amount
            
            print(f"your curent amount {balance}")
            
        if option ==3:
            
            break
        
else:
    print("invalid pin")