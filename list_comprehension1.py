#ls = [2,3,4,5,6,7,8,9,10]
ls = [ 1 , 3 , 5 , 8 , 10 , 13 , 18 , 36 , 78 ]
ls1 = [ i for i in ls[::2] if i % 2 ==0]
print ls1