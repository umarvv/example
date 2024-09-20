soz = input("So'zni kiriting: ")
harf = input("Harfni kiriting: ")

natija = ""
for belgi in soz:
    if belgi == harf:
        natija += belgi.upper()
    else:
        natija += belgi

print(natija)