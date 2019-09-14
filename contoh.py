class kalkulator:
    pass


    def __init__(self):
        self.satu=1
        self.dua=2
        self.tiga=3
        self.empat=4
        self.lima=5
        self.enam=6
        self.tujuh=7
        self.delapan=8
        self.sembilan=9


    def tambah(self,up1,up2):
        return up1+up2

    def kurang(self,up1,up2):
        return up1-up2

    def kali(self,up1,up2):
        return up1*up2


    def bagi(self,up1,up2):
        return up1/up2



angka=kalkulator()

print(angka.tambah(8,9))
print(angka.kurang(8,2))
print(angka.kali(8,4))
print(angka.bagi(9,3))