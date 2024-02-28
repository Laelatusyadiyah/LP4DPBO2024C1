# import class file
from Car import Car
from Garage import Garage
from Motorcycle import Motorcycle
from ParkingLot import ParkingLot
from Vehicle import Vehicle

# instansiasi objek mobil
bmw = Car("B421FR", "BMW", '2020', "Red", '2', '2')
toyota = Car("D45JK", "TOYOTA", '2018', "Gray", '4', '8')
tesla = Car("B11PP", "TESLA", '2023', "Blue", '2', '2')
ford = Car("E24RK", "FORD", '2020', "White", '4', '5')
hyundai = Car("L45JL", "HYUNDAI", '2021', "Black", '4', '8')

# instansiasi objek motor
honda = Motorcycle("D12QW", "HONDA", '2020', "Red", "Scooter", '4')
yamaha = Motorcycle("E23ER", "YAMAHA", '2018', "Blue", "Cub", '4')
suzuki = Motorcycle("F34RT", "SUZUKI", '2021', "Black", "Scooter", '4')
kawasaki = Motorcycle("H56TY", "KAWASAKI", '2021', "Red", "Sport", '7')

# instansiasi objek Garage
mall = Garage("Perbelanjaan Modern", '500', [yamaha, suzuki, kawasaki, honda], [bmw, tesla, ford, hyundai, toyota])
home = Garage("Rumah", '8', [honda, kawasaki], [hyundai])
market = Garage("Perbelanjaan Tradisional", '300', [yamaha, suzuki, honda], [bmw, tesla, ford])
store = Garage("Perbelanjaan Modern", '20', [yamaha, suzuki], [bmw, tesla, ford])

# bikin list of object parking
list_parking = []

# instansiasi objek ParkingLot
luas = ParkingLot('15', '100', [mall, market])
list_parking.append(luas)
sempit = ParkingLot('8', '20', [home, store])
list_parking.append(sempit)

# menampilkan list parking
print("==>", "List Kendaraan".center(60), "<==\n")

# looping objek parking pada list_parking
for i, parking in enumerate(list_parking):
    # print nama dan kode parking
    print(f"""{i+1}.  Jumlah Saat ini       : {parking.get_jumlah_saatini()}
    Kapasitas Kendaraan   : {parking.get_kapasitas()}
    List Kendaraan        : """)
    # looping list objek kendaraan yang dimiliki tempat parkir tersebut
    for j, garage in enumerate(parking.get_Garage()):
        print(f"""
    {j+1}.  Nama Garasi         : {garage.get_nama()}
        Luas Garasi         : {garage.get_luas()}
        Kendaraan Bermotor  :""")
        # looping objek motor di dalam list dfmotor
        for k, motor in enumerate(garage.get_dfmotor()):
            print(f"""
        {k+1}.  Plat            : {motor.get_plat()}
            Merk            : {motor.get_merk()}
            Tahun           : {motor.get_tahun()}
            Warna           : {motor.get_warna()}
            Jenis           : {motor.get_jenis_motor()}
            Kapasitas Tangki: {motor.get_kapasitas_tangki()}""")
        
        print("""
    Kendaraan Mobil  :""")
        # looping objek mobil di dalam list dfmobil
        for l, mobil in enumerate(garage.get_dfmobil()):
            print(f"""
        {l+1}.  Plat            : {mobil.get_plat()}
            Merk            : {mobil.get_merk()}
            Tahun           : {mobil.get_tahun()}
            Warna           : {mobil.get_warna()}
            Jumlah Kursi    : {mobil.get_jumlah_kursi()}
            Jumlah Pintu    : {mobil.get_jumlah_pintu()}""")
