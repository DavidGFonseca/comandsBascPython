#Vou iniciar com a frase famosa
print("Olá mundo")

#Diferente de algumas linguegens, o py não tem uma palavra reservada para declarar
#variavel

#Até então não precisa de ; . Indentação é muito importante em py

#Tipo de dados flexivel, mas vc pode determinar via conversão explicida

x = str(3)
y = int(3)
z = float(3)

print(type(x))
print(type(y))
print(type(z))

#Nas strings podem usar aspas simples ou duplas, e py é CASE SENSITIVE

#Para definição do nome de variaveis existe alguns padroes de boas praticas

#Camel Case
myVariavelCamelCase = 'Ok'
#Pascal Case
MyVariavelPascalCase = "Ok"
#Snake Case
my_variavel_snake_case = 'Ok'

#Py tem escopo global e local - semelhante ao JS
#Obs. Interessante que pode ser criado uma variavel global dentro da função
#utilizando da palavra reservada ---global--- 

def myFunc():
    global t
    t = 'var. global'

myFunc()
print(t)

#alterando valor de uma variavel glogal dentro da função

def altValue():
    global x
    x = 'valor alterado'

altValue()
print(x)

#Tipo de dados
texto = str('David')
numeroInt = int(10)
numeroFloat = float(10.0)
numeroComplex = complex(10j)

#para atribuir um texto mais de 1 linha pode usar ''' ou """
#para saber o tamanho de uma string usa o len()

print(len(x))

#Para saber se uma palavra,frase esta inserida em um texto pode usar o in

print('valor' in x)
print('David' not in texto)

#fatiar uma string

print(texto[1:3])
print(texto[:3])
print(texto[-3:])

#Deixar tudo maiusculo
print(texto.upper())
#Deixar tudo minusculo
print(texto.lower())
#removendo espaços no inicio
print(x.strip())
#Substituindo
print(texto.replace('D','F'))
#Dividindo
print(x.split(' '))
