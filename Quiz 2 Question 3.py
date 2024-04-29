mylist = [2, 8, 64, 16, 32, 4, 16, 8]
mylist = [1, 2, 3, 5, 94, 31, 53, 17]

a=len(mylist)

while a!=0:
    for x in mylist:
        if mylist.count(x)!=1:
            y=1
            a=0
        else:
            y=0
            a=a-1
  
if y==1:
    print("This list contains duplicate values.")
else:
    print("This list does not contain duplicate values.")
    



#for x in mylist:
#    if mylist.count(x)!=1:
#        y= "This list contains duplicate values of {}"
#        print(y.format(x))
#    else:
#        z= "This list does not contain duplicate values of {}"
#        print(z.format(x))

    
