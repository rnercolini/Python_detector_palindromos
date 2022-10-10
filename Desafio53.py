# Verifica se a frase é um palíndromo.
frase = str(input('Digite uma frase: ')).strip().upper()
junta = frase.replace(' ', '')
vira = junta[::-1]
print('A frase \033[34m{}\033[m escrita ao contrário é \033[34m{}\033[m.'.format(junta, vira))
if junta == vira:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo')
