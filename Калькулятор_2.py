import kalkylator
z=input()
if z=="*":
  kalkylator.i()
if z=="+":
  kalkylator.ili()
if z=="-":
  kalkylator.minus()
def kalkylator():
a=int(input(),2)
b=int(input(),2)
def i():
  print(bin(a&b))
def ili():
  print(bin(a|b))
def minus():
  print(bin(a-b))
 