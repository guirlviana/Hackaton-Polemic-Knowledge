decisao = str(input("Converter Cº ou Fº? [C/F] ")).strip().upper()
if decisao == "C":
    cel = float(input('Informe a temperatura em ºC: '))
    fah = cel * 1.8 + 32
    print(f'A temperatura de {cel:.1f}ºC corresponde a {fah:.1f}ºF!')
else:
    fah = float(input('Informe a temperatura em ºF: '))
    cel = (fah -32) / 1.8
    print(f'A temperatura de {cel:.1f}ºC corresponde a {fah:.1f}ºF!')