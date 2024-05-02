class Map:
    def _init_(self):
        self.daftarkota = {}

    def tambahkankota(self,kota):
        if kota not in self.daftarkota:
            self.daftarkota[kota] = []
            return True
        return False
    
    def hapusKota(self,kotadihapus):
        #mengecek apakah kota yang akan dihaous terdapat dalam list
        if kotadihapus in self.daftarkota:
            for kota2 in self.daftarkota:
            #mengecek apakah terdapat jalur ke kota2
                if kotadihapus in self.daftarkota[kota2]:
                    self.daftarkota[kota2].remove(kotadihapus)
            del self.daftarkota[kotadihapus]
            return True
        return False
    
    #fungsi untuk menghubungkan antara kota 1 dan kota 2
    def tambahkanjalur(self,kota1,kota2):
        if kota1 in self.daftarkota and kota2 in self.daftarkota:
            #menambahkan kota1 ke dalam list kota2
            self.daftarkota[kota2].append(kota1)
            #menambahkan kota2 ke dalam list kota1
            self.daftarkota[kota1].append(kota2)
            return True
        return False

    #fungsi untuk menghapus jalur antara kota 1 dan kota 2
    def hapusjalur(self,kota1,kota2):
        if kota1 in self.daftarkota and kota2 in self.daftarkota:
            #hapus kota 1 di list kota2
            self.daftarkota[kota2].remove(kota1)
            #hapus kota 2 di list kota1
            self.daftarkota[kota1].remove(kota2)
            return True
        return False
        
    
    def printMap(self):
        for kota in self.daftarkota:
            print(kota, ":",self.daftarkota[kota])
        

MapKota = Map()
MapKota.tambahkankota("Surabaya")
MapKota.tambahkankota("Sidoarjo")
MapKota.tambahkankota("Madiun")
MapKota.tambahkankota("Kediri")
MapKota.tambahkankota("Lamongan")
MapKota.tambahkankota("Nganjuk")
MapKota.tambahkankota("Gresik")
MapKota.tambahkankota("Malang")
MapKota.tambahkankota("Mojokerto")
MapKota.tambahkankota("Pasuruan")
MapKota.tambahkankota("Probolinggo")
MapKota.tambahkankota("Ponorogo")
MapKota.tambahkankota("Blitar")
MapKota.tambahkankota("Tulungagung")
MapKota.tambahkankota("Trenggalek")
MapKota.tambahkankota("Ngawi")
MapKota.tambahkankota("Bojonegoro")
MapKota.tambahkankota("Batu")
MapKota.tambahkanjalur("Surabaya","Sidoarjo")
MapKota.tambahkanjalur("Surabaya","Gresik")
MapKota.tambahkanjalur("Mojokerto","Sidoarjo")
MapKota.tambahkanjalur("Gresik","Sidoarjo")
MapKota.tambahkanjalur("Mojokerto","Gresik")
MapKota.tambahkanjalur("Mojokerto","Madiun")
MapKota.tambahkanjalur("Mojokerto","Batu")
MapKota.tambahkanjalur("Lamongan","Madiun")
MapKota.tambahkanjalur("Nganjuk","Madiun")
MapKota.tambahkanjalur("Kediri","Nganjuk")
MapKota.tambahkanjalur("Pasuruan","Sidoarjo")
MapKota.tambahkanjalur("Kediri","Tulungagung")
MapKota.tambahkanjalur("Tulungagung","Blitar")
MapKota.tambahkanjalur("Blitar","Trenggalek")
MapKota.tambahkanjalur("Trenggalek","Ponorogo")
MapKota.tambahkanjalur("Ponorogo","Madiun")
MapKota.tambahkanjalur("Madiun","Ngawi")
MapKota.tambahkanjalur("Lamongan","Gresik")
MapKota.tambahkanjalur("Pasuruan","Probolinggo")
MapKota.tambahkanjalur("Lamongan","Bojonegoro")
MapKota.tambahkanjalur("Bojonegoro","Ngawi")
MapKota.tambahkanjalur("Malang","Batu")
MapKota.tambahkanjalur("Sidoarjo","Malang")
MapKota.tambahkanjalur("Blitar","Malang")
MapKota.tambahkanjalur("Kediri","Mojokerto")
MapKota.tambahkanjalur("Kediri","Batu")
MapKota.tambahkanjalur("Surabaya","Mojokerto")
MapKota.tambahkanjalur("Malang","Pasuruan")
MapKota.tambahkanjalur("Kediri","Trenggalek")
MapKota.tambahkanjalur("Mojokerto","Bojonegoro")

print('==================================')
MapKota.printMap()
print('==================================')
#MapKota.hapusjalur("Daedong-Ri","Songak-Ri")
MapKota.hapusKota("Madiun")
MapKota.printMap
