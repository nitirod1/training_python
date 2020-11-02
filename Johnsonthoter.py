def change (condition):
    if condition == False :
        return True
    else:
        return False
condition = []
# tydefstruct sadas:
    #data 
    #condition = TRUE
#SADES[5]
#SADES[0].DATA = ???
#SADES[0].CONDTION = ????
# [TRUE, TRUE, TRUE ,TRUE ]
#   0      1    2       3   
#   1       2   3       4
data = []
swap = lambda x,i,j : (x[j],x[i])
def finding():
    for i in range(len(data),0,-1):
        index  = data.index(i)## index ของ ตัวที่ค้นพบ
        if condition[data[index]-1]==True:
            if index-1>-1 and data[index]>data[index-1]:
                return index
        else:
            if index+1<len(data) and data[index]>data[index+1]:
                return index
    return -1

def reverse (k):
    for i in range(0,len(data)):
        if data[i]>data[k]:
            condition[data[i]-1]=change(condition[data[i]-1]) 
def start (x):
    left_to_right = True
    for i in range(0,x):
        condition.append(left_to_right)
def Johnsonthoter(x):
    o = 1
    for i in range(1,x+1):
        data.append(i)
    print(data,o)
    k = finding()
    while k!=-1:
        if condition[data[k]-1] == True:
            data[k],data[k-1] = swap(data,k,k-1)
            reverse(k-1)
        else:
            data[k],data[k+1] = swap(data,k,k+1)
            reverse(k+1)
        k = finding()
        o=o+1
        print(data,o)

if __name__ == "__main__":
    x = int(input())
    start(x) ## set boolean left to right
    Johnsonthoter(x)