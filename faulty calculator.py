print("Enter the first number")
num_1=int(input())
print("Enter the second number")
num_2=int(input())
print("Enter your operators ""+,-,*,/,%")
num_3=input()

if num_1==45 and num_2==3 and num_3=="*":
    print("555")
elif num_1==56 and num_2==9 and num_3=="+":
    print("77")
elif num_1==56 and num_2==6 and num_3=="/":
    print("4")
elif num_3=="*":
    num4=num_1 *num_2
    print(num4)
elif num_3=="+":
    plus=num_1+num_2
    print(add)
elif num_3=="/":
    div=num_1/num_2
    print(div)
elif num_3=="-":
    sub=num_1-num_2
    print(sub)
elif num_3=="%":
    per=num_1%num_2
    print(per)
else:
    print("Error! Please check your number")


