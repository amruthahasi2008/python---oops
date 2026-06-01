class robots :
    def __init__(self, name):
        self.name = name

tom = robots('Tom')
jerry = robots('Jerry')

print("Hi my name is {} ".format(tom.name))
print("Hi my name is {} ".format(jerry.name))

