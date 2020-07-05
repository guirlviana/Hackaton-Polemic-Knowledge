romano = input("Digite um número: ").strip().upper()
romanos = {'I': 1, 'V': 5, 
        'X': 10, 'L': 50, 
        'C': 100, 'D': 500, 'M': 1000}
num = 0

for i in range(len(romano)):
    if i > 0 and romanos[romano[i]] > romanos[romano[i - 1]]: # numeral na posição i for maior que o seu anterior (i -1) 
        num += romanos[romano[i]] - 2 * romanos[romano[i - 1]]
    else:
        num += romanos[romano[i]] # numeral anterior for menor que o sucessor (1+i)
    


print(num) 



