#進階計算機
num1 = float(input("請輸入第一個數值: "))
op = input("請輸入運算符號 : ")
num2 = float(input("請輸入第二個數值: "))

if op == "+":
    print(num1,"+",num2,"=",num1+num2)
elif op == "-":
    print(num1,"-",num2,"=",num1-num2)
elif op == "*":
    print(num1,"*",num2,"=",num1*num2)
elif op == "/":
    print(num1,"/",num2,"=",num1/num2)
else :
    print("不支援運算")