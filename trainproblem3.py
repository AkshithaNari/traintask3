l1=int(input("train1 length in m:"))
l2=int(input("train2 length in m:"))
t_s1=int(input("train1 speed in kmph: "))
t_s2=int(input("train2 speed in kmph: "))
total_length=l1+l2
rs=(t_s1+t_s2)*5/18
t=total_length/rs
print("time of crossing in sec:",t)
