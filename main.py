import time
import cython


def showInvoice(totalPrice):
#Invoice here maakr it snazzy
    print("Is this your invoice:")
    print(f"The total for tonight is{totalPrice}")
    print("Proceeding to cgeckout in 10 seconds")
    time.sleep(10)
    #Displays an order confirmation to the customer with the total price    
     #Enter your python code here
def payInvoice(totalprice):
    ccnum = int(input("ENTER CREDIT CARD NO: "))
    print(cardVerify(ccnum))
    address = input("ENTER BILLING ADDRESS: ")

    #paying 
#Menu Screen
def cardVerify(ccnum):
    sum = 0
    sum2 = 0
    num3=ccnum
    length = len(str(ccnum)) 
    print(length)
    len_card = length 

    if length % 2 != 0:
    
        length = ((length - 1) / 2)
    
    else:
    
        length = length / 2
    check = ccnum
    num2=ccnum
    for i in range(len(str(length))):
    
        #checks sum of digits  multiplied
        check = check / 10
        digit = check % 10
        digit = digit * 2
        if digit  < 10:
            sum += digit
            check = check / 10
            
        
        #separates digits if two decimal places
        else:
            sum += (1 + (digit % 10))
            check = check / 10
#function/ objects for pizza, Drink, Invoice, check
        digit2 = num2 % 10
        sum2 += digit2
        num2 = num2 / 100
    
    total_sum = sum + sum2
    print(f"total sum: {total_sum}\n")
    #checks if card valid using Luhns algorithm
    if total_sum % 10 == 0:
    
        while True:
        
            digit = 0
            #American express starts with 34 or 37
            if len_card == 15:
                #dividing gets as many digits as we need
                digit =  num / 1000000000000
                if digit == 34 or digit == 37:
                    print("AMEX\n")
                    break
                
            #VISA starts with 4
            if len_card == 16 or len_card == 13:
                if len_card == 16:
                
                    digit =  num / 1000000000000000

                
                elif len_card == 13:
                
                    digit =  num / 1000000000000
                
                if digit == 4:
                
                    print("VISA\n")
                    break
                
            
            #mastercard starts with 51, 52, 53, 54, or 55
            if len_card == 16:
                print("test mastercard")
                digit =  num / 100000000000000
                if digit == 51 or digit == 52 or digit == 53 or digit == 54 or digit == 55:
                
                    print("MASTERCARD\n")
                    break

                
            
            else:
            
                printf("test INVALID\n");
                break;
            print("test2 INVALID\n")
            break

#EOF EXIT
        
    
    if total_sum % 10 != 0:
    
        print("INVALID\n")

    


#pizza function
    #define each type of pizza
#drink function

#invoice function

#cardVerify(5555555555554444)
cardVerify(5105105105105100)
#cardVerify(1)