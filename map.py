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