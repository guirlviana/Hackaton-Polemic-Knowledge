
class JogoDavelha:
    def __init__(self):
        self.linhaA = ['1','2','3']
        self.linhaB = ['4','5','6']
        self.linhaC = ['7','8','9']
        
        print(f"{self.linhaA}\n{self.linhaB}\n{self.linhaC}")

    def decisao(self):
        self.cont = 0
        while True:
            self.escolhaX()
            self.cont += 1
            if self.cont >= 9:
                print("Deu velha")
                break
            if self.linhaA ==  ['X', 'X', 'X']:
                print("X venceu")
                break
            if self.linhaB ==  ['X', 'X', 'X']:
                print("X venceu")
                break
            if self.linhaC ==  ['X', 'X', 'X']:
                print("X venceu")
                break
            if self.linhaA[0] == "X" and self.linhaB[0] == "X" and self.linhaC[0] == "X":
                print("X venceu")
                break
            if self.linhaA[1] == "X" and self.linhaB[1] == "X" and self.linhaC[1] == "X":
                print("X venceu")
                break
            if self.linhaA[2] == "X" and self.linhaB[2] == "X" and self.linhaC[2] == "X":
                print("X venceu")
                break
            if self.linhaA[0] == "X" and self.linhaB[1]  == "X" and self.linhaC[2]  == "X":
                print("X venceu")
                break
            if self.linhaA[2] == "X" and self.linhaB[1]  == "X" and self.linhaC[0]  == "X":
                print("X venceu")
                break

            self.escolhaO()
            self.cont += 1
            if self.linhaA ==  ['O', 'O', 'O']:
                print("O venceu")
                break
            if self.linhaB ==  ['O', 'O', 'O']:
                print("O venceu")
                break
            if self.linhaC ==  ['O', 'O', 'O']:
                print("O venceu")
                break
            if self.linhaA[0] == "O" and self.linhaB[0] == "O" and self.linhaC[0] == "O":
                print("O venceu")
                break
            if self.linhaA[1] == "O" and self.linhaB[1] == "O" and self.linhaC[1] == "O":
                print("O venceu")
                break
            if self.linhaA[2] == "O" and self.linhaB[2] == "O" and self.linhaC[2] == "O":
                print("O venceu")
                break
            if self.linhaA[0] == "O" and self.linhaB[1]  == "O" and self.linhaC[2]  == "O":
                print("O venceu")
                break
            if self.linhaA[2] == "O" and self.linhaB[1]  == "O" and self.linhaC[0]  == "O":
                print("O venceu")
                break
        print("FIM")


    def escolhaX(self):
        self.decisaoPos = str(input("a posição jogar X? [1 até 9]")).strip().upper()
        
        if self.decisaoPos == '1':
            self.linhaA[0] = "X"
        if self.decisaoPos == '2':
            self.linhaA[1] = "X"
        if self.decisaoPos == '3':
            self.linhaA[2] = "X"

        if self.decisaoPos == '4':
            self.linhaB[0] = "X"
        if self.decisaoPos == '5':
            self.linhaB[1] = "X"
        if self.decisaoPos == '6':
            self.linhaB[2] = "X"

        if self.decisaoPos == '7':
            self.linhaC[0] = "X"
        if self.decisaoPos == '8':
            self.linhaC[1] = "X"
        if self.decisaoPos == '9':
            self.linhaC[2] = "X"

        print(f"{self.linhaA}\n{self.linhaB}\n{self.linhaC}")

    def escolhaO(self):    

        self.decisaoPos = str(input("a posição jogar O? [1 até 9]")).strip().upper()
        
        if self.decisaoPos == '1':
            self.linhaA[0] = "O"
        if self.decisaoPos == '2':
            self.linhaA[1] = "O"
        if self.decisaoPos == '3':
            self.linhaA[2] = "O"

        if self.decisaoPos == '4':
            self.linhaB[0] = "O"
        if self.decisaoPos == '5':
            self.linhaB[1] = "O"
        if self.decisaoPos == '6':
            self.linhaB[2] = "O"

        if self.decisaoPos == '7':
            self.linhaC[0] = "O"
        if self.decisaoPos == '8':
            self.linhaC[1] = "O"
        if self.decisaoPos == '9':
            self.linhaC[2] = "O"              
        print(f"{self.linhaA}\n{self.linhaB}\n{self.linhaC}")
        
        




                 
          



rodar = JogoDavelha()
rodar.decisao()
