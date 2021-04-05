koefisien = [
            {
                "Unit Pembangkit": "IC#1",
                "a": 15.59,
                "b": 443872.57,
                "c": 8854230.19
            },
            {
                "Unit Pembangkit": "IC#2",
                "a": 432.52,
                "b": 228835.28,
                "c": 26186478.79
            },
            {
                "Unit Pembangkit": "IC#3",
                "a": 928.68,
                "b": -130876.67,
                "c": 81788363.85
            }
        ]
min_daya_unit = 200
max_daya_unit = 315
global w0
w0 = 400000
global loop
loop = "y"

def hitungbebanunit(input):
    global totalp
    totalp = 0
    print("W0 :", w0)
    for i in koefisien:
        p = (w0 - i['b']) / (2 * i['a'])
        print("P :", p)
        if p < min_daya_unit:
            p = min_daya_unit
        else:
            p = max_daya_unit
        totalp += p
        tampilp(p, i['Unit Pembangkit'])
    return True

def cekBeban():
    global totala
    global dp
    totala = 0
    dp = inputanbeban - totalp
    print("DP :", dp)
    if dp == 0:
        print("P1 :", p1, "P2 : ", p2, "P3 : ", p3)
        return True
    else:
        for a in koefisien:
            totala += 1/2*a['a']
        return False

def hitungW():
    w = w0 + dp / totala
    return w

def tampilp(nilai,unit):
    global p1
    global p2
    global p3
    if unit == "IC#1":
        p1 = 0
        p1 = nilai
    elif unit == "IC#2":
        p2 = 0
        p2 = nilai
    else:
        p3 = 0
        p3 = nilai

def hitung():
    hasilw = hitungW()
    w0 = hasilw
    hitungbebanunit(inputanbeban)
    hasilcek = cekBeban()
    if hasilcek == False:
        loop = "y"
    else:
        loop = "t"
    return False

print("==== PAGE AWAL =====")
inputanbeban = int(input("Masukan Beban Unit : "))

hasil = hitungbebanunit(inputanbeban)
hasilcek = cekBeban()
if hasilcek == False:
    while loop == "y":
        hasilw = hitungW()
        w0 = hasilw
        hitungbebanunit(inputanbeban)
        hasilcek = cekBeban()
        if hasilcek == False:
            loop = "y"
        else:
            loop = "t"
else:
    print("SELESAI")