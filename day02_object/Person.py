class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + " is eating.")

    def sleep(self):
        print(self.name + " is sleeping.")

    def work(self):
        print(self.name + " is working.")


p = Person("Tom", 20)
print("姓名："+p.name)
print("年龄："+str(p.age))
p.sleep()
p.work()
