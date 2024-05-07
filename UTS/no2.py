def Tahun(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

year = int(input("Masukkan tahun: "))

if Tahun(year):
    print(year, "adalah tahun kabisat.")
else:
    print(year, "bukan tahun kabisat.")
