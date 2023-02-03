# 巢狀迴圈-判斷學號
ID = input("請輸入學號 : ")
print(ID)
year = int(ID[1:3])
# 取ID第2和3的數值判斷年級
print(year)

if year < 4 :
    print("您已畢業")
elif year >= 4 and year <= 7:
    if year == 7:
        print("您是新生")
    elif year == 6 :
        print("您為一年級生")
    elif year == 5 :
        print("您為二年級生")
    elif year == 4 :
        print("您為三年級生")
else :
    print("您尚未註冊")
