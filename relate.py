# for a one to many we have association, aggregation or composition
# --> Association



class GroceryItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Shopper:
    def __init__(self, name):
        self.name = name
        self.grocery_items = []
shopper = Shopper("Klein")
item1 = GroceryItem("apple", 400)
item2 = GroceryItem("orange", 678)
shopper.grocery_items.append(item1)
shopper.grocery_items.append(item2)
#  this is  a one way one to many relationship since only the shopper knows the grocery items but the grocery item has no need to know who the shopper is


#  for a two way one to many relationship we have an example of a teacher and student where both the teacher and the student need to know each other

# class Student:
#     all = []
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.teacher = None
#         Student.all.append(self)

#     @property
#     def teacher(self):
#         return self.teacher
#     @teacher.setter
#     def teacher(self, value):
#         self.value = value
#         if not isinstance(value, Teacher):
#             raise TypeError("Teacher must be an instance of Teacher class")
#         self._teacher = value
# class Teacher:
#     def __init__(self, name):
#         self.name = name
#     def students(self):
#         return [student for student in Student.all if student.teacher == self]


# class GroceryItem:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
# class Shopper:
#     def __init__(self, name):
#         self.name = name
#         self.shopping_items = []
# goods = GroceryItem("Eggs", 900)
# buyer = Shopper("Klein")
# buyer.shopping_items.append(goods)
# print(buyer.shopping_items)

class CPU:
    def __init__(self, cpu_type):
        self.cpu_type = cpu_type
    def __str__(self):
        return str(self.cpu_type)
class Computer:
    def __init__(self, cpu_type):
        self.cpu = CPU(cpu_type)
my_cpu = CPU("MWXH-1006")
my_computer = Computer(my_cpu.cpu_type)
print(my_computer.cpu)