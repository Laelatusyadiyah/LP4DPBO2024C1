from Vehicle import Vehicle


# deklarasi class
class Motorcycle(Vehicle):

    # deklarasi private atribut
    __jenis_motor = ""
    __kapasitas_tangki = ''

    # constructor dengan parameter

    def __init__(self, plat="", merk="", tahun='', warna="", jenis="", tangki=''):
        super().__init__(plat, merk, tahun, warna)
        self.__jenis_motor = jenis
        self.__kapasitas_tangki = tangki

    # setter dan getter untuk masing masing attribut
    def get_jenis_motor(self):
        return self.__jenis_motor

    def set_jenis_motor(self, jenis):
        self.__jenis_motor = jenis
        
    def get_kapasitas_tangki(self):
        return self.__kapasitas_tangki

    def set_kapasitas_tangki(self, tangki):
        self._kapasitas_tangki = tangki