#for 迴圈

#for 變數 in 字串 或 列表
###要重複執行的程式碼

# for letter in "Hello World":
#     print(letter)

# for num in [0,1,2,3]:
#     print(num)

# pow(2,3)=2*2*2  次方

# print(pow(2,5))
def power(base_num,pow_num):
    # 方法一
    # result = base_num
    # for index in range(pow_num-1):
    #     result = result * base_num
    # 2*2*2*2
    # return result

    # 方法二
    result = 1
    for index in range(pow_num):
        result = result * base_num
    1*2*2*2*2
    
    return result
print(power(2,4))
    