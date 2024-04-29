import random

combate = 1
conhecimento = 1
habilidade = 1
sorte = 1

combateclasse = 0
conhecimentoclasse = 0
habilidadeclasse = 0
sorteclasse = 0

gatuno = 5
cacador = 6
mercenario = 7
lider = 8
xama = 9
piromaniaco = 10

verde = 11
verdeclaro = 12
verdeescuro = 13
amarelo = 14
azul = 15
vermelho = 16
 
cor = random.randint(11, 16)
classe = random.randint(5,10)

if cor == 11:
    combate = 2
    conhecimento = 1
    habilidade = 1
    sorte = 2

if cor == 12:
    combate = 2
    conhecimento = 2
    habilidade = 1
    sorte = 1
    
if cor == 13:
    combate = 2
    conhecimento = 1
    habilidade = 2
    sorte = 1
    
if cor == 14:
    combate = 1
    conhecimento = 1
    habilidade = 2
    sorte = 2
    
if cor == 15:
    combate = 1
    conhecimento = 2
    habilidade = 1
    sorte = 2
    
if cor == 16:
    combate = 1
    conhecimento = 2
    habilidade = 2
    sorte = 1

if classe == 5:
    habilidadeclasse = 1
    conhecimentoclasse = 1
    
if classe == 6:
    combateclasse = 1
    sorteclasse = 1
    
if classe == 7:
    combateclasse = 1
    habilidadeclasse = 1
    
if classe == 8:
    combateclasse = 1
    conhecimentoclasse = 1
    
if classe == 9:
    conhecimentoclasse = 1
    sorte = 1
    
if classe == 10:
    habilidadeclasse = 1
    sorteclasse = 1
    
statscombate = combate + combateclasse
statsconhecimento = conhecimento + conhecimentoclasse
statshabilidade = habilidade + habilidadeclasse
statssorte = sorte + sorteclasse


insano = 17
fedorento = 18
gordo = 19
fala_errado = 20
cicatrizes = 21
anomalia = 22

manchas_rosas = 23
orelhas_no_sovaco = 24
corcunda = 25 
braco_extra_atrofiado = 26
olhos_extra = 27
olhos_gigantes = 28
maos_gigantes = 29
duas_cabecas = 30

caracteristica = random.randint(17, 22)

anomaliarandom = random.randint(23, 30)

if anomaliarandom == 23:
    anomaliarandom = "manchas rosas"
    
if anomaliarandom == 24:
    anomaliarandom = "orelhas no sovaco"
    
if anomaliarandom == 25:
    anomaliarandom = "corcunda"
    
if anomaliarandom == 26:
    anomaliarandom = "braço extra atrofiado"

if anomaliarandom == 27:
    anomaliarandom = "olhos(rode um d6)"
    
if anomaliarandom == 28:
    anomaliarandom = "olhos gigantes"

if anomaliarandom == 29:
    anomaliarandom = "mãos gigantes"

if anomaliarandom == 30:
    anomaliarandom = "duas cabeças"

print("Seus status são:", statscombate, statsconhecimento, statshabilidade, statssorte)

if caracteristica == 17:
    print("Sua característica é:","insano")
    
if caracteristica == 18:
    print("Sua característica é:","fedorento")
    
if caracteristica == 19:
    print("Sua característica é:","gordo")
    
if caracteristica == 20:
    print("Sua característica é:","fala errado")
    
if caracteristica == 21:
    print("Sua característica é:","cicatrizes")
    
if caracteristica == 22:
    print("Sua característica é:",anomaliarandom)
    
equipamento_leve = random.randint(1, 6)

equipamento_pesado = random.randint(1,6)

equipamento_explosivo = random.randint(1,6)

if equipamento_leve == 1:
    equipamento_leve = "2 adagas* (dano 2)"
    
if equipamento_leve == 2:
    equipamento_leve = "adaga* (dano 2) e escudo* (proteção)"
    
if equipamento_leve == 3:
    equipamento_leve = "arco simples* (distância; dano 2)"
    
if equipamento_leve == 4:
    equipamento_leve = "arco composto* (distância; dano 2)"
    
if equipamento_leve == 5:
    equipamento_leve = "4 adagas* (dano 2)"
    
if equipamento_leve == 6:
    equipamento_leve = "besta (distância; dano 3) e elmo (proteção 1)"
    
if equipamento_pesado == 1:
    equipamento_pesado = "espada (dano 3) e escudo (proteção 1 )"
    
if equipamento_pesado == 2:
    equipamento_pesado = "machado (dano 4) e elmo (proteção 1)"
    
if equipamento_pesado == 3:
    equipamento_pesado = "2 machadinhas* (dano 3)"
    
if equipamento_pesado == 4:
    equipamento_pesado = "espadona (dano 5)"
    
if equipamento_pesado == 5:
    equipamento_pesado = "2 espadas* (dano 3) e armadura (proteção 1)"
    
if equipamento_pesado == 6:
    equipamento_pesado = "adaga*, espada e armadura (proteção 1)"
    
if equipamento_explosivo == 1:
    equipamento_explosivo = "Pistola (distância; dano 4) e Elmo (proteção 1)"
    
if equipamento_explosivo == 2:
    equipamento_explosivo = "2 Pistolas (distância; dano 4)"
    
if equipamento_explosivo == 3:
    equipamento_explosivo = "3 Galinhas Explosivas (distância; dano 4 em todos até 3m)"
    
if equipamento_explosivo == 4:
    equipamento_explosivo = "Barril de Pólvora (dano 5 em todos até 3m)"
    
if equipamento_explosivo == 5:
    equipamento_explosivo = "Pistola e 2 Galinhas Explosivas"
    
if equipamento_explosivo == 6:
    equipamento_explosivo = "Canhão (distância; dano 8; Carregar [2 turnos])"
    
if classe == 5:
    print("Seu equipamento é:",equipamento_leve)
    
if classe == 6:
    print("Seu equipamento é:",equipamento_leve)
    
if classe == 7:
    print("Seu equipamento é:", equipamento_pesado)
    
if classe == 8:
    print("Seu equipamento é:", equipamento_pesado)

if classe == 9:
    print("Seu equipamento é:","Cajado (Dano 1), mas começa com 8 pontos de magia.") 
    
if classe == 10:
    print("Seu equipamento é:",equipamento_explosivo)