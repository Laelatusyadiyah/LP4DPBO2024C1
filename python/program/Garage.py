from Car import Car
from Motorcycle import Motorcycle


class Garage:

    # deklarasi private atribut
    __nama = ""
    __luas = ''
    # composite class Motorcycle dan Car
    # __motor = Motorcycle()
    # __mobil = Car()
    __dfmotor = [] # array of object motor
    __dfmobil = [] # array of object mobil

    # constructor dengan parameter

    def __init__(self, nama="", luas='', dfmotor=[], dfmobil=[]):
        self.__nama = nama
        self.__luas = luas
        # self.__motor = motor
        # self.__mobil = mobil
        self.__dfmotor = dfmotor
        self.__dfmobil = dfmobil

    # setter dan getter untuk masing masing attribut
    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama
        
    def get_luas(self):
        return self.__luas

    def set_luas(self, luas):
        self.__luas = luas
        
    # def get_motor(self):
    #     return self.__motor

    # def set_motor(self, motor):
    #     self.__motor = motor
        
    # def get_mobil(self):
    #     return self.__mobil

    # def set_mobil(self, mobil):
    #     self.__mobil = mobil
        
    def get_dfmotor(self):
        return self.__dfmotor

    def set_dfmotor(self, dfmotor):
        self.__dfmotor = dfmotor
        
    def get_dfmobil(self):
        return self.__dfmobil

    def set_dfmobil(self, dfmobil):
        self.__dfmobil = dfmobil