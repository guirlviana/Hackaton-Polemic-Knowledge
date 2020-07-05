numeral = str(input("Digite um algarismo romano: ")).upper().replace(" ", "")
total = 0
for romano in numeral:
    if 'I' in romano:
        total += 1
    if 'V' in romano:
        total += 5
    if 'X' in romano:
        total += 10
    if 'L' in romano:
        total += 50
    if 'C' in romano:
        total += 100
    if 'D' in romano:
        total += 500
    if 'M' in romano:
        total += 1000

print(total)

