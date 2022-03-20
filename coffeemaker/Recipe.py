from typing import Final
from RecipeException import RecipeException
class Recipe:
    def __init__(self):
        self.__name=""
        self.__price=0
        self.__amtCoffee=0
        self.__amtMilk=0
        self.__amtSugar=0
        self.__amtChocolate=0
    def getAmtChocolate(self):
        return self.__amtChocolate
    def setAmtChocolate(self,chocolate):
        amtChocolate=0
        try:
            amtChocolate=int(chocolate)
            if amtChocolate >= 0:
                self.__amtChocolate = amtChocolate
            else:
                raise RecipeException("Units of chocolate must be a positive integer")
        except ValueError as e:
            raise RecipeException("Units of chocolate must be a positive integer")




    def getAmtCoffee(self):
        return self.__amtCoffee
    def setAmtCoffee(self,coffee):
        amtCoffee = 0
        try:
            amtCoffee = int(coffee)
            if amtCoffee >= 0:
                self.__amtCoffee = amtCoffee
            else:
                raise RecipeException("Units of coffee must be a positive integer")
        except ValueError as e:
            raise RecipeException("Units of coffee must be a positive integer")


    def getAmtMilk(self):
        return self.__amtMilk
    def setAmtMilk(self,milk):
        amtMilk=0
        try:
            amtMilk=int(milk)
            if amtMilk >= 0:
                self.__amtMilk = amtMilk
            else:
                raise RecipeException("Units of milk must be a positive integer")

        except ValueError as e:
            raise RecipeException("Units of milk must be a positive integer")


    def getAmtSugar(self):
        return self.__amtSugar
    def setAmtSugar(self,sugar):
        amtSugar=0
        try:
            amtSugar=int(sugar)
            if amtSugar >= 0:
                self.__amtSugar = amtSugar
            else:
                raise RecipeException("Units of sugar must be a positive integer")
        except ValueError as e:
            raise RecipeException("Units of sugar must be a positive integer")


    def getName(self):
        return self.__name
    def setName(self,name):
        if name!=None:
            self.__name=name

    def getPrice(self):
        return self.__price
    def setPrice(self,price):
        amtPrice=0
        try:
            amtPrice=int(price)
            if amtPrice >= 0:
                self.__price = amtPrice
            else:
                raise RecipeException("Price must be a positive integer")
        except ValueError as e:
            raise RecipeException("Price must be a positive integer")

    def __repr__(self):
        return f'{self.__name}'
    def __hash__(self):
        return 0 if self.__name==None else  (self.__name.__hash__())


    def __eq__(self, other):
        if other==None:
            return False
        if not isinstance(other,Recipe):
            return False
        if self.__name!=other.__name:
            return False
        return True
