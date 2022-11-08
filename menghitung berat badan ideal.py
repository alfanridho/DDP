#program menghitung berat badan ideal
#input
TinggiBadan = input('masukkan tinggi badan = ')

#rumus
BeratBadanIdeal = (int(TinggiBadan) - int(100)) - (int(TinggiBadan) - int(100)) * int(10)/int(100)

#output
print ('berat badan ideal anda adalah =', BeratBadanIdeal)