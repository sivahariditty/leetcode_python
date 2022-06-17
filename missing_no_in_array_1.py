arr = [3,7,1,2,6,4,5]
n = 8
flg = [0] * 8

for itm in arr:
    flg[itm-1] = 1

print(flg.index(0)+1)

