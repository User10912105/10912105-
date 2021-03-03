''' main '''
# 使用自建的套件 myMath 來計算使用者輸入的五個數的平均值
from mymath import myStatistics
list1 = []
for i in range(5) :
    a= float(input('請輸入五次數字:'))
    list1.append(a)
sum = tuple(list1)

print(myStatistics.myMean(sum))
