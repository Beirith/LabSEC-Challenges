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

# Função que converte valores binários para hexadecimal.
def conversaoBinarioParaHex(binario):
    hex = []
    resultadoFinal = ""
    for i in range(int((len(binario))/4)):
        valor4Bits = 0
        for j in range(4):
            indice = (j - 3) * (-1)
            dadoBit = binario[j + i * 4] * 2**indice     
            valor4Bits += dadoBit

        if valor4Bits > 9:
            if valor4Bits == 10:
                valor4Bits = 'a'
            if valor4Bits == 11:
                valor4Bits = 'b'
            if valor4Bits == 12:
                valor4Bits = 'c'
            if valor4Bits == 13:
                valor4Bits = 'd'
            if valor4Bits == 14:
                valor4Bits = 'e'
            if valor4Bits == 15:
                valor4Bits = 'f'
        else:
            valor4Bits = str(valor4Bits)
                
        hex.append(valor4Bits)

    for i in range(len(hex)):
        resultadoFinal += hex[i]

    return resultadoFinal

# Função que aplica o XOR entre dois número binários. Neste caso, ambos os números possuem o mesmo tamanho.
def xorFunction(binario1, binario2):
    resposta = []
    binario1 = list(binario1)
    binario2 = list(binario2)

    for i in range(len(binario1)):

        if binario1[i] != binario2[i]:
            resposta.append(1)

        else:
            resposta.append(0)
    
    return resposta

# Main loop
while True:
    print(" ")
    print("Digite duas strings em hexadecimal: ")
    binario1 = list(input())
    binario2 = list(input())

    binario1 = conversaoHexParaBinario(binario1)
    binario2 = conversaoHexParaBinario(binario2)

    resultadoXor = xorFunction(binario1, binario2)

    resultadoFinal = conversaoBinarioParaHex(resultadoXor)

    print("O resultado da função XOR entra as duas strings é: " + str(resultadoFinal))
