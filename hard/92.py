def myfunc(n):
  return lambda a : a +n

myadd=myfunc(2)
mymodule=(myadd(11))
print(mymodule)