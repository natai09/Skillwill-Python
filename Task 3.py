class Car:
    def __init__(self, brand, model, production_year, color, horse_power, is_sport_car = False):
        self.__brand = brand
        self.__model = model
        self.__production_year = production_year
        self.__color = color
        self.__horse_power = horse_power
        self.__is_sport_car = is_sport_car

    def get_brand(self):
        return self.__brand
    def get_model(self):
        return self.__model
    def get_production_year(self):
        return self.__production_year
    def get_color(self):
        return self.__color
    def get_horse_power(self):
        return self.__horse_power
    def get_is_sport_car(self):
        return self.__is_sport_car

    def change_color(self,new_color):
        if new_color == self.__color:
            return False
        else:
            self.__color = new_color
            return True
    def increase_horse_power (self, hp):
        if hp > 0:
            self.__horse_power +=hp
            return True
        else:
            return False

if __name__=='__main__':

    Car1 = Car('Volga', 'Gaz_21', 1990, 'white',110)
    print(Car1.increase_horse_power(50))
    print (Car1.get_horse_power())
    # if Car1.change_color('black'):
    #     print(f'I am {Car1.get_color()} now')
    print (f'I am {Car1.get_color()} now' if Car1.change_color('ppp') else '0')

    Car2 = Car ('Volga2', 'Gaz_23', 1991, 'yellow',115)
    