# Normal:  ABCDEFGHIJKLMNOPQRSTUVWXYZ[1]
# Cifrado: DEFGHIJKLMNOPQRSTUVWXYZABC[1]

dict = {
    " " : " ",
    "A" : "D",
    "B" : "E",
    "C" : "F",
    "D" : "G",
    "E" : "H",
    "F" : "I",
    "G" : "J",
    "H" : "K",
    "I" : "L",
    "J" : "M",
    "K" : "N",
    "L" : "O",
    "M" : "P",
    "N" : "Q",
    "O" : "R",
    "P" : "S",
    "Q" : "T",
    "R" : "U",
    "S" : "V",
    "T" : "W",
    "U" : "X",
    "V" : "Y",
    "W" : "Z",
    "X" : "A",
    "Y" : "B",
    "Z" : "C",
}

text = input("Qual o texto? ")
print (f"Texto: {text}")

cifra = ""
for c in text:
    cifra += dict[c.upper()]

print (f"Cifra de cesar: {cifra}")