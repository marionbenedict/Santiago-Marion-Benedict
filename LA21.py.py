class Favorite_food():
    def __init__(self,name,main_ingredient,onion,carrot,):
        self.__name = name
        self._main_ingredient = main_ingredient
        self.__onion = onion
        self._carrot = carrot

    def __str__(self):
        return f"my favorite food is {self.__name} and the mian ingredient {self._main_ingredient}, {self.__onion}, {self._carrot}"
    def getter(self,age):
        if age >= 15:
            return f"The mian ingredient {self._main_ingredient}, {self.__onion}, {self._carrot}"
        else:
            return "invalid"
food = Favorite_food("lumpia_shanghai", "baboy" , "sibuyas" , "karot")
print(food.getter(11))