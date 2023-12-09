import Animal


class Cat(Animal.Annimals):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        # self.name = name
        # self.age = age
        self.color = color

    def eat(self):
        print(self.name + " 爱吃鱼.")

    def sleep(self):
        print(self.name + " 喜欢眯着眼睡觉.")

    def work(self):
        print(self.name + " 不爱工作.")


cat = Cat("蓝猫", 18, '白色')
print(cat.name)
print(cat.age)
print(cat.color)
cat.work()
cat.sleep()
cat.eat()
