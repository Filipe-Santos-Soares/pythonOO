class Criptografador:
    def __init__(self, texto):
        self.texto = texto

    def criptografar(self):
        #A – 4, E – 3, I – 1, O – 0, U – 8
        substituicoes = {
            "A": "4", "a": "4",
            "e": "3", "E": "3",
            "i": "1", "I": "1",
            "o": "0", "O": "0",
            "u": "8", "U": "8"
        }
        frase_criptografada = ""
        for caracter in self.texto:
            if caracter in substituicoes:
                frase_criptografada += substituicoes[caracter]
            else:
                frase_criptografada += caracter
            
        return frase_criptografada
    

def main():
    texto = input("\nDigite um texto para criptografar: ")
    criptografia = Criptografador(texto)
    resultado = criptografia.criptografar()
    print(f"\nTexto criptografado: '{resultado}'")  


if __name__ =="__main__":
    main()