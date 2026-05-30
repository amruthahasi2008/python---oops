class parrot :

    def __init__(self, name , age):
        self.name = name 
        self.age = age


    def sing (self , song) :
        return '{} is singing {}'.format(self.name,song)
    
    def dance (self) :
        return '{} is dancing'.format(self.name)
    

blu = parrot('blu',10)

print(blu.sing('happy'))
print(blu.dance())

        

        