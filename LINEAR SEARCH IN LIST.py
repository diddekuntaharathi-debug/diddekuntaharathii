list=[1,2,3,4,5]
key=int(input("enter an element:"))
flag=0
for i in range(len(list)):
    if list[i]==key:
        print("Element is found at position:",i)
        flag=1
        break
if flag==0:
    print("Element is not found")
