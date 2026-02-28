#compound interset
p=float(input("enter priniciple amount"))
t=float(input("enter time amount"))
r=float(input("enter rate amount"))
amount=p*(1+r/100)**t
ci=amount-p
print("Total Amount=",amount)
print("compound interest=",ci)
