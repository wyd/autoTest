import day02_object.Animal


class Dog(day02_object.Animal.Annimals):

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.name = name
        self.age = age
        self.color = color

    def eat(self):
        print(self.name + "爱吃骨头")

    def sleep(self):
        print(self.name + "喜欢躺着睡")

    def work(self):
        print(self.name + "不爱工作")


dog = Dog("大黄", 20, '黑色')
print(dog.name)
print(dog.age)
print(dog.color)
dog.work()
dog.sleep()
dog.eat()
