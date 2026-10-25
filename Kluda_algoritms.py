import math

dati = input("Ievadi tiešā mērījumā iegūtos dats: ")
dati = dati.replace(",", ".")

merijumi = []
for skaitlis in dati.split():
    merijumi.append(float(skaitlis))

n = len(merijumi)
videjais_aritmetiskais = sum(merijumi) / n

novirzu_summa = 0
novirzu_kvadratu_summa = 0
for x in merijumi:
    novirze = abs(x - videjais_aritmetiskais)
    novirzes_kvadrats = novirze*novirze
    print(x, "novirze: ", round(novirze, 3), "novirzes kvadrāts", round(novirzes_kvadrats, 5))
    novirzu_summa += novirze 
    novirzu_kvadratu_summa += novirzes_kvadrats
    print("Noviržu kvadrātu summa: ", round(novirzu_kvadratu_summa, 5))

ticamiba = float(input("Ticamības procents: "))
match ticamiba:
    case 90:
        koeficients = [2.920, 2.353, 2.132, 2.015, 1.943, 1.895, 1.860, 1.833, 1.812]
    case 95:
        koeficients = [4.303, 3.182, 2.776, 2.571, 2.447, 2.365, 2.306, 2.262, 2.228]
    case 99:
        koeficients = [9.925, 5.841, 4.604, 4.032, 3.707, 3.499, 3.355, 3.250, 3.169]
    case _:
        koeficients = []

if len(koeficients) == 0:
    print("Koeficienta nav")
elif n < 3 or n > 11:
    print("Šādam mērījumu sakaitam nav atbilstoša Stjudenta koeficienta")
else:
    t = koeficients[n - 3]
    videja_standart_novirze = math.sqrt(novirzu_kvadratu_summa/ n*(n-1))
    absoluta_kluda = t*videja_standart_novirze
    print("Stjudenta koeficients: ", t)
    print("Tiešā mērījumā iegūto lielumu kļūda", videjais_aritmetiskais, "±", round(absoluta_kluda, 5))