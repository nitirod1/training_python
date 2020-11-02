
def process_stack(sum,mx):
    temp = []
    i=0
    for e in sum :
        if len(e) == 0 or min(e)>mx:
            temp.append(i)
        i=i+1
    return temp

def process_dict(sum,space):#sum[start]
    i=0
    for e in sum:
        if i+1>=len(space): #
            i=0
        else:
            i=i+1
    return space[i]

def move(sum,start,end):#sum[start]
    temp = sum[start].pop()
    sum[end].append(temp)
    return sum

def find_min(sum):
    mn = 99999
    i=0
    pos=0
    for e in sum :
        if len(e)!=0:
            if min(e)<mn:
                mn = min(e)
                pos = i
        i=i+1
    return pos

def find_delta(sum,start,mx):
    i = 0
    k = 0
    while sum[start][k]>mx:
        k=k+1
    for e in sum:
        if min(e)-sum[start][k]==1:
            return i,k
        i=i+1
    return 999999

def hanoi(sum,start,end,mx,count):# end คือตำแหน่งที่ mx ต้องการย้ายไป
    space= process_stack(sum,mx)
    if mx in sum[end] and len(space)==2 :
        return sum,count
    if len(space)==0:
        pos_mn = find_min(sum)
        posdelta,k=find_delta(sum,pos_mn,mx)
        sum,count= hanoi(sum,pos_mn,posdelta,sum[pos_mn][k],count)
        return hanoi(sum,start,end,mx,count)
    else:
        move_end=process_dict(sum[start],space)
        if mx in sum[end]:
            space= process_stack(sum,mx-1)
            pos_mn=find_min(sum)
            move_end=process_dict(sum[pos_mn],space)
            sum = move(sum,pos_mn,move_end)
            count=count+1
            return hanoi(sum,pos_mn,end,mx-1,count)
        sum = move(sum,start,move_end)
        count=count+1
        return hanoi(sum,start,end,mx,count)
sum=[[4,3,2,1],[],[]]
count = 0
sum,count=hanoi(sum,0,2,4,count)
print(sum)
print(count)