def func(n):
    for i in range(1, n+1):
        sonlar = list(range(1, n+1))
        yigindi = sum(sonlar)
        natija =  ' + '.join(map(str, sonlar))
    print(f"{natija} = {yigindi}")

n = int(input("Sonnni kiriting: "))

func(n)
