def main():
    text = input("Digite o texto: ")
    print(f"{replace(text)}")

def replace(t):
    return t.strip().replace(" ", "...")

main()
