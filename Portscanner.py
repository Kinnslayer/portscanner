#Fazendo a importação do Nmap para o Pycharm.
import nmap

#Criando uma variável para alocar todos os arquivos do nmap.
scanner = nmap.PortScanner()

#Introdução do programa e interação com o usuário.
start = print("Seja bem vindo ao Portscanner!")
print("<----------------------------->")

#Pedido ao usuário para digitar o IP que gostaria de fazer a varredura.
ip = input("Digite o ip a ser varrido: ")
print("O ip digitado foi:", ip)
type(ip)

#Menu para a escolha do tipo de varredura de acordo com usuário.
menu = input("""\n Escolha o tipo de varredura a ser realizada
                1 -> Varredura do tipo SYN
                2 -> Varredura do tipo UDP
                3 -> Varredura do tipo Intensa
                Digite a opção escolhida: """)

print("A opção escolhida foi", menu)

#Se o usuário escolher a varredura do tipo 1, essas serão as condições:
if menu == "1":
    print("Versão do Nmap: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024',  '-v -sS')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Portas Abertas: ", scanner[ip]['tcp'].keys())

#Se o usuário escolher a varredura do tipo 2, essas serão as condições:
elif menu == "2":
    print("Versão do Nmap: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Portas Abertas: ", scanner[ip]['udp'].keys())

#Se o usuário escolher a varredura do tipo 3, essas serão as condições:
elif menu == "3":
    print("Versão do Nmap: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sC')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Portas Abertas: ", scanner[ip]['tcp'].keys())

#Caso o usuário digite uma opção inválida, será informado a ele sobre o erro.


















