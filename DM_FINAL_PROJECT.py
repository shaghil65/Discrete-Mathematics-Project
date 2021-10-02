def factorial(n):
    if n == 1:
        return n
    else:
        print("Now This Number",n," Will Multiply With It's Previous Number",n-1)
        return n*factorial(n-1) 



def gcd(a, b):

    if a < b:
        smaller = a
        larger = b
    elif a > b:
        smaller = b
        larger = a

    if larger and smaller > 0:
        r = larger % smaller
        
    
    if larger == 0:
         
        return str(smaller)
    elif smaller == 0:
       
        return  str(larger) 
    else:
        print(larger,"=",int(larger/smaller),"." ,smaller,"+" ,r)
        print("Larger = " + str(larger) + ", Smaller = " + str(smaller))
        return gcd(smaller,r) 

   
    
def power(base, exponent):
    if exponent == 0 :
        return 1
    
    else :
        return base * power(base, exponent - 1)





def Fib(Num):
    if Num == 0 or Num == 1:
        return Num
    else:
        return Fib(Num - 2) + Fib(Num - 1)




while (True):
    print("\n-------------------------Welcome To Recursive Applications-------------------------------------")
    print()
    print(" 1 : To Print Fictorial OF A Number")
    print(" 2 : To Find GCD OF Two Numbers")
    print(" 3 : To Compute Power Of A Number ")
    print(" 4 : To Print Fibonacci Series Till Given Number")
    print(" 5 : To Exit")

    choice = int(input("Enter your Choice: "))

    
    if (choice == 5):
        break

    if (choice == 4):
        num1 = int(input("Please Enter The Range Of Many Fibonnachi Series You Want To Print : "))
        for i in range(num1):
            print(Fib(i), end=" ")

    if (choice == 3):
        num1 = float(input("Please Enter the Value Of Base : "))
        num2 = float(input("Please Enter the  Value Of Exponent : "))
        print(power(num1, num2))

    if (choice == 2):
        int1 = input("Enter integer 1 \n")
        int2 = input("Enter integer 2 \n")
        print("\n GCD of {0} and {1} = {2}".format(int1, int2, gcd(int(int1),int(int2))))
        
    if(choice == 1):
        num= float(input("Please Enter  Your Number : "))
        if num < 0:
            print("Sorry, factorial does not exist for negative numbers")
        elif num == 0:
            print("The factorial of 0 is 1")
        else:
            print("The factorial of", num, "is", factorial(num))