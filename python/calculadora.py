print("===  Python Calculator  ===");
running = True

def resolveMode(modeId):
    match modeId:
        case 0:
            print("Saindo... ")
            running = False
            return
        case 1:
            print("Soma: ")
            return soma
        case 2:
            print("Subtração: ")
            return sub
        case 3:
            print("Multiplicação: ")
            return multi
        case 4:
            print("Divisão: ")
            return div
        case 5:
            print("Exponenciação: ")
            return exp
        case 6:
            print("Raiz: ")
            return rt
        case default:
            print("Comando invalido")
            return invalid  

def printRes(operação, res, A, B):
    print("O resultado da {} entre {} e {} é igual a {}\n".format(operação, A, B, res))
    return

def getInput():
    A = float(input("A = "))
    B = float(input("B = "))
    return(A, B)

def invalid(A, B):
    return

def soma(A, B):
    return(A + B)

def sub(A, B):
    return(A - B)

def multi(A, B):
    return(A * B)

def div(A, B):
    return(A / B)

def exp(A, B):
    return(A ** B)

def rt(A, B):
    return(A ** (1/B))

while running:
    print("Escolha um modo: (0 - 6)\n 1 - Soma (A + B) \n 2 - Subtração (A - B) \n 3 - Multiplicação (A x B)\n 4 - Divisão (A / B) \n 5 - Exponenciação (A ^ B) \n 6 - Raiz (A ^(1/B)) \n 0 - Sair");
    modo = int(input(" > "))
    resolveMode(modo)(A, B = map(getInput()))
