print("Simple Arithmetic Calculator")

operations_dict={
    1:"Addition",
    2:"Subtraction",
    3:"Multiplication",
    4:"Division"
}

while True:
    print("Select any operation 1.Addition 2.Subtraction 3.Multiplication 4.Division 5.Quit")
    try:
        operation=int(input("Enter the operation: "))
        if operation==5:
            break
        else:
            if operation>=1 and operation <=4:
                input_1=input("Enter number 1: ")
                input_2=input("Enter number 2: ")
                input_1,input_2=float(input_1),float(input_2)
                if operation==1:
                    result=input_1+input_2
                elif operation==2:
                    result=input_1-input_2
                elif operation==3:
                    result=input_1*input_2
                elif operation==4:
                    result=input_1/input_2
            else:
                print("Invalid option, please select the correct option")
            print("{} of {} and {} is {}".format(operations_dict[operation],input_1,input_2,result))
    except:
        print("Pleast enter a valid operation")