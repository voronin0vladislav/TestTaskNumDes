def cross_rec(rec1,rec2) -> bool:
    x1l=rec1[0]
    y1l=rec1[1]
    x1r=rec1[2]
    y1r=rec1[3]
    x2l=rec2[0]
    y2l=rec2[1]
    x2r=rec2[2]
    y2r=rec2[3]
    if (min(x1l,x1r)<=min(x2l,x2r)<max(x1l,x1r) and min(y1l,y1r)<=min(y2l,y2r)<max(y1l,y1r)) or (min(x1l,x1r)<max(x2l,x2r)<max(x1l,x1r) and min(y1l,y1r)<max(y2l,y2r)<max(y1l,y1r)):     
        print('True')
        return True
    elif (min(x1l,x1r)<min(x2l,x2r)<max(x1l,x1r) and min(y1l,y1r)<max(y2l,y2r)<max(y1l,y1r)) or (min(x1l,x1r)<max(x2l,x2r)<max(x1l,x1r) and min(y1l,y1r)<min(y2l,y2r)<max(y1l,y1r)):
        print('True')
        return True
    else:
        print('False')
        return False



#Пример 1
rec1 = [0,0,2,2]
rec2 = [1,1,3,3]
cross_rec(rec1,rec2)


#Пример 2
rec1 = [0,0,1,1]
rec2 = [1,0,2,1]
cross_rec(rec1,rec2)


#Пример 3
rec1 = [0,0,1,1]
rec2 = [2,2,3,3]
cross_rec(rec1,rec2)


#Пример 4
rec1 = [0,0,2,2]
rec2 = [1,-1,3,1]
cross_rec(rec1,rec2)


#Пример 5
rec1 = [0,0,2,2]
rec2 = [1,1,3,3]
cross_rec(rec1,rec2)


#Пример 6
rec1 = [0,0,2,2]
rec2 = [-1,1,1,3]
cross_rec(rec1,rec2)




