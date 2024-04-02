daftarMakanMinuman = ['Lengko','Tea Jus Dan Surya']


pesanan = str(input('Minum dan Makan apa malam ini?? : '))
tempat = str(input('Suasana tempat apa yang anda rasakan saat ini? : '))
jumlah = int(input('Pesan berapa porsi? : '))
harga = int(input('Harga :'))
tambahan = str(input('Ada tambahan apa lagi kak?, kalo tidak ada ketik tidak :'))
bayar = jumlah + harga

if pesanan not in daftarMakanMinuman:
    print('JANGAN MAKAN DULU YA ini lagi puasaa , minuman : {pesanan} tempat : {tempat} total harga : {bayar}')
else:
    print(f'Mari kita kenyangin perut : {pesanan} tempat : {tempat} total harga : {bayar} tambahan costumer : {tambahan}')