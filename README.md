<<<<<<< HEAD
# GIT
>git init-初始化 git

> git clone 網址

>git status 狀態

>git branch -r 查看遠端還有什麼分支

>git checkout 分支 切換到分之

> git add . (增加)=>git commit -m "說明" =>git remote add origin(遠端命名) 網址(新增遠端網址) (git remote -v 檢查遠端)
=>git push -u origin(遠端命名) main(branch)

>git pull --rebase 如果有衝突, 就再修正衝突即可

# Python 語法
>print()換行

>end=" "不要換行
# Python list
* Range -使用range()和 len()函數創建合適的可迭代對象。
>range(起始值,終止值,遞增(減)值)

* 元組tuple(資料不能做更改)
```
score = (90,80,70,60)
score[0] = 10
print(score[i])
```
#檔案寫入、讀取

> open("檔案路徑",mode="開啟模式")

> 絕對路徑 (ex:C:/Users/黃則叡/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/file.py)
> 相對路徑 -> 以程式位置做延伸(ex:file.py)

> mode ="r" 讀取、
> mode ="w" 覆寫、
> mode ="a" 在原先的資料後寫東西
