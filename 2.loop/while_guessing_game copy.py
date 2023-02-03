#猜數字
select_num=59
guess = None

while select_num != guess:
    guess = int(input("請輸入數字 : "))
    if guess > select_num :
        print("小一點")
    elif guess < select_num :
        print("大一點")
print("恭喜~猜對了")