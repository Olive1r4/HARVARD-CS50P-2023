#Programa recebe uma string e substitui os espaços por três pontos
def main():
    text = input("Digite o texto: ")
    print(f"{replace(text)}")

def replace(t):
    # retira os espaços antes de depois da string e substitui os espaços internos por três pontos
    return t.strip().replace(" ", "...")

main()
