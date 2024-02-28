class ParkingLot:

    # deklarasi private atribut
    __jumlah_saatini = ''
    __kapasitas = ''
    # composite kelas Garage
    __Garage = []  # array of object garage
    

    # constructor dengan parameter

    def __init__(self, jumlah='', kapasitas='', Garage=[]):
        self.__jumlah_saatini = jumlah
        self.__kapasitas = kapasitas
        self.__Garage = Garage
        
    # setter dan getter untuk masing masing attribut
    def get_jumlah_saatini(self):
        return self.__jumlah_saatini

    def set_jumlah_saatini(self, jumlah):
        self.__jumlah_saatini = jumlah
        
    def get_kapasitas(self):
        return self.__kapasitas

    def set_kapasitas(self, kapasitas):
        self._kapasitas = kapasitas
        
    def get_Garage(self):
        return self.__Garage

    def set_Garage(self, Garage):
        self.__Garage = Garage
        