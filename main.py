#1. Adatok beolvasa listaban
adatok=[] 
with open ("data.txt", "r", encoding="utf-8") as fin:
    for sor in fin:
        adatok.append(int(sor))
print(adatok)

#2. Adatok átlaga
atlag=sum(adatok)/len(adatok)
print(f"Átlaga: {atlag:.2f}")

#3. dontsuk el hogy volt e 4?
van=False
for szam in adatok:
    if szam==4: 
        van=True
        break

if van:
    print("van 4-es")
else:
    print("nincs 4-es")

#4. keressuk meg volt e 5
van5=False
for i in range(len(adatok)):
    if adatok[i]==5:
        van5=True
        break

if van5:
    print(f"Van 5-ös és a(z) {i}. elem")
else:
    print("Nincs 5-ös")

#5.hany darab kilences volt?
db=0
for szam in adatok: 
    if szam == 9:
        db+=1
print(f"{db} darab kilences van." ) 

#6. Mennyi a legnagyobb beirt szam?
legnagyobb_szam=adatok[0]
for szam in adatok:
    if szam>legnagyobb_szam:
        legnagyobb_szam = szam
print(f"A legnagyobb szám: {legnagyobb_szam}")

#7. Hanyadik indexen van a legkisebb elem?
minindex=adatok[0]
helye=adatok[0]
for i in range(len(adatok)):
    if adatok[i]<minindex:
        minindex=adatok[i]
        helye=i

print(f"A legkisebb elem a(z) {minindex} és a(z) {helye}. elem")
    
#8. paros szamok kiirasa paros txt.be
with open("paros.txt", "w", encoding="utf-8") as f:
    for szam in adatok:
        if szam % 2 == 0:      
            f.write(f"{szam}\n")