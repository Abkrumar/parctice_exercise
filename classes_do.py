class Cat:
    '''producing cat profile'''
    def __init__(self, name, age, group):
        self.group = group
        self.name = name
        self.age = age
        print(f'{self.name} is sitting')
        print(f'{self.name} is {self.age} years old')
        print(f'I love my {self.age} years old {self.name}')
        print(f'{self.name} is  an {self.group}')


name = input("Name: \n")
Age = 3
group = "animals"
Cat(name, Age, group)


class restaurant:
    '''describin restaurant'''
    def __init__(self, restaurant_name, cuisin_type):
        self.r_n = restaurant_name
        self.c_t = cuisin_type
        print(f'the name of this restaurant is {self.r_n}')
        print(f'the type of cuissin in this restaurats is  {self.c_t}')
        print(f'{self.r_n} is open')


restaurant_name = ("Uwar Tuwo")
cuisin_type = ("kujeru")
restaurant(restaurant_name, cuisin_type)


class restaurant_2(restaurant):
    '''inheritance from class restaurant'''
    def __init__(self, restaurant_name, cuisin_type):
        super().__init__(restaurant_name, cuisin_type)


name_3 = ("Dadi restaurant")
kujeru_2 = ("Laushi kujeru")
restaurant_2(name_3, kujeru_2)
