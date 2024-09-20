n = int(input("n ni kiriting: "))

summ = 0
raqam = 0
belgi = ""

for i in range(1, n+1):
    raqam = raqam * 10 + 2
    summ += raqam
    belgi += str(raqam)
    if i != n:
        belgi += " + "

print(f"{belgi} = {summ}")