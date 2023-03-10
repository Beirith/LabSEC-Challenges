# Dicionário utilizado para 'traduzir' a mensagem de binário para base 64.
dictBase64 = {'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H', '8': 'I', '9': 'J', '10': 'K', '11': 'L', '12': 'M', '13': 'N', '14': 'O', '15': 'P',
            '16': 'Q', '17': 'R', '18': 'S', '19': 'T', '20': 'U', '21': 'V', '22': 'W', '23': 'X', '24': 'Y', '25': 'Z','26': 'a', '27': 'b', '28': 'c', '29': 'd', '30': 'e', '31': 'f', 
            '32': 'g', '33': 'h', '34': 'i', '35': 'j', '36': 'k', '37': 'l', '38': 'm', '39': 'n', '40': 'o', '41': 'p','42': 'q', '43': 'r', '44': 's', '45': 't',
            '46': 'u', '47': 'v', '48': 'w', '49': 'x', '50': 'y', '51': 'z', '52': '0', '53': '1', '54': '2', '55': '3', '56': '4', '57': '5', '58': '6', 
            '59': '7', '60': '8', '61': '9', '62': '+', '63': '/'}

# Como é preciso trabalhar com os dados em bytes brutos, inicialmente é necessário converter a entrada de hexadecimal para binário
def conversaoHexParaBinario(hex):
    hex = list(hex)
    binario = []
    valor = 0
    for i in range(len(hex)):       
        if hex[i] == '0':
            valor = '0000'
        elif hex[i] == '1':
            valor = '0001'
        elif hex[i] == '2':
            valor = '0010'
        elif hex[i] == '3':
            valor = '0011'
        elif hex[i] == '4':
            valor = '0100'
        elif hex[i] == '5':
            valor = '0101'
        elif hex[i] == '6':
            valor = '0110'
        elif hex[i] == '7':
            valor = '0111'
        elif hex[i] == '8':
            valor = '1000'
        elif hex[i] == '9':
            valor = '1001'
        elif hex[i] == 'a':
            valor = '1010'
        elif hex[i] == 'b':
            valor = '1011'
        elif hex[i] == 'c':
            valor = '1100'
        elif hex[i] == 'd':
            valor = '1101'
        elif hex[i] == 'e':
            valor = '1110'
        else:
            valor = '1111'

        valor = list(valor)
        for j in range(len(valor)):
            binario.append(int(valor[j]))

    return binario

# Após isso, é realizada conversão de binário para base 64, utilizando um dicionário (dictBase64) para 'traduzir' os valores.
def conversaoBinarioParaBase64(binario):
    vetorcodigo = []

# Primeiro, verifica-se se o número de bits do vetor binario é divisível por 6, pois os valores são lidos e convertidos para decimal de 6 em 6 bits, para depois então 
# utilizar o mesmo valor decimal para encontrar o indice do caractere correspondente em base 64, 'traduzindo' então a mensagem.
    if (len(binario)) % 6 == 0:
        for i in range(int((len(binario))/6)):
            valor6Bits = 0
            for j in range(6):
                indice = (j - 5) * (-1)
                dadoBit = binario[j + i * 6] * 2**indice
                valor6Bits += dadoBit

            vetorcodigo.append(valor6Bits)
    
# Caso o número de bits do vetor binário não seja divisível por 6, 
    else:
        valor6Bits = 0

    resultado = ""

    for i in range(len(vetorcodigo)):
        resultado += dictBase64[str(vetorcodigo[i])]

    print(" ")
    print('A string convertida para base 64 é: ' + resultado)
    return resultado

# Main loop
while True:
    print(" ")
    print("Digite a string em hexadecimal: ")
    entrada = list(input())
    aux = conversaoHexParaBinario(entrada)
    conversaoBinarioParaBase64(aux)