# Program to devide teo numbers without using the dvision operator

def devide(ourDividend, ourDivisor):
    
    # check if divisor is +ve or -ve
    sign = (-1 if((ourDividend < 0)^
                  (ourDivisor < 0 )) else 1);

    # Make both positive
    ourDividend = abs(ourDividend);
    ourDivisor = abs(ourDivisor);

    quotinentNumber = 0
    tempNumber = 0

    # go from 31 to 0 and accumulate all valid bits

    for i in range(31, -1 , -1):

        if (tempNumber + (ourDivisor << i) <= ourDividend):
            tempNumber += ourDivisor << i 
            quotinentNumber |= 1 << i

    # Assuming the sign value computed ear;ier is -1, negative the quotinent value 
    if sign ==-1 :
        quotinentNumber=-quotinentNumber
    return quotinentNumber


a = int(input("Enter a for a/b :"))
b = int(input("Enter b for a/b :"))
print("Result of ",a,"/",b,"is",devide(a,b))

