import random
import string

senha = random.sample(string.digits + string.ascii_letters, 11)
password = ''.join(map(str,senha))
print(f"Senha: {password}")

