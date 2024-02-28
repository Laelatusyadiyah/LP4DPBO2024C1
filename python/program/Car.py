from Vehicle import Vehicle


# deklarasi class
class Car(Vehicle):

    # deklarasi private atribut
    __jumlah_kursi = ''
    __jumlah_pintu = ''

    # constructor dengan parameter

    def __init__(self, plat="", merk="", tahun='', warna="", pintu='', kursi=''):
        super().__init__(plat, merk, tahun, warna)
        self.__jumlah_kursi = kursi
        self.__jumlah_pintu = pintu

    # setter dan getter untuk masing masing attribut
    def get_jumlah_kursi(self):
        return self.__jumlah_kursi

    def set_jumlah_kursi(self, kursi):
        self.__jumlah_kursi = kursi
        
    def get_jumlah_pintu(self):
        return self.__jumlah_pintu

    def set_jumlah_pintu(self, pintu):
        self._jumlah_pintu = pintu
    
 