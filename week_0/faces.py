def main():
    text = input()
    print(f"{faces(text)}")

def faces(t):
    # retira os espaços antes de depois da string e substitui os espaços internos por emojis
    return t.replace(":)", "🙂").replace(":(", "🙁")
main()