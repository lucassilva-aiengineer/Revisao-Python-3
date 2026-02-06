import random 
from string import ascii_lowercase, ascii_uppercase 
from typing import List, Dict 


# id_ = ""
letras: List[str] = []


letras += ascii_lowercase + ascii_uppercase
lista_id = [str(random.randint(0, 9)) if random.randint(0, 1) == 0 else random.choice(letras) for numero in range(10)] 

# for numero in numeros:
#     id_ += str(numero) 

# letras += ascii_lowercase + ascii_uppercase

# print(id_) 

# print(letras)
# id_ += str(numeros) 

id_ = "".join(lista_id)


print(id_)

gerar_id = lambda nome : nome + "_" + ''.join([str(random.randint(0, 9)) if random.randint(0, 1) == 0 else random.choice(letras) for _ in range(10)])

print(gerar_id("Marcos"))