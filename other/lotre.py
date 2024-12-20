nomor = [
    "89171152",
]

pemenang = ["44140251", "14715309", "86562747", "79171152", "77925523"]



# Cocok dengan nomor pertama

for n in nomor:
    if n == pemenang[0]:
        print(f"\n ======================================= \n   {n} = Special prize\n ======================================= \n")



# Cocok dengan nomor kedua

for n in nomor:
    if n == pemenang[1]:
        print(f"\n ======================================= \n   {n} = Grand prize\n ======================================= \n")



# Cocok dengan nomor ketiga, keempat, atau kelima

for n in nomor:
    for p in pemenang[2:5]:
        if n == p:
            nomor.remove(n)
            print(f"\n ======================================= \n   {n} ~ {p} = First prize\n ======================================= \n")



# 7 digit terakhir cocok dengan salah satu nomor di First prize

for n in nomor:
    for p in pemenang[2:5]:
        if n[1:] == p[1:]:
            nomor.remove(n)
            print(f"\n ======================================= \n   {n} ~ {p} = Second prize\n ======================================= \n")



# 6 digit terakhir cocok dengan salah satu nomor di First prize

for n in nomor:
    for p in pemenang[2:5]:
        if n[2:] == p[2:]:
            nomor.remove(n)
            print(f"\n ======================================= \n   {n} ~ {p} = Third prize\n ======================================= \n")



# 5 digit terakhir cocok dengan salah satu nomor di First prize

for n in nomor:
    for p in pemenang[2:5]:
        if n[3:] == p[3:]:
            nomor.remove(n)
            print(f"\n ======================================= \n   {n} ~ {p} = Fourth prize\n ======================================= \n")



# 4 digit terakhir cocok dengan salah satu nomor di First prize

for n in nomor:
    for p in pemenang[2:5]:
        if n[4:] == p[4:]:
            nomor.remove(n)
            print(f"\n ======================================= \n   {n} ~ {p} = Fifth prize\n ======================================= \n")



# 3 digit terakhir cocok dengan salah satu nomor di First prize

for n in nomor:
    for p in pemenang[2:5]:
        if n[5:] == p[5:]:
            nomor.remove(n)
            print(f"\n ======================================= \n   {n} ~ {p} = Sixth prize\n ======================================= \n")
