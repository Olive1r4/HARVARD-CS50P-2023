def main():
    x = int(input("x = "))
    print(f"o quadrado de {x} é {quadrado(x)}")

def quadrado(n):
    return pow(n, 2)

main()
