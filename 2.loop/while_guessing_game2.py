#猜數字進階(超過3次就輸了)
select_num=59
guess = None

guess_count = 0
guess_limit = 3
game_over =False

#進行中(沒猜中且在3次內)
while select_num != guess and not(game_over) :
    guess_count += 1 #次數+1
    if  guess_count <= guess_limit:
        guess = int(input("請輸入數字 : "))
        if guess > select_num :
            print("小一點")
        elif guess < select_num :
            print("大一點")
    else : 
        game_over = True 
        # while select_num != guess and not(game_over) 不成立=>跳出迴圈
if game_over :
        print("猜錯3次，你輸了")
else:
        print("恭喜~猜對了")