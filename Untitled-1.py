print("Hello World!!!")
for i in range(20):
    print(i)

class MyClass:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def __str__(self):
        return  f"name:{self.name}, id:{self.id}"

my = MyClass("Name", 123)
print(my)

