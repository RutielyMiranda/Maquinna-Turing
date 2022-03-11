from Maquina_Turing import Maquina_Turing


estado_inicial = "init",
estado_aceito = ["final"],
funcao_transicao = {("init", "0"): ("init", "1", "R"),
                    ("init", "1"): ("init", "0", "R"),
                    ("init", " "): ("final", " ", "N"),
                    }
estado_final = {"final"}

t = Maquina_Turing("101100110 ",
                   estado_inicial="init",
                   estado_final=estado_final,
                   funcao_transicao=funcao_transicao)

print("Dentro da Fita:\n" + t.get_fita())

while not t.final():
    t.step()

print("Resultado do cálculo da Máquina de Turing:")
print(t.get_fita())
