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

#  Convertendo de binário para hexadecimal
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

# Função que aplica o XOR entre dois número binários. Neste caso, o segundo número binário possui 8 bits.
def xorFunction(binario1, binario2):
    resposta = []
    binario1 = list(binario1)
    binario2 = list(binario2)

    for j in range(len(binario1)):
        bitBinario1 = binario1[j]
        bitBinario2 = int(binario2[j%8])
        if bitBinario1 != bitBinario2:
            resposta.append(1)

        else:
            resposta.append(0)
    
    return resposta

# As 'chaves' são todos as 128 combinações de números binários da tabela ASCII. Criei esta classe para agilizar e deixar mais fácil o entendimento
# e organização do código. Cada 'chave' possui 4 atributos: chave (seu valor em binário de 8 bits), after_xor (seu valor após a operação xor com o código hexadecimal a ser 'traduzido'),
# codigo_gerado (código em ascii que o atributo after_xor gera) e score (valor que mede a possibilidade da chave ser a 'verdadeira').
class Chaves():
    def __init__(self, chave, after_xor, codigo_gerado, score):
        self.chave = chave
        self.codigo_gerado = codigo_gerado
        self.after_xor = after_xor
        self.score = score

# Esta é a função que calcula o valor que a 'chave' possui de ser a 'verdadeira'. Quanto mais alto o valor, mais alta a probabilidade da 'chave' ser a correta.
# Criei um sistema de pontuação para calcular o valor que uma chave possui. Tal sistema se baseiam em como a mensagem pode 'parecer' uma mensagem usual, como a qual 
# envimos regularmente. Os critérios somam e subtraem pontos do score da chave.
# Os critérios de avaliação são os seguintes: 
# A existência de espaços ' ' na mensagem soma 3 pontos ao score da chave;
# 1 - Caso o próximo caractere após uma consoante for uma vogal, é somado 1 ponto ao score da chave;
# 2 - Caso o próximo caractere após uma vogal for uma consoante, é somado 1 ponto ao score da chave;
# 3 - Caso o próximo caractere após um número for um caractere especial, é subtraído 1 ponto do score da chave;
# 4 - Caso o próximo caractere após um caractere especial for um número, é subtraído 1 ponto do score da chave;
# 5 - Caso o próximo caractere após um caractere especial também for um caractere especial, é subtraído 1 ponto do score da chave;
def calcularScore(codigo_gerado):
    codigo_gerado = str(codigo_gerado)
    codigo_gerado = codigo_gerado.lower()
    codigo_gerado = list(codigo_gerado)
    codigo_gerado.remove('b')
    score = 0

    for i in range(len(codigo_gerado)):
        if codigo_gerado[i] == ' ':
            score += 3

        if i != len(codigo_gerado)-1:
            if codigo_gerado[i] in vogais:
                if codigo_gerado[i+1] in consoantes:
                    score += 1
            
            if codigo_gerado[i] in consoantes:
                if codigo_gerado[i+1] in vogais:
                    score += 1

            if codigo_gerado[i] in numeros:
                if codigo_gerado[i+1] in caracteresEspeciais:
                    score -= 1

            if codigo_gerado[i] in caracteresEspeciais:
                if codigo_gerado[i+1] in numeros:
                    score -= 1
            
            if codigo_gerado[i] in caracteresEspeciais:
                if codigo_gerado[i+1] in caracteresEspeciais:
                    score -= 1

    return score
        
vetorChaves = ['00000000','00000001','00000010','00000011','00000100','00000101','00000110','00000111','00001000','00001001','00001010','00001011','00001100','00001101','00001110','00001111','00010000','00010001','00010010','00010011','00010100','00010101','00010110','00010111','00011000','00011001','00011010','00011011','00011100','00011101','00011110','00011111','00100000','00100001','00100010','00100011','00100100','00100101','00100110','00100111','00101000','00101001','00101010','00101011','00101100','00101101','00101110','00101111','00110000','00110001','00110010','00110011','00110100','00110101','00110110','00110111','00111000','00111001','00111010','00111011','00111100','00111101','00111110','00111111','01000000','01000001','01000010','01000011','01000100','01000101','01000110','01000111','01001000','01001001','01001010','01001011','01001100','01001101','01001110','01001111','01010000','01010001','01010010','01010011','01010100','01010101','01010110','01010111','01011000','01011001','01011010','01011011','01011100','01011101','01011110','01011111','01100000','01100001','01100010','01100011','01100100','01100101','01100110','01100111','01101000','01101001','01101010','01101011','01101100','01101101','01101110','01101111','01110000','01110001','01110010','01110011','01110100','01110101','01110110','01110111','01111000','01111001','01111010','01111011','01111100','01111101','01111110','01111111','10000000','10000001','10000010','10000011','10000100','10000101','10000110','10000111','10001000','10001001','10001010','10001011','10001100','10001101','10001110','10001111','10010000','10010001','10010010','10010011','10010100','10010101','10010110','10010111','10011000','10011001','10011010','10011011','10011100','10011101','10011110','10011111','10100000','10100001','10100010','10100011','10100100','10100101','10100110','10100111','10101000','10101001','10101010','10101011','10101100','10101101','10101110','10101111','10110000','10110001','10110010','10110011','10110100','10110101','10110110','10110111','10111000','10111001','10111010','10111011','10111100','10111101','10111110','10111111','11000000','11000001','11000010','11000011','11000100','11000101','11000110','11000111','11001000','11001001','11001010','11001011','11001100','11001101','11001110','11001111','11010000','11010001','11010010','11010011','11010100','11010101','11010110','11010111','11011000','11011001','11011010','11011011','11011100','11011101','11011110','11011111','11100000','11100001','11100010','11100011','11100100','11100101','11100110','11100111','11101000','11101001','11101010','11101011','11101100','11101101','11101110','11101111','11110000','11110001','11110010','11110011','11110100','11110101','11110110','11110111','11111000','11111001','11111010','11111011','11111100','11111101','11111110','11111111']
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vogais = ['a', 'e', 'i', 'o', 'u']
caracteresEspeciais = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'] 
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
listaDeChaves = []

empateScore = []

# Main loop
while True:
    start = input('Digite a mensagem a ser descriptografada: ')
    aux = conversaoHexParaBinario(start)

    for i in range(128):
        codigoStr = ""
        aux = xorFunction(aux, vetorChaves[i])

        for j in range(len(aux)):
            codigoStr += str(aux[j])
            chaveAtual = Chaves('','','', '')
            chaveAtual.chave = vetorChaves[i]

        string = conversaoBinarioParaHex(aux)
        chaveAtual.after_xor = string
        string = bytes.fromhex(string)
        string.decode("ASCII")
        chaveAtual.codigo_gerado = string
        listaDeChaves.append(chaveAtual)
    
    for h in range(len(listaDeChaves)):
        chave = listaDeChaves[h]
        score = calcularScore(chave.codigo_gerado)
        chave.score = score
        print("-------------------------------------------------------------------------------")
        print("Chave utilizada: ", end='')
        print(chave.chave)
        print("After XOR: ", end='')
        print(chave.after_xor)
        print("Mensagem descriptografada: ", end='')
        removerMalditoB = ""
        removerB = chave.codigo_gerado
        removerB = str(removerB)
        removerB = list(removerB)
        removerB.remove('b')
        for i in range(len(removerB)):
            removerMalditoB += removerB[i]
        print(removerMalditoB)
        print("Score da chave: ", end='')
        print(chave.score)

    scoreAtual = 0

# Checando o maior score entre todas as chaves.
    for chave in listaDeChaves:

        if chave.score > scoreAtual:
            scoreAtual = chave.score 
            mensagemDescriptografada = chave.codigo_gerado
            chaveFinal = chave.chave

# Adicionado a mensagem da chave de maior score em uma string. Removi também a letra 'b', quem é adicionada após converter o texto para ASCII.
    mensagemFinal = ""
    mensagemDescriptografada = str(mensagemDescriptografada)
    mensagemDescriptografada = list(mensagemDescriptografada)
    mensagemDescriptografada.remove('b')

    for i in range(len(mensagemDescriptografada)):
        mensagemFinal += mensagemDescriptografada [i]

    print('====================================================================================')
    print("Está é a mensagem descriptografada: ", end='')
    print(mensagemFinal)
    print("A chave que gerou esta mensagem é: ", end='')
    print(chaveFinal)
    print("E seu score é: ", end = '')
    print(scoreAtual)
    print('====================================================================================')