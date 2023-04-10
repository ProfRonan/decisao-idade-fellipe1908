print("Digite sua Idade: ")
idade = int((input(">")))
impossível = False
menor = False
maior = False
velho = False

if idade < 0:
    print("impossível!")
    impossivel = True
if idade < 18:
    print("não precisa se alistar.")
    menor = True 
if 18 < idade < 65:
    print("Não esqueça de votar na proxima eleição.")
    maior = True
if idade > 65:
    print("Vá descansar.")
    velho = True
if not(impossível or menor or maior or velho):
    print("eita!") 


