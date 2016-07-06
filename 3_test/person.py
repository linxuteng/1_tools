# -*- coding: utf-8 -*-
__author__= 'linxuteng'


class Person():
    def __init__(self,name,job=None,pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay = int(self.pay *(1 + percent))
        return self.pay
    def __str__(self):
        return '[Person:%s,%s,%s]' %(self.name,self.job,self.pay)
class Manager:
    def __init__(self,name,pay):
        self.person = Person(name,'mgr',pay)
    def giveRaise(self,percent,bonus = 0.10):
        #self.pay = int(self.pay * (1 + percent + bonus))
        self.person.giveRaise(percent + bonus)
    def __getattr__(self,attr):
        return getattr(self.person,attr)
    def __str__(self):
        return str(self.person)
class Department:
    def __init__(self,*args):
        self.members = list(args)
    def addMember(self,person):
        self.members.append(person)
    def giveRaises(self,percent):
        for person in self.members:
            person.giveRaise(percent)
    def showAll(self):
        for person in self.members:
            print(person)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jone', job = 'dev',pay = 100000)
    tom = Manager('Tom Jones',500000)
    tom.giveRaise(0.10)
    print(bob.name,bob.pay)
    print(sue.name,sue.pay)
    print(dir(Person))
    print(dir(bob))
    print(bob.name.split(' '))
    print(bob.lastName())
    print(sue.giveRaise(0.10))
    print(sue)
    print(tom)
    print(tom.lastName())
    print('--ALL three--')
    for object in (bob,sue,tom):
        object.giveRaise(0.10)
        print(object)
    print("-"*8)
    development = Department(bob,sue)
    development.addMember(tom)
    development.giveRaises(0.10)
    development.showAll()
    print(development)

    print(123)