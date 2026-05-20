class Mahasiswa:
    def __init__(self,nama,prodi,fakultas):
        self.nama = nama
        self.prodi = prodi
        self.fakultas = fakultas
    
mhs001 = Mahasiswa("seno","TI","saintek")
mhs002 = Mahasiswa("Budi","HI","Humaniora")
mhs003 = Mahasiswa("Karno","EI","Syariah")
mhs004 = Mahasiswa("Jono","AFI","Ushuluddin")

print(f"nama: {mhs001.nama}, prodi: {mhs001.prodi}, fakultas: {mhs001.fakultas}")
print(f"nama: {mhs002.nama}, prodi: {mhs002.prodi}, fakultas: {mhs002.fakultas}")
print(f"nama: {mhs003.nama}, prodi: {mhs003.prodi}, fakultas: {mhs003.fakultas}")
print(f"nama: {mhs004.nama}, prodi: {mhs004.prodi}, fakultas: {mhs004.fakultas}")

