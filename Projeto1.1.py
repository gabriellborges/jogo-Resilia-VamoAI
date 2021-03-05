print("*"*100)
print('             O Mundo do Yupiiiii')
print("*"*100)

print('Personagens jogáveis: Mario // Luigi // Toad\n\n')
print("*"*100)
print('Esses três personagens precisam de ajuda para sairem\n'
      'vivos de um nefasto inimigo, que quer o fim de todos\n'
      'e esses personagens precisam de um mentor, você pode\n'
      'ser esse mentor, você deve fazer uma escolha de qual\n'
      'personagem você quer jogar!!')
print("*"*100 + '\n')
print('                 Personagens                    \n')
personagens = ['mario', 'luigi', 'toad']
mapas =['MontanhasEncanadas', 'SubmundoVerde', 'IlhaDoCogumelo']

print('Mario: É um encanador do mundo dos videogames, e irá\n'
      'usar a sua vasta experiência em games para vencermos.\n')
print('Luigi: É o irmão do mario e compartilha das mesmas experiências,'
      'os dois estão sempre juntos.\n')
print('Toad: É um grande amigos dos dois acima, e conhece os intentos\n'
      'do inimigo em comum dos três, ajudando com a sua nuvem voadora\n'
      'e sua pouca força para chegar no objetivo.\n')
print("*"*100 + '\n')
print('Teremos três mundos: \n'
      'Montanhas Encanadas  //  Submundo Verde // Ilha do Cogumelo\n')
print("*"*100)

i = 0
validador = 0
escolha = str
personagemEscolhido = str(input('Digite o nome do personagem escolhido\n')).lower().strip()
for i in range(0, 3):
    if personagemEscolhido == personagens[i]:
        escolha = str(personagens[i])
    else:
        escolha = personagemEscolhido
        pass

if personagemEscolhido == personagens[0] or personagemEscolhido == personagens[1] or personagemEscolhido == personagens[2]:
    print('Que legal, você escolheu {}'.format(escolha))
else:
    print('Voce escolheu ({})'.format(escolha) + ' porém esse nome não está na lista de personagens.')


def verificacao(caminho):
    if caminho == 1:
        print('Você não está infectado')
        return False
    else:
        print('Você está infectado.')
        return True


print('A nossa missão é combater o coronavírus, precisamos passar por três locais diferentes, subir na \n'
      'torre para pegar a máscara, escolher corretamente os canos para atravessarmos o canal da fake news\n'
      'para pegar o alcool em gel, e com a máscara e o alcool em gel poder chegar até o local da vacinação\n')

print('Precisamos chegar até a torre para pegar a máscara.\n'
      'Temos dois caminhos para chegar na Torre.\n'
      'Caminho 1: por cima da montanhas ou Caminho 2: por baixo.')
caminho = int(input('Qual caminho vai escolher 1 ou 2?\n'))
if caminho == 1:
    print('Vamos por cima: Gastamos um pouco mais de tempo para subir, mas está vazio aqui e\n'
          'vamos chegar com tranquilidade. \n')
    print('Muito bem chegamos até o primeiro local da nossa jornada, foi simples e conseguimos\n '
          'pegar a nossa primeira proteção, a máscara.\n')
elif caminho == 2:
    print('Caminho 2: Vamos por baixo, porém passaremos por várias pessoas, podemos nos infectar.\n\n')
    print('Muito bem chegamos até o primeiro local da nossa jornada, porém passamos por muitas\n '
          'pessoas no caminho, isso que me preocupa, mas agora estamos de máscara.\n')
travatela = input('')
print('Vamos continuar a nossa jornada,estamos mais próximos da torre do caminho escolhido,\n'
      ' agora nos resta desvendar uma charada, afinal só precisamos atravessar ela para chegar na torre \n'
      'e passarmos de fase.\n')
travatela1 = input('')
print('Há 3 canos para entrar, porém cada um com sua peculiaridade.\n')
print('Cano 1: Barulhento, não da para reconhecer oque é.')
print('Cano 2 : Brilhante de mais, chega a arder os olhos:')
print('Cano 3 : Escuro e sombrio, da calafrios:')
travatela2 = input('')
escolha = int(input('Agora que você já conhece os caminhos, qual cano vai escolher ?\n'))

if escolha == 1:
    print('Entramos nessa barulheira, mas descobrimos que esse barulho é de um vulcão subterrâneo\n'
          'que acabou de ser reativado, e seu personagem não tem mais como fugir! Você morreu! JOGAR NOVAMENTE\n')
elif escolha == 2:
    print('Ardeu os olhos para entrar mas aqui dentro é tudo escuro e não tem luz alguma para me mover,\n'
          'EPA!! O QUE É ISSO??!! Você morreu! JOGAR NOVAMENTE')
elif escolha == 3:
    print('Entramos nesse cano esperando o pior, e nada de suspeito. Realmente nada acontece aqui dentro,\n'
          'caminhamos até o outro lado e saímos do cano sem novidades, porém vivo!\n')

if escolha == 3:
    print('Maravilhaaaa, se você entrou no cano 3, você conseguiu atravessar, mas para prosseguir você não pode\n'
          'estar infectado, e faremos esta verificação agora.')

verificacao(caminho)
if verificacao(caminho) == True:
    print('Você está infectado, infelizmente você não pode entrar e vai ter que continuar sem o alcool em gel')
elif verificacao(caminho) == False:
    print('Que bom que você não está infectado, vamos prosseguir já que agora conseguimos a Máscara!')

print('Estamos no terceiro e último cenário do jogo, você já tem dois itens importantes.')

print('Há um fila enorme e precisamos passar por uma última barreira, a verificação de covid e itens essenciais')