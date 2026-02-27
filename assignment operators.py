Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=6
b=4
print("sum is:",a+b)
sum is: 10
print("sub is:"a-b)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("sub is:",a-b)
sub is: 2
print("mul is:",a*b)
mul is: 24
print("div is:",a/b)
div is: 1.5
print("mod is:",a%b)
mod is: 2
print("floor div is:",a//b)
floor div is: 1
print("exp is:",a**b)
exp is: 1296
print(a<b)
False
print(a>b)
True
print(a<=b)
False
print(a>=b)
True
print(a==a)
True
print(a!=b)
True
print(a==b)
False
a=5
b=9
a+=b
print(a)
14
a-=b
print(a)
5
a=4
b=9
print(a-=b)
SyntaxError: invalid syntax
5
a=4
b=9
print(a-=b)
SyntaxError: multiple statements found while compiling a single statement




a=True
b=False
print(a and b)
False
print(a or b)
True
print(a not)
SyntaxError: invalid syntax
a=3
b=5
print(a&b)
1
print(a^b)
6
print(a/b)
0.6
print(~a)
-4
print(a//b)
0
print(a>>b)
0
print(a>>2)
0
print(a<<2)
12
print(a||2)
SyntaxError: invalid syntax
print(a|2)
3
print(a|1)
3
print(a||2)
SyntaxError: invalid syntax
a=5
b=8
c=5
print(a is c)
True
print(b is c)
False
>>> print(c is a)
True
>>> a=[1,2,3,4,7,9]
>>> b=[2,3,4,8,6,1]
>>> print(1 in b)
True
>>> print(2 in b)
True
>>> print(5 in a)
False
>>> print(2 not ina)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(2 not in a)
False
>>> a=5
>>> b=7
>>> print(a is 4)
False
>>> print(b is not 8)
True
>>> print(b is not 7)
False
>>> print(b is 7)
True
>>> a=5
>>> b=8
>>> c=a
>>> print(a is c)
True
>>> print(b is a)
False
>>> print(c is a)
True
>>> print(b is c)
False
