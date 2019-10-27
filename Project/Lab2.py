a = input("masukan nilai a:")
b = input("masukan nilau b:")
print("variabel a =", a)
print("variabel b =", b)
print('hasil penggabungan {1} & {0} = %d'.format(a, b))

a = int(a)
b = int(b)

print('hasil penjumlahan {1} & {0} = %d'.format(a, b) % (a + b))
print('hasil pembagian {0} & {1} = %d'.format(a, b) % (a / b))