for i in range(1,10) :
    for j in range(1,10) :
        # print("I = ",i ,", J = ",j)
        
        # if j == 9 :
        #     print("\t",i*j) #i沒限制，j==9(才會印出) "\t"換行
        # else :
        #     print("\t",i*j,end=" ") #j<9 不換行

        if j == 9 :
            print("\t",i,"*",j," = " ,i*j) #i沒限制，j==9(才會印出) "\t"換行
        else :
            print("\t",i,"*",j," = " ,i*j,end=" ") #j<9 不換行