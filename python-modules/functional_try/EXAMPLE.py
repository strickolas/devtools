from option import *


ls = []
x = Try(lambda: ls[1])
print(type(x))
print(x.get())
print(type(x.get()))
print()

y = Try(lambda: ls + [1])
print(type(y))
print(y.get())
print(type(y.get()))
