'''class Point():
    def __init__(self,x,y):#CONSTRUTOR
        self.x = x #VARIAVEIS 
        self.y = y#VARIAVEIS 
        
    def calc(self):#FUNÇÃO
        return self.x*self.y

ponte1 = Point(10,3)
print(ponte1.calc())

#EXERCICIOS

class NumberSet():
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2


t = NumberSet(6,10)
print(t)


class Poit():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

point1 = Poit(10,2)

#FUNÇÃO 

class Animal():
    def __init__(self,arms, legs):
        self.arms = arms
        self.legs = legs
        
    def limbs(self):
        return self.arms + self.legs
        
animal = Animal(4,5)
spider = Animal(4,4)
spidlimbs = spider.limbs()
print(spidlimbs)

'''
cityNames = ["são paulo", "brasilia","bahia","rio de janeiro"]
populations = [10000,43223,456664,54]
estados = ["Sp","Df","BA","Rj"]

tupla_cidade = zip(cityNames,populations,estados)

class City:
    def __init__(self,n,p,s):
        self.name = n
        self.population = p
        self.state = s
        
    def __str__(self):
        return ("{} ,{} ,{}".format(self.name, self.population, self.state))

cities = []

for item in tupla_cidade:
    nome,populacao,estados = item
    city = City(nome,populacao,estados)
    print(city)