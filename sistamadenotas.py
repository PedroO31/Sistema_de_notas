from pickle import TRUE


def lin(msg):
    print('-'*30)
    print(msg)
    print('-'*30)

def media():
    s = n1 + n2
    m = s/2
    print('Média: {}'.format(m))


while TRUE:
    lin('SISTEMA DE MÉDIAS DE NOTAS')
    n1 = int(input('Primeira nota: '))
    n2 = int(input('Segunda nota: '))
    media()