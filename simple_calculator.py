def addition(a,b):
    return(a+b)
def subtraction(a,b):
    return(a-b)
def multiplication(a,b):
    return(a*b)
def division(a,b):
    return(a/b)

number1=eval(input("Enter the first number:"))
number2=eval(input("Enter the second number:"))

print("Select any option")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exit")

while(True):
    choice=int(input("Enter the choice from(1/2/3/4/5):"))
    if choice in (1,2,3,4,5):
        if choice==1:
            print("Addition of number1 and number2 ",number1,"+",number2,"=",(number1+number2))
        elif choice==2:
            print("Subtraction of number1 and number2",number1,"-",number2,"=",(number1-number2))
        elif choice==3:
            print("Multiplication of number1 and number2 ",number1,"*",number2,"=",(number1*number2))
        elif choice==4:
            print("Division of number1 and number2",number1,"/",number2,"=",(number1/number2))
        elif choice==5:
            print("Exit")
            exit()
        else :
            print("Invalid choice please try again")