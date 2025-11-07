#1. Adatok beolvasa listaban
adatok=[] 
with open ("data.txt", "r", encoding="utf-8") as fin:
    for sor in fin:
        adatok.append(int(sor))
print(adatok)

#2. Adatok átlaga
atlag=sum(adatok)/len(adatok)
print(f"Átlaga: {atlag:.2f}")

#3. dontsuk el hogy volt e 4
#4. keressuk meg volt e 5
#5.hany darab kilences volt?
#6. Mennyi a legnagyobb beirt szam?
#7. Hanyadik indexen van a legkisebb elem?
#8. paros szamok kiirasa 