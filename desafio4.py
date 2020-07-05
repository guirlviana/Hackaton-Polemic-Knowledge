import re
cpf_usuario = str(input("Digite o cpf: "))

numbers = [int(digito) for digito in cpf_usuario if digito.isdigit()]
soma1 = sum(pos*num for pos, num in zip(numbers[0:9], range(10, 1, -1)))
result1 = (soma1 * 10 % 11) % 10

numbers = [int(digito) for digito in cpf_usuario if digito.isdigit()]
soma2 = sum(pos*num for pos, num in zip(numbers[0:10], range(11, 1, -1)))
result2 = (soma2 * 10 % 11) % 10

if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf_usuario) or cpf_usuario[-1] != result1 or cpf_usuario[-2] != result2:
    print("Invalido")
else:
    print("Valido")




