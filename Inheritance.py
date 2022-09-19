#Inheritence
##class A():
##
##    def feature1(self):
##        print("F1")
##
##    def feature2(self):
##        print("F2")
##
##a1 = A()
##
##a1.feature1
##a1.feature2
##
##class B(A):
##
##     def feature3(self):
##        print("F3")
##
##     def feature4(self):
##        print("F4")
##
##b1 = B()
##
##b1.feature1
##


class Person:
  def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
x.printname()


mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

##print(next(myit))
##print(next(myit))
##print(next(myit))

for x in mytuple:
    print(x)


mystr = "banana  "

for x in mystr:
  print(x)


  #x = 300

def myfunc():
  #global x
  x = 200
  print(x)
myfunc()

#print(x)