
class human:
 def __init__(self, name, age):
    self.name = name
    self.age = age
    
h1 = human("jason", 15)

print(h1.name)
print(h1.age)


class human:
  def __init__(self, name, age):
    self.name = name
    self.age = age

h1 = human("John", 36)

print(h1.name)
print(h1.age)



class User:

    def __init__(self, name, age, colour):
        self.fullname = name
        self.age = age
        self.colour = colour

    
user1 = User("Joffrey", "15", "black")
user2 = User("James", "20", "1")



class Users():
    def __init__(self, name, age, colour):
        self.fullname = name
        self.age = age
        self.colour = colour


user3 = Users("Fry", "15", "black")
user4 = Users("Jon", "20", "1")


print(user3.fullname)

