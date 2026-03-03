#PERFECT SQUARE
import math
n=int(input("enter n number"))
root=math.isqrt(n)
if root*root==n:
    print("Perfect square")
else:
    print("Not Perfect square")
