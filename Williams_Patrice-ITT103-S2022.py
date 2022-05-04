

# Function definition for Class 1
def commission_1(amount=0.0):
    sales_amount = (float(amount))
    if sales_amount <= 1000:
        return sales_amount * 0.06 
     
    elif sales_amount > 1000 and sales_amount < 2000:
        return sales_amount * 0.07
        
    elif sales_amount >= 2000:
        return sales_amount * 0.10

     
# Function definition for Class 2
def commission_2(amount = 0.0):
    sales_amount = (float(amount))
    if sales_amount < 1000:
        return sales_amount * 0.04
        
    elif sales_amount >= 1000:
        return sales_amount * 0.06


# Function definition for Class 3
def commission_3(amount = 0.0):
    sales_amount = (float(amount))
    return sales_amount * 0.045

    
 
# Function definition to run another calculation   
def continue_():
    calcAgain = str(input("\nDo you wish to do another calculation?  'y' for YES Or 'n' for NO: "))
 
    while calcAgain == 'Y' or calcAgain == 'y':
        main()

    if calcAgain == 'N' or calcAgain == 'n':
        print("Exiting Console.... Goodbye!")    
        time.sleep(2)
    else:
        print("Invalid Input. Try again\n\n")
        continue_()




# Function definition to check if Sales Number is Valid    
def validateID(x):
    if len(x) == 0:
        print("Error! Field cannot be empty")
        main()
    elif len(x) != 5:
        print("Invalid Input! Sales number must be 5 characters long. Try Again")
        main()
        
    initials = x[0:2]
    if not initials.isalpha():
        print("Invalid Input! Sales number must start with 2 letters(First and Last initial) eg TK123. Try Again")
        main()

    user_num = x[-3:]
    if not user_num.isdigit():
        print("Invalid Input! Sales number must end with 3 numbers. Try Again")
        main()

# Function definition to check if input is decimal
def check(y):    
    try:
        float(y)
        return True
    except ValueError:
        return False
            

# Function definition to check if Sales Amount is Valid    
def validateAmt(y):
    if check(y) == True:
        return (float(y))
    else:
        print("Invalid Input! Please enter a decimal value")
        get_Amt()
    if len(y) == 0:
         print("Error! Field cannot be empty")
         get_Amt()
    

# Function definition to Prompt for Agent Number    
def get_ID():
    print("\nPlease enter your sales number: ")
    
    if keyboard.read_key() == "esc":
        print("You pressed 'Esc'. Exiting Console...")
        time.sleep(2)
        sys.exit()
    else:
        agent_num = str(input())
        return validateID(agent_num) # Call ID Validation Function


# Function definition to Prompt for Sales Amount                 
def get_Amt():
    print("\nPlease enter sales amount: ")
    
    if keyboard.read_key() == "esc":
        print("You pressed 'Esc'. Exiting Console...")
        time.sleep(2)
        sys.exit()
    else:
        amt = str(input())
        return validateAmt(amt) # Call Sales Validation Function


def get_Class():
    print("\nPlease enter: \n \t '1' for Class 1 \n \t '2' for Class 2 \n \t '3' for Class 3 \n \t 'Esc' to exit")

    if keyboard.read_key() == "esc":
        print("You pressed 'Esc'. Exiting Console...")
        time.sleep(2)
        sys.exit()
    else:
        opt = str(input())
        return opt

           
   
def main():
    get_ID() #Call Function
    sales = get_Amt() #Call function and assign return value
    Class = get_Class() #Call function and assign return value

    classDict={ 
                '1': commission_1(sales), #Call Class1 Function
                '2': commission_2(sales), #Call Class2 Function
                '3': commission_3(sales), #Call Class3 Function
              }
        
    print(classDict.get(Class, f"The Class '{Class}' is not an option!"))# for default if Class is not found     
    continue_()       
                   


    
import keyboard
import sys
import time

print ("\nWelcome to JamEx Commission Calculator!   ") 
print("Press Esc to exit at any time. ")
main()

















