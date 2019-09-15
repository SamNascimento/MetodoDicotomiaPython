'''
Esse Programa consegue pegar polinômios de até 5° Grau e realizar operações com o Teorema de Bozano e o Método de Dicotomia
Ele usa o Teorema e o Método para verificar se dentro do intervalo imposto pelo usuário existe alguma raiz
Também é utilizado a varíavel "erro" que define o limite de vezes que as operações vão se repetir baseado no número posto nela
Esse programa suporta erros de até 2 dígitos depois da vírgula

'''
# Iniciando a variável de grau do polinômio
grau = 0

# Iniciando a váriavel que pega os números utilizados no cálculo dos polinômios
num = []

# Define o grau da equação, não permitindo valores maiores que 5 e nem menores que 1
while (grau > 5 or grau < 1): 
    grau = int (input ("Defina o número de grau do polinômio (Deve ser de 1 à 5): "))
    if (grau > 5 or grau < 1): 
        print("grau inválido")

# Coletando valores para o Intervalo Inicial e o Erro da equação
intervaloInicial = float (input ("Defina o primeiro valor do intervalo inicial: "))
intervaloFinal = float (input ("Defina o segundo valor do intervalo inicial: "))
erro = float (input ("Defina o erro (limite) do cálculo: "))

# Pega os valores para utilizar na equação, os valores são armazenados no vetor num[] e a quantidade de números armazenados é correspondente ao grau do polinômio
print ("Agora só resta definir os valores para efetuar os cálculos pelo Teorema de Bozano e o Método da Dicotomia")
for i in range (grau+1):
    print("Defina o valor do", i+1, end="° ")
    valor = float (input ("número: "))
    num.append (valor)

# Exibe o cálculo que será feito, ilustrando os números que serão utilizados
if (grau == 1):
    print("A equação geral ficou F(x) =", num[0],"x +", num[1])
elif (grau == 2):
    print("A equação geral ficou F(x) =", num[0],"x^2 +", num[1],"x +", num[2])
elif (grau == 3):
    print("A equação geral ficou F(x) =", num[0],"x^3 +", num[1],"x^2 +", num[2],"x +", num[3])
elif (grau == 4):
    print("A equação geral ficou F(x) =", num[0],"x^4 +", num[1],"x^3 +", num[2],"x^2 +", num[3],"x +", num[4])
elif (grau == 5):
    print("A equação geral ficou F(x) =", num[0],"x^5 +", num[1],"x^4 +", num[2],"x^3 +", num[3],"x^2 +", num[4],"x +", num[5])

# Armazena o valor dos 2 números dados no Intervalo Inicial
i = intervaloInicial
j = intervaloFinal

# Variável que checa se a raiz exata foi encontrada
achouRaiz = False

# Variável que pega o valor da função que possui a raiz exata
raiz = 0.0

# Variável que verifica se foi encontrada raiz em algum intervalo ou não
semRaiz = True

# Variável que verifica se o cálculo chegou a ser iniciado
rodouCalc = False

# Iniciando as variaveis que irão checar qual dos intervalos será dividido por dois ao realizar o Método de Dicotomia. Por padrão ele irá utilizar o segundo valor do intervalo final
usarIntervaloInicial = False
usarIntervaloFinal = True

# Calculando a diferença dos intervalos dados
diferenca = i - j
if (diferenca < 0):
    diferenca = diferenca*-1.0

# Um loop que irá rodar até que a diferença entre os intervalos seja menor ou igual ao erro estipulado pelo usuário
while (diferenca >= erro):
    # Pegando so valores que definem de que intervalo até que intervalo o cálculo irá rodar
    i = intervaloInicial
    j = intervaloFinal

    # Caso a raiz tenha sido encontrada em algum ponto do loop essa condição é ativada encerrando o processo e mostrando em que Função a raiz foi encontrada
    if (achouRaiz == True):
        print ("Raiz encontrada na posição: F(", raiz ,")")
        break

    # Essa condição será ativada no caso do intervalo inicial ser maior que o intervalo final, evitando que o programa entre em loop infinito
    if (i >= j):
        print("O primeiro valor do intervalo inicial não pode ser maior ou igual ao segundo")
        # Informa que o programa pelo menos iniciou o cálculo e finaliza o Loop
        rodouCalc = True
        break

    # Esse bloco de códigos irá rodar enquanto a condição de "i" (que pegou o valor do Intervalo Inicial do cálculo) for menor ou igual há "j" (que pegou o valor do Intervalo Final do cálculo)
    while (i <= j):
        # "x" pega o valor que está armazenado em "i" no começo de cada loop
        x = i

        # Condição que executa o cálculo baseado em qual grau foi escolhido pelo usuário, evitando que o programa tente puxar valores do vetor que não foram setados
        if (grau == 1):
            # Executa o cálculo
            calc = (num[0]*x) + num[1]
            # Verifica se o cálculo atual possui a raiz
            if (calc == 0.00):
                raiz = x
                achouRaiz = True 
            # Validação que evita que o programa tente utilizar valores menores do que os definidos no Intervalo Inicial
            if(x > intervaloInicial):
                # Define o número de casas que será calculado dependendo do tamanho da diferença entre os números
                if (diferenca > 1.0):
                    # Cálcula o número anterior baseado no tamanho da diferença, quanto menor a diferença mais preciso o cálculo se torna (ou seja, com mais casas decimais depois da virgula ele calcula)
                    anterior = (num[0]*(x-1)) + num[1]
                    if (anterior < 0 and calc >= 0):
                        intervaloInicial = x-1
                        intervaloFinal = x
                        # Informa que existe alguma raiz no Intervalo dado
                        semRaiz = False
                        # Verifica se o intervalo anterior usado é o intervalo que possui a raiz
                        if (anterior == 0.0):
                            raiz = x - 1
                            achouRaiz = True
                elif (diferenca <= 1.0 and diferenca > 0.1):
                    anterior = (num[0]*(x-0.1)) + num[1]
                    if (anterior < 0.0 and calc >= 0.0):
                        intervaloInicial = x-0.1
                        intervaloFinal = x
                        semRaiz = False
                        if (anterior == 0.0):
                            raiz = x - 0.1
                            achouRaiz = True
                else:
                    anterior = (num[0]*(x-0.01)) + num[1]
                    if (anterior < 0.00 and calc >= 0.00):
                        intervaloInicial = x-0.01
                        intervaloFinal = x
                        semRaiz = False
                        if (anterior == 0.00):
                            raiz = x - 0.01
                            achouRaiz = True
        elif (grau == 2):
            calc = (num[0]*x)*2 + (num[1]*x) + num[2]
            if (calc == 0.00):
                raiz = x
                achouRaiz = True 
            if(x > intervaloInicial):
                if (diferenca > 1.0):
                    anterior = (num[0]*(x-1))*2 + (num[1]*(x-1)) + num[2]
                    if (anterior < 0 and calc >= 0):
                        intervaloInicial = x-1
                        intervaloFinal = x
                        semRaiz = False
                        if (anterior == 0.0):
                            raiz = x - 1
                            achouRaiz = True
                elif (diferenca <= 1.0 and diferenca > 0.1):
                    anterior = (num[0]*(x-0.1))*2 + (num[1]*(x-0.1)) + num[2]
                    if (anterior < 0.0 and calc >= 0.0):
                        intervaloInicial = x-0.1
                        intervaloFinal = x
                        semRaiz = False
                        if (anterior == 0.0):
                            raiz = x - 0.1
                            achouRaiz = True
                else:
                    anterior = (num[0]*(x-0.01))*2 + (num[1]*(x-0.01)) + num[2]
                    if (anterior < 0.00 and calc >= 0.00):
                        intervaloInicial = x-0.01
                        intervaloFinal = x
                        semRaiz = False
                        if (anterior == 0.00):
                            raiz = x - 0.01
                            achouRaiz = True
        elif (grau == 3):
            calc = (num[0]*x)*3 + (num[1]*x)*2 + (num[2]*x) + num[3]
            if (calc == 0.00):
                raiz = x
                achouRaiz = True 
            if(x > intervaloInicial):
                if (diferenca > 1.0):
                    anterior = (num[0]*(x-1))*3 + (num[1]*(x-1))*2 + (num[2]*(x-1)) + num[3]
                    if (anterior < 0 and calc >= 0):
                        intervaloInicial = x-1
                        intervaloFinal = x
                        semRaiz = False
                        if (anterior == 0.0):
                            raiz = x - 1
                            achouRaiz = True
                elif (diferenca <= 1.0 and diferenca > 0.1):
                    anterior = (num[0]*(x-0.1))*3 + (num[1]*(x-0.1))*2 + (num[2]*(x-0.1)) + num[3]
                    if (anterior < 0.0 and calc >= 0.0):
                        intervaloInicial = x-0.1
                        intervaloFinal = x
                        semRaiz = False
                        if (anterior == 0.0):
                            raiz = x - 0.1
                            achouRaiz = True
                else:
                    anterior = (num[0]*(x-0.01))*3 + (num[1]*(x-0.01))*2 + (num[2]*(x-0.01)) + num[3]
                    if (anterior < 0.00 and calc >= 0.00):
                        intervaloInicial = x-0.01
                        intervaloFinal = x
                        semRaiz = False
                        if (anterior == 0.00):
                            raiz = x - 0.01
                            achouRaiz = True
        elif (grau == 4):
            calc = (num[0]*x)*4 + (num[1]*x)*3 + (num[2]*x)*2 + (num[3]*x) + num[4]
            if (calc == 0.00):
                raiz = x
                achouRaiz = True 
            if(x > intervaloInicial):
                if (diferenca > 1.0):
                    anterior = (num[0]*(x-1))*4 + (num[1]*(x-1))*3 + (num[2]*(x-1))*2 + (num[3]*(x-1)) + num[4]
                    if (anterior < 0 and calc >= 0):
                        intervaloInicial = x-1
                        intervaloFinal = x
                        semRaiz = False
                        if (anterior == 0.0):
                            raiz = x - 1
                            achouRaiz = True
                elif (diferenca <= 1.0 and diferenca > 0.1):
                    anterior = (num[0]*(x-0.1))*4 + (num[1]*(x-0.1))*3 + (num[2]*(x-0.1))*2 + (num[3]*(x-0.1)) + num[4]
                    if (anterior < 0.0 and calc >= 0.0):
                        intervaloInicial = x-0.1
                        intervaloFinal = x
                        semRaiz = False
                        if (anterior == 0.0):
                            raiz = x - 0.1
                            achouRaiz = True
                else:
                    anterior = (num[0]*(x-0.01))*4 + (num[1]*(x-0.01))*3 + (num[2]*(x-0.01))*2 + (num[3]*(x-0.01)) + num[4]
                    if (anterior < 0.00 and calc >= 0.00):
                        intervaloInicial = x-0.01
                        intervaloFinal = x
                        semRaiz = False
                        if (anterior == 0.00):
                            raiz = x - 0.01
                            achouRaiz = True
        elif (grau == 5):
            calc = (num[0]*x)*5 + (num[1]*x)*4 + (num[2]*x)*3 + (num[3]*x)*2 + (num[4]*x) + num[5]
            if (calc == 0.00):
                raiz = x
                achouRaiz = True 
            if(x > intervaloInicial):
                if (diferenca > 1.0):
                    anterior = (num[0]*(x-1))*5 + (num[1]*(x-1))*4 + (num[2]*(x-1))*3 + (num[3]*(x-1))*2 + (num[4]*(x-1)) + num[5]
                    if (anterior < 0 and calc >= 0):
                        intervaloInicial = x-1
                        intervaloFinal = x
                        semRaiz = False
                        if (anterior == 0.0):
                            raiz = x - 1
                            achouRaiz = True
                elif (diferenca <= 1.0 and diferenca > 0.1):
                    anterior = (num[0]*(x-0.1))*5 + (num[1]*(x-0.1))*4 + (num[2]*(x-0.1))*3 + (num[3]*(x-0.1))*2 + (num[4]*(x-0.1)) + num[5]
                    if (anterior < 0.0 and calc >= 0.0):
                        intervaloInicial = x-0.1
                        intervaloFinal = x
                        semRaiz = False
                        if (anterior == 0.0):
                            raiz = x - 0.1
                            achouRaiz = True
                else:
                    anterior = (num[0]*(x-0.01))*5 + (num[1]*(x-0.01))*4 + (num[2]*(x-0.01))*3 + (num[3]*(x-0.01))*2 + (num[4]*(x-0.01)) + num[5]
                    if (anterior < 0.00 and calc >= 0.00):
                        intervaloInicial = x-0.01
                        intervaloFinal = x
                        semRaiz = False
                        if (anterior == 0.00):
                            raiz = x - 0.01
                            achouRaiz = True
        # Exibe qual função foi cálculada nesse loop e qual o valor da mesma
        print("F(%f) = %f" %(x, calc))

        # Define a precisão do loop baseado no atual número da diferença entre os valores do Intervalo
        if (diferenca > 1.0):
            i += 1
        elif (diferenca <= 1.0 and diferenca > 0.1):
            i += 0.1
        else:
            i += 0.01
    # Caso o loop rode e não encontre nenhuma raiz isso signifca que não existe raiz no Intervalo setado pelo usuário, desta forma o loop é finalizado
    if (semRaiz):
        print("O intervalo não possui raiz")
        rodouCalc = True
        break

    # Caso tenha uma raiz em algum dos intervalos o programa executa esse bloco de códigos
    elif(semRaiz == False):
        # É aqui que ele exibe entre quais intervalos a raíz se encontra
        print ("A raíz está entre os intervalos ", intervaloInicial ," e ", intervaloFinal)

        # Verifica se o primeiro número do intervalo é negativo, se for ele inicia o bloco para calcular se o número divido por dois será o primeiro ou o segundo valor do Intervalo Inicial
        if (intervaloInicial < 0.0):
            # Armazena o primeiro valor do Intervalo Inicial para simular se ele é a melhor escolha para diminuir
            temp = intervaloInicial/2.0

            # Faz a simulação baseado no grau utilizado no polinômio
            if (grau == 1):
                calc = (num[0]*temp) + num[1]
                if (calc <= 0.0):
                    # Caso na simulação a função do primeiro valor do intervalo não ultrapasse a raiz (que é o 0) então o programa define que o primeiro valor é o melhor para diminuir e realizar a equação nova da função
                    usarIntervaloInicial = True
                    usarIntervaloFinal = False
            elif (grau == 2):
                calc = (num[0]*temp)*2 + (num[1]*temp) + num[2]
                if (calc <= 0.0):
                    usarIntervaloInicial = True
                    usarIntervaloFinal = False
            elif (grau == 3):
                calc = (num[0]*temp)*3 + (num[1]*temp)*2 + (num[2]*temp) + num[3]
                if (calc <= 0.0):
                    usarIntervaloInicial = True
                    usarIntervaloFinal = False
            elif (grau == 4):
                calc = (num[0]*temp)*4 + (num[1]*temp)*3 + (num[2]*temp)*2 + (num[3]*temp) + num[4]
                if (calc <= 0.0):
                    usarIntervaloInicial = True
                    usarIntervaloFinal = False
            elif (grau == 5):
                calc = (num[0]*temp)*5 + (num[1]*temp)*4 + (num[2]*temp)*3 + (num[3]*temp)*2 + (num[4]*temp) + num[5]
                if (calc <= 0.0):
                    usarIntervaloInicial = True
                    usarIntervaloFinal = False
        # Caso as simulações com o primeiro valor do intervalo tenham ultrapassado o valor de 0 então define que é melhor diminuir o segundo valor do Intervalo Inicial
        else:
            usarIntervaloFinal = True
    # Roda esse loop caso o programa não tenha achado a função exata da raiz anteriormente
    if (achouRaiz == False):
        print("Calculando diferença...")
        # Realiza o novo calcúlo da diferença para saber com qual precisão o cálculo deve ser tratado ao rodar o loop, se deve ser tratado com a precisão de números inteiros ou números com até 2 casas depois da vírgula de precisão
        diferenca = i - j
        if (diferenca < 0.0):
            diferenca = diferenca*-1.0 
        # Exibe a atual diferença
        print("A diferença é de: ", diferenca)

        # Caso a diferença atual não tenha ultrapassado o limite do erro ele informa qual será o próximo intervalo utilizado no cálculo
        if (diferenca > erro):
            print("Repetindo o processo utilizando os valores: ", end="[")
            # É aqui que é a simulação afeta o código, dependendo da simulação ele diminuirá o primeiro valor ou o segundo valor do Intervalo Inicial
            if (usarIntervaloInicial == True):
                intervaloInicial = intervaloInicial/2.0
                print ("%f, %f]" %(intervaloInicial, intervaloFinal))
            elif (usarIntervaloFinal == True):
                intervaloFinal = intervaloFinal/2.0
                print ("%f, %f]" %(intervaloInicial, intervaloFinal))
        # Caso a diferença dos valores tenha atingido um valor menor ou igual ao erro estipulado o código informa que finalizou o processo por tal razão
        elif (diferenca <= erro):
            print("Processo atingiu o limite (erro) delimitado, finalizando processo")
    # Caso o programa não tenha sido interrompido em nenhum dos pontos ele define ao final do primeiro loop que o cálculo rodou
    rodouCalc = True
# Se o cálculo nem chegou a ser rodado é por conta do erro definido ser maior que os intervalos estipulados, dessa forma o programa formaliza isso através desse bloco
if (rodouCalc == False):
    print("Erro maior que a diferença do intervalo Inicial")