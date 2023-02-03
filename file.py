#檔案寫入、讀取

# open("檔案路徑",mode="開啟模式")
# 絕對路徑 (ex:C:/Users/黃則叡/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/123.txt)
# 相對路徑 -> 以程式位置做延伸(ex:123.txt)

# mode ="r" 讀取
# mode ="w" 覆寫
# mode ="a" 在原先的資料後寫東西

# file = open("123.txt",mode="r")
# print(file.read())#開啟
# print(file.readlines())#開啟每一行列印
# for line in file : #每一行列印
#     print(line)
# file.close

# file = open("123.txt",mode="w")
# file.write("hello")
# file.close

file = open("123.txt",mode="a",encoding="utf-8")
file.write("\n你好") #中文需轉換encoding="utf-8
file.close


# 為上寫法的縮寫=>無須關關閉
with open("123.txt",mode="a",encoding="utf-8") as file:
    file.write("\n 晚安")
