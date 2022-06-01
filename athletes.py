nome = str(input('Informe o nome do atleta ou FIM para encerrar: '))
idade = int(input('informar idade: '))
altura = float(input('informar altura'))
peso = float(input('informar peso: '))
sexo = str(input('informar sexo: ')) 
cont = int
media = float
alto = float
pesado = float
soma = float
nalto = str
npesado = str

media == 0
cont ==0
alto == 0 
pesado == 0
nalto == " "
npesado == " "

while nome == 'fim':
    soma =+ 1
    cont =+ 1
    if sexo == 'm' or sexo == 'M':
        if altura > alto:
            alto == altura
            nalto == nome
    if sexo == 'f' or sexo == 'F':
        if peso > pesado:
            pesado == peso
            npesado == nome
        print(input('informe o nome do atleta ou fim: '))
        print('o nome do atleta mais alto:', nalto)
        print('o nome do atleta mais pesado é: ', npesado)