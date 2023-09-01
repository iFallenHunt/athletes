name = str(input("Enter the athlete's name or END to close: "))
age = int(input('inform age: '))
height = float(input('inform height: '))
weight = float(input('inform weight: '))
gender = str(input('inform gender: ')) 
cont = int
media = float
tall = float
heavy = float
addition = float
ntall = str
nheavy = str

media == 0
cont ==0
tall == 0 
heavy == 0
ntall == " "
nheavy == " "

while name == 'fim':
    addition =+ 1
    cont =+ 1
    if gender == 'm' or gender == 'M':
        if height > tall:
            tall == height
            ntall == name
    if gender == 'f' or gender == 'F':
        if weight > heavy:
            heavy == weight
            nheavy == name
        print(input('informe o nome do atleta ou fim: '))
        print('o nome do atleta mais tall:', tall)
        print('o nome do atleta mais pesado é: ', nheavy)