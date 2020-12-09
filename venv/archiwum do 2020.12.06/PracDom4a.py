print("Podaj wysokość pożyczki:")
print("(Wpisz 12000 \"zeta\")")
pozyczka = int(input())
print('''Czyli bierzesz {} złotych. W takim razie czy oprocentowanie wynosi 3%
 w skali roku?'''.format(pozyczka))
print("(Wpisz 3)")
oprocentowanie = float(input())
print('''{}%. OK.
No to podaj jeszcze kwotę miesięcznej raty do spłaty.'''.format(oprocentowanie))
print("(200, wpisz 200!)")
rata = int(input())
print("Dzięki...")
message = "Twoja rata {} PLN.".format(rata)
print(message)
message = "W takim razie, twój harmonogram spłat będzie wyglądał następująco:"
print(message)

y1 = 1.592824484
y2 = -0.453509101
y3 = 2.324671717
y4 = 1.261254407
y5 = 1.782526286
y6 = 2.329384541
y7 = 1.502229842
y8 = 1.782526286
y9 = 2.328848994
y0 = 0.616921348
ya = 2.352295886
yb = 0.337779545
z1 = 1.577035247
z2 = -0.292781443
z3 = 2.48619659
z4 = 0.267110318
z5 = 1.417952672
z6 = 1.054243267
z7 = 1.480520104
z8 = 1.577035247
z9 = -0.07742069
z0 = 1.165733399
za = -0.404186718
zb= 1.499708521

a1 =((1+((y1 + oprocentowanie)/1200)) * int(pozyczka) - rata)
a2 =((1+((y2 + oprocentowanie)/(1200))) * a1 - rata)
a3 =((1+((y3 + oprocentowanie)/(1200))) * a2 - rata)
a4 =((1+((y4 + oprocentowanie)/(1200))) * a3 - rata)
a5 =((1+((y5 + oprocentowanie)/(1200))) * a4 - rata)
a6 =((1+((y6 + oprocentowanie)/(1200))) * a5 - rata)
a7 =((1+((y7 + oprocentowanie)/(1200))) * a6 - rata)
a8 =((1+((y8 + oprocentowanie)/(1200))) * a7 - rata)
a9 =((1+((y9 + oprocentowanie)/(1200))) * a8 - rata)
a0 =((1+((y0 + oprocentowanie)/(1200))) * a9 - rata)
aa =((1+((ya + oprocentowanie)/(1200))) * a0 - rata)
ab =((1+((yb + oprocentowanie)/(1200))) * aa - rata)
b1 =((1+((z1 + oprocentowanie)/(1200))) * ab - rata)
b2 =((1+((z2 + oprocentowanie)/(1200))) * b1 - rata)
b3 =((1+((z3 + oprocentowanie)/(1200))) * b2 - rata)
b4 =((1+((z4 + oprocentowanie)/(1200))) * b3 - rata)
b5 =((1+((z5 + oprocentowanie)/(1200))) * b4 - rata)
b6 =((1+((z6 + oprocentowanie)/(1200))) * b5 - rata)
b7 =((1+((z7 + oprocentowanie)/(1200))) * b6 - rata)
b8 =((1+((z8 + oprocentowanie)/(1200))) * b7 - rata)
b9 =((1+((z9 + oprocentowanie)/(1200))) * b8 - rata)
b0 =((1+((z0 + oprocentowanie)/(1200))) * b9 - rata)
ba =((1+((za + oprocentowanie)/(1200))) * b0 - rata)
bb =((1+((zb + oprocentowanie)/(1200))) * ba - rata)

print("Pozostało do spłaty Styczeń.01 - {} PLN".format(int(a1*100)/100))
print("Pozostało do spłaty Luty.01 - {} PLN".format(int(a2*100)/100))
print("Pozostało do spłaty Marzec.01 - {} PLN".format(int(a3*100)/100))
print("Pozostało do spłaty Kwiecień.01 - {} PLN".format(int(a4*100)/100))
print("Pozostało do spłaty Maj.01 - {} PLN".format(int(a5*100)/100))
print("Pozostało do spłaty Czerwiec.01 - {} PLN".format(int(a6*100)/100))
print("Pozostało do spłaty Lipiec.01 - {} PLN".format(int(a7*100)/100))
print("Pozostało do spłaty Sierpień.01 - {} PLN".format(int(a8*100)/100))
print("Pozostało do spłaty Wrzesień.01 - {} PLN".format(int(a9*100)/100))
print("Pozostało do spłaty Październik.01 - {} PLN".format(int(a0*100)/100))
print("Pozostało do spłaty Listopad.01 - {} PLN".format(int(aa*100)/100))
print("Pozostało do spłaty Grudzień.01 - {} PLN".format(int(ab*100)/100))
print("Pozostało do spłaty Styczeń.02 - {} PLN".format(int(b1*100)/100))
print("Pozostało do spłaty Luty.02 - {} PLN".format(int(b2*100)/100))
print("Pozostało do spłaty Marzec.02 - {} PLN".format(int(b3*100)/100))
print("Pozostało do spłaty Kwiecień.02 - {} PLN".format(int(b4*100)/100))
print("Pozostało do spłaty Maj.02 - {} PLN".format(int(b5*100)/100))
print("Pozostało do spłaty Czerwiec.02 - {} PLN".format(int(b6*100)/100))
print("Pozostało do spłaty Lipiec.02 - {} PLN".format(int(b7*100)/100))
print("Pozostało do spłaty Sierpień.02 - {} PLN".format(int(b8*100)/100))
print("Pozostało do spłaty Wrzesień.02 - {} PLN".format(int(b9*100)/100))
print("Pozostało do spłaty Październik.02 - {} PLN".format(int(b0*100)/100))
print("Pozostało do spłaty Listopad.02 - {} PLN".format(int(ba*100)/100))
print("Pozostało do spłaty Grudzień.02 - {} PLN".format(int(bb*100)/100))
print("")
message = (f'''Po 24. miesiącach spłacania pożyczki na {pozyczka} PLN,
przy oprocentowaniu {oprocentowanie}% i racie w wysokości {rata} PLN,
pozostanie do spłaty {(int(bb*100)/100)}.''')
print(message)
