frases = {
    'inventario_insuficiente': 'Sem os recursos necessários para avançar.',
    'canal_privado': 'Por favor, envie mensagens para mim através de canal compartilhado de texto (não pvt).',
    'sem_canal_de_voz': 'Por favor, esteja em um canal de voz para ter a imersão necessária do jogo.',
    'erro': 'I\'m sorry Dave, I\'m afraid I can\'t do that.'
}

estados = {
    0: {
        'frases': ['Digite "Redstone" para começar o jogo.'],
        'proximos_estados': {
            '[rR]edstone': 1 
        }
    },
    1: { #inicio da aventura 1
        'frases': ['**Dia 11/09/2022**, você e seu amigo estavam andando de bicicleta, quando se depara com um celular caído no centro histórico de São José, por conta da curiosidade você pega ele e se depara com uma mensagem, que dizia o seguinte:|*"Finalmente alguem me encontrou, estava ansioso para mostrar o novo mundo que criei, cheio de desafios, você esta pronto para começar a aventura?*" (Digite o número referente a sua decisão)|:one: - Sim, vamos nessa! |:two: - Não, to fora.'],
        'proximos_estados': {
            '1': 2,
            '2': 3
        }
    },
    2: { #inicio da aventura 1.1
        'frases': ['Olá, parece que você caiu em um mundo estranho, que se assemelha muito ao MINECRAFT, mas seu amigo não está com você!! E você olha para o seu pulso e ve uma pulseira com metade de uma pérola, teria seu amigo a outra metade? Vamos descobrir, afinal a única coisa que você quer é encontrar seu amigo e sair daqui! Vamos começar logo essa jornada, pois não sabemos o que nos aguarda aqui!|O que você deseja fazer primeiro?|:one: - Gritar pelo seu amigo.|:two: - Ir para dentro da floresta.|:three: - Procurar por rastros do seu amigo.'],
        'proximos_estados':{
            '1': 4,
            '2': 5,
            '3': 6
        } 
    },
    3: { #inicio da aventura 1.2
        'frases': ['Você não consegue mais largar o celular, ele esta completamente grudado em você, a seguinte mensagem apareceu:|"Agora você ja sabe da existencia deste celular, logo, você meio que não tem escolha, vamos logo."|:one: - Bom, então vamos.'],
        'proximos_estados':{
            '1': 2
        }
    },
    4: { #Dia 1.1
        'frases': ['Você grita por seu amigo por algum tempo e acaba escutando alguns barulhos vindos da floresta, você assustado corre em direção do rio e ao chegar lá, com o sol se pondo, se senta pra descansar mas percebe que está com muita fome. O que fazer?|:one: - Ir atras de comida.|:two: - Ir dormir e procurar comida ao amanhecer.'],
        'proximos_estados':{
            '1': 7,
            '2': 8
        }
    },
    5: { #Dia 1.2
        'frases': ['Você acaba procurando por seu amigo na floresta por um longo tempo na floresta, ve o sol se pondo e percebe que está sentindo muita fome, Que tal ir atrás de comida?|:one: - Ir atrás de comida.|:two: - Ir dormir e procurar comida ao amanhecer.'],
        'proximos_estados':{
            '1': 7,
            '2': 8
        }       
    },
    6: { #Dia 1.3
        'frases': ['Você sai procurando por alguns rastros possivelmente deixados por seu amigo, e depois de um bom tempo andando, percebe que os rastros acabam em um riacho e ao chegar lá, com o sol se pondo, se senta pra descansar mas percebe que está com muita fome. O que fazer?|:one: - Ir atrás de comida.|:two: - Ir dormir e procurar comida ao amanhecer.'],
        'proximos_estados':{
            '1': 7,
            '2': 8
        }        
    },
    7: { #dia 1.4
        'frases': ['Por sorte, logo no inicío da sua jornada atrás de alimento, você encontra um arco e 3 flechas jogados próximo a uma árvore, o arco está bem danificado mais ainda é possível utilizá-lo.|:one: - Pegar arco e flechas.|:two: - continuar sem nenhum armamento.'],
        'proximos_estados':{
            '1': 9,
            '2': 10
        }
    },
    8: { #dia 1.5
        'frases': ['Dormir sem buscar comida não foi uma boa ideia, você acordou com muita fome, como estava desesperado atrás de alimento, pulou no rio para pegar um peixe e acabou sendo atacado por uma enguia elétrica.|**Você Morreu**|:one: - Voltar para o inicio.'],
        'proximos_estados':{
            '1': 2,
        }
    },
    9: { #dia 1.6
        'frases': ['Você coletou o arco e foi para uma planície logo a frente, lá você acerta 2 das 3 flechas e consegue abater 2 galinhas, garantindo comida para passar a noite.|Você está alimentado agora, mas também está extremamente cansado, o que fazer?|:one: - Continuar andando pela planície.|:two: - Dormir embaixo de alguns arbustos.'],
        'proximos_estados':{
            '1': 11,
            '2': 12
        }
    },
    10: { #dia 1.7
        'frases': ['Você optou continuar sem o arco, já que não sabe os perigos desta floresta. Continua caminhando e consegue sair da floresta em que estava, logo você avista várias bagas doces, uma frutinha que cresce nos arbustos da região, você se encontra com muita fome, e não ve mais nada ao horizonte, talvez seja a sua única opção. O que fazer?|:one: - Comer as frutinhas.|:two: - Continuar procurando.'],
        'proximos_estados':{
            '1': 13,
            '2': 14
        }
    },
    11: { #dia 1.12
        'frases': ['Você continuou andando pela planície e começa a ver bastante fumaça e luzes a frente, ao chegar mais perto vê uma especie de vila, com casas e alguns aldeões, a princípio amigáveis. O que deseja fazer?|:one: - Ir em direção a vila.|:two: - Se afastar da vila.'],
        'proximos_estados':{
            '1': 15,
            '2': 16
        }
    },
    12: { #dia 1.10
        'frases': ['Você é acordado por um grupo de 3 exploradores um pouco estranhos, você fica um pouco assustado, mas eles te acalmam e te convidam a conhecer a pequena vila deles. Apesar de ter comido você ainda estava com fome, provavelmente ir junto com os exploradores é a melhor opção.|:one: - Seguir em direção ao vilarejo.'],
        'proximos_estados':{
            '1': 17
        }
    },
    13: { #dia 1.8
        'frases': ['Você andou por muito tempo e não encontrou nada para comer, ficando sem energia por conta da fome. Você avista 2 homens ao horizonte, gasta suas ultimas energias correndo e gritando na direção deles, mas ao chegar perto ve que na verdade eram dois zumbis, que se aproximam de você, que não consegue fugir e desmaia por ali mesmo.|**Você Morreu.**|:one: - Voltar para o inicio.'],
        'proximos_estados':{
            '1': 2
        }
    },
    14: { #dia 1.9
        'frases': ['As frutinhas não fizeram mal algum, e agora você se encontra muito bem alimentado, porém exausto. O que deseja fazer?|:one: - Continuar andando pela planície.|:two: - Dormir embaixo de alguns arbustos.'],
        'proximos_estados':{
            '1': 11,
            '2': 12
        }
    },
    15: { #dia 1.13
        'frases': ['Andando em direção a vila, você encontra com um homem e ele lhe pergunta o que faz a essa hora andando pelo pasto.|:one: - *"Estou com um pouco de fome, pode me ajudar?"*'],
        'proximos_estados':{
            '1': 18
        }    
    },
    16: { #dia 1.14
        'frases': ['Quando você vira as costas para a vila, escuta um homem chamando você e então para conversar um pouco.|Homem desconhecido: *"Olá meu jovem, o que faz essa hora andando pelo pasto? Está precisando de alguma ajuda?"*|:one: - *"Estava em busca de comida, vi essas luzes e decidi me aproximar."*|:two: - *"Estou perdido e não sei o que estou fazendo aqui, pode me ajudar?"*'],
        'proximos_estados':{
            '1': 18,
            '2': 18
        }
    },
    17: { #dia 1.11
        'frases': ['Ao chegar na Vila, os exploradores continuam a sua aventura e você é recebido por um homem que estava lá no local, ele estende a mão para lhe cumprimentar.|:one: - Cumprimentar o homem e falar como está cansado.'],
        'proximos_estados':{
            '1': 18
        }
    },
    18: { #dia 1.15
        'frases': ['Homem Desconhecido: *"Certo rapaz, vamos entrar e tomar uma chicará de chá, pelo menos para não passar essa noite na rua, pode confiar na gente, nós somos apenas aldeões que cultivam plantas nesta pequena vila, temos algumas camas sobrando também, vamos entrar?"*|:one: - *"Certo, afinal estou com muito sono mesmo!"*'],
        'proximos_estados':{
            '1': 19
        }
    },
    19: { #dia 1.16
        'frases': ['Aldeão: *"Ok, vamos lá!"*|**Dentro da cabana**|Aldeão: *"Bom, aparentemente preciso lhe informar algumas coisas sobre este mundo... Aqui dentro você tem duas opções, vivar para o resto da sua vida cuidando de animais e plantações para sobreviver, ou tentar encontrar o rapaz que veio com você, e seguir as instruções do livro do fim para encontrar o portal de volta para seu mundo, ai você pode voltar a sua vida normal na terra."*|:one: - *"Como você sabe sobre o meu amigo?"*|:two: - *"Conte mais sobre o livro."*'],
        'proximos_estados':{
            '1': 20,
            '2': 21
        }
    },
    20: { #dia 1.17
        'frases': ['Aldeão: *"Ninguém aqui veio sozinho, todos viemos acompanhados de alguem, porém apenas 1 dupla conseguiu se encontrar, o que não adiantou muito já que falharam no desafio final do livro do fim."*|:one: - *"Me conte mais sobre o livro."*'],
        'proximos_estados':{
            '1': 21
        }
    },
    21: { #dia 1.18
        'frases': ['Aldeão: *"O livro é bem grande, temos uma cópia dele aqui na vila, posso lhe entregar para dar uma lida se quiser, mas basicamente ele te da 3 desafios antes de voltar para casa... O primeiro, encontrar a pessoa que possui a mesma pulseira que você. O segundo, encontrar o portal do fim e então lá dentro você tem o terceiro desafio, matar o poderoso dragão. A cabeça do dragão lhe permitirá abrir o portal de volta para casa."*|**Você adquiriu o livro do fim**|:one: - *"Muito obrigado pela ajuda, vou descansar um pouco agora."*'],
        'proximos_estados':{
            '1': 22
        }
    },
    22: { #dia 2.2
        'frases': ['**Checkpoint**|Após descansar um pouco a noite e refletir sobre o que o aldeão falou, você se depara com um dilema, afinal você precisa saber onde seu amigo está, mas você está de mãos vazias para entrar em um "combate".|:one: - Ler o livro.|:two: - Sair em uma jornada atrás de looting.|:three: - Ir para floresta pegar madeira e craftar uma picareta.'],
        'proximos_estados':{
            '1': 23,
            '2': 24,
            '3': 25
        }
    },
    23: { #livro
        'frases': ['```Olá viajante, seja bem vindo ao mundo do MINECRAFT, eu sei que você não quer estar aqui assim como seu amigo. Ele não começou a jornada ao seu lado mas precisa terminar, para que isso seja concluido da forma correta é necessário juntar os olhos em seus pulsos em cima de uma piscina de lava na biblioteca sombria nos fundos de uma mina abandonada. Os olhos possuem um grande poder, quando os 2 viajantes descobrem como sair desse mundo, os olhos brilham como o sol e olham em direção ao seu olho irmão. Passando do portal você ainda não estará livre, no mundo do fim há um gigantesco desafio, assim como na era medieval voces terão de trabalhar em equipe para derrotar o dragão e assim se libertarem dessa criação.```|:one: - Voltar.'],
        'proximos_estados':{
            '1': 22
        }
    },
    24: { #dia 2.3
        'frases': ['Ao sair em uma jornada você segue por um longo tempo e acaba achando uma pequena cabana de tijolos com chaminé saindo fumaça. Por ter andado muito tempo você parece um pouco cansado e já sente fome. Pode ser que tenha alguém ali.|:one: - Ir na floresta atrás de uma galinha e retornar para a cabana.|:two: - Bater na porta da cabana.'],
        'proximos_estados':{
            '1': 28,
            '2': 29
        }
    },
    25: { #dia 2.4
        'frases': ['Você foi em direção para floresta de pinheiro a frente e conseguiu adquiriu algumas madeiras e fez uma picareta de madeira e está pronto para minerar, só precisa encontrar alguma caverna. Caminhando por pouco mais de uma hora, você finalmente encontra uma mina.|:one: - Ir minerar.'],
        'proximos_estados':{
            '1': 26
        }
    },
    26: { #dia 2.5
        'frases': ['Parabéns, você possui uma picareta de madeira e foi em busca de minérios e acabou conseguindo algumas pedras e melhorando sua picareta, continuou no trabalho duro e conseguiu bastante ferro, se quiser voce pode fazer algumas armas.|:one: - Continuar minerando.|:two: - Fazer armamento.'],
        'proximos_estados':{
            '1': 27,
            '2': 32
        }
    },
    27: { #dia 2.6
        'frases': ['O resto do tempo que passou minerando não lhe rendeu muitos recursos, você acabou se cansando bastante e a noite está próxima, a melhor opção é craftar suas armas.|:one: - Guardar minérios e voltar para a vila.|:two: - Fazer armamento.'],
        'proximos_estados':{
            '1': 31,
            '2': 32
        }
    },
    28: { #dia 2.7
        'frases': ['Com a flecha que sobrou da primeira caçada, e após ter pego um pouco a prática você usou uma flecha para pegar 2 coelhos em 1 cajadada só, assim você descansa e se alimenta nesse fim de tarde e está na hora de ir para a cabana.|:one: - Voltar para a cabana.'],
        'proximos_estados':{
            '1': 29
        }
    },
    29: { #dia 2.8
        'frases': ['Ao chegar perto da cabana você começa a escutar a lenha da chaminá estalando por conta da janela da sala estar aberta, então você bate na porta algumas vezes porém sem resposta da parte de dentro.|Já está escuro lá fora, e alguns lobos começam a uivar na floresta.|:one: - Entrar silenciosamente na cabana.|:two: - Não entrar na casa de um estranho e achar outro lugar para passar a noite.'],
        'proximos_estados':{
            '1': 30,
            '2': 33
        }
    },
    30: { #dia 2.9
        'frases': ['Ao abrir a porta você acaba fazendo um barulho muito alto, talvez está casa seja meio velha, o barulho acaba acordando um senhor que vem correndo em direção à porta de entrada.|Homem barbudo: *"QUEM É VOCÊ? O QUE FAZ AQUI?"*|:one: - Cair no soco com o velho.|:two: - *"Sou apenas um viajante atrás de ajuda, não fique nervoso, vamos conversar."*'],
        'proximos_estados':{
            '1': 39,
            '2': 40
        }
    },
    31: { #dia 2.10
        'frases': ['Continuar sem armas não foi uma boa opção, no caminho de volta para a vila você é cercado por monstros, por mais que tenha tentado gritar por ajuda, nínguem estava próximo para ajudá-lo.|**Você Morreu.**|:one: - Voltar para o checkpoint.'],
        'proximos_estados':{
            '1': 22
        }
    },
    32: { #dia 2.11
        'frases': ['Você conseguiu fazer sua armadura e espada com o ferro que adquiriu, voltando para a vila você começa a ficar com muita sede e fome, e ainda tem pelo menos mais uns 10 quilometros de caminhada até a vila, o que deseja fazer?|:one: - Ir em direção a vila.|:two: - Parar para caçar.'],
        'proximos_estados':{
            '1': 34,
            '2': 35
        }
    },
    33: { #noite 2
        'frases': ['Ao sair da cabana você vai em direção ao riacho para tentar encontrar alguma casa vizinha a cabana, porém sem sorte, então acaba descansando por ali mesmo.|No meio da noite você acorda com uivos muito barulhentos ao seu redor, e percebe que estás cercado por 2 lobos claramente com fome.|:one: - Usar o arco para se defender.|:two: - Ir se afastando e correr em direção a cabana.'],
        'proximos_estados':{
            '1': 41,
            '2': 42
        }
    },
    34: { #dia 2.12
        'frases': ['Depois de caminhar cerca de 5 quilometros,  você percebe que não vai conseguir chegar vivo por causa da desidratação, tem certeza que quer continuar?|:one: - Continuar caminhando.|:two: - Parar para caçar.'],
        'proximos_estados':{
            '1': 36,
            '2': 35
        }
    },
    35: { #dia 2.13
        'frases': ['Sua caça foi muito bem sucedida, com a espada você consegue matar 1 porco, então fez uma fogueira e assou a carne, ficando muito bem alimentado.|O tempo vai passando e o clima vai esfriando, começa a cair um pouco de neve, e sua roupa não vai conseguir esquentá-lo durante uma nevasca, por sorte, avista um cavalo manso, que pode levá-lo rapidamente de volta para a vila.|:one: - Montar no cavalo e ir até a vila.|:two: - Passar a noite do lado da fogueira.'],
        'proximos_estados':{
            '1': 37,
            '2': 38
        }
    },
    36: { #dia 2.14
        'frases': ['A fome e a desidratação fizeram com que você desmaiasse, durante a noite ainda cai uma nevasca e então você morre congelado no meio da floresta.|```Lembre-se que aqui é tudo diferente, inclusive o tempo que pode ficar sem comer e/ou beber água```|:one: - Voltar para o checkpoint.'],
        'proximos_estados':{
            '1': 22
        }
    },
    37: { #dia 2.15
        'frases': ['O cavalo era muitó dócil e vocês se deram muito bem, depois de montar em cima dele não demorou muito para que chegasse em segurança na vila. Ao chegar, logo leva o cavalo até o estábulo dos aldeões, para que ele passe a noite em segurança, seu novo amigo lhe ajudará muito futuramente, você o apelidou de pé de pano.|:one: - Ir descansar.'],
        'proximos_estados':{
            '1': 57
        }
    },
    38: { #dia 2.16
        'frases': ['Passaram-se 2 horas desde o momento que decidiu deixar o cavalo ir embora e ficar ao lado da fogueira, que acabou apagando quando a nevasca começou, o frio extremo fez com que seu corpo todo congelasse, começando pelos dedos dos pés e das mãos.|**Você Morreu**|:one: - Voltar para o checkpoint.'],
        'proximos_estados':{
            '1': 22
        }
    },
    39: { #dia 2.17
        'frases': ['Você corre em direção ao homem tentando atingi-lo com um soco, mas o senhor acaba desviando, mostrando incríveis reflexos.|Homem barbudo: *"Você invadiu a cabana do cara errado, vai se arrepender por isso!"*|O homem pega então uma frigideira, muito similar a do free fire, e lhe atinge com uma forte pancada no queixo.|**Você Morreu**|:one: - Voltar para o checkpoint.'],
        'proximos_estados':{
            '1': 22
        }
    },
    40: { #dia 2.18
        'frases': ['Homem barbudo: *"Você tem alguma arma aí?"*|Você: *"Apenas um arco velho, mas sem flechas, quer que eu o deixe aqui na entrada?"*|Homem barbudo: *"Faça isso mesmo... Depois pode se sentar ali no sofá, imagino que tenha algo para me perguntar."*|:one: - Ir para cima do velho no momento que ele vira de costas.|:two: - Sentar-se e perguntar se o senhor pode lhe ajudar com alguns itens.'],
        'proximos_estados':{
            '1': 39,
            '2': 46
        }
    },
    41: { #noite 2.1
        'frases': ['Por estar sem flechas você usaria o próprio arco para tentar se defender dos múltiplos ataques dos lobos, você consegue desviar de alguns ataques batendo nos lobos com seu arco, porém em um ataque surpresa você coloca o arco na frente e acaba sendo abocanhado pelo lobo e se quebra.|Após um logo embate sem armamento dessa vez, os lobos acabam conseguindo o que querem e você vira comida de lobo.|**Você Morreu**|:one: - Voltar para o checkpoint.'],
        'proximos_estados':{
            '1': 22
        }
    },
    42: { #noite 2.2
        'frases': ['A cabana se encontra meio longe, e mesmo correndo o mais rápido que você podia, os lobos conseguem chegar até você, que não consegue se defender apenas com um arco.|**Você Morreu**|:one: - Voltar para o checkpoint.'],
        'proximos_estados':{
            '1': 22
        }
    },
    44: { #dia 2.20
        'frases': ['Noel: *"No meu rancho tenho algumas armaduras que usei na viagem, e aqui no estábulo ao lado tenho um cavalo que usei na jornada até o portal. Eu atualmente não tenho mais o tamanho para usar as armaduras, e até perdi a cavalgada e não consigo mais andar com o pé de pano."*|:one: - *"Posso olhar o cavalo?"*|:two: - *"Posso ver as armaduras?"*'],
        'proximos_estados':{
            '1': 47,
            '2': 48
        }
    },
    46: { #dia 2.22
        'frases': ['Caminhando até o sofá, você se depara com uma foto de dois homens, então acaba esquecendo dos itens e se interessando pela história deste cara misterioso.|Você: *"Você é o homem do quadro então, quem é esse ao seu lado? quem é voĉe?"*|Noel: *"Bom, me chamo Noel, e acredito que ja deve saber como funciona este mundo... Este ao meu lado é meu amigo e fomos os únicos que conseguiram se encontrar até hoje, porém no dia em que faríamos o desafio final do livro, Martin pulou no portal, e eu não tive coragem de fazer o mesmo, desde então nunca mais eu o vi, e minha pulseria ja parou de brilhar, acredito que ele tenha morrido e eu perdi a chance de voltar para a casa, também não consegui voltar para a vila e contar a todos o que aconteceu."*|Você: *"Nossa, eu ainda nem encontrei meu amigo, só que com tudo que o senhor me disse me deixou extremamente preocupado com o que pode acontecer, mas acho que tanto ele como eu queremos voltar as nossas vidas normais, alias...."*|:one: - *"Será que você poderia me ajudar com alguns itens?"*'],
        'proximos_estados':{
            '1': 44
        }
    },
    47: { #dia 2.23
        'frases': ['Noel: *"Claro, me acompanhe"*|```Noel leva você até o lado de fora da cabana, onde esta o cavalo```|Noel: *"Esse é o pé de pano, é um cavalo extremamente dócil e saudável, trato ele como meu filho, é o unico companheiro que tenho, mas ele sente muito falta de correr pelos campos e infelizmente não consigo mais levá-lo, se quiser pode ficar com ele, acredito que será de grande ajuda na sua jornada e também irá fazer pé de pano mais feliz."*|Você: *"É um cavalo bonito, não acredito que ele está a tanto tempo sem correr, seu porte ainda está incrível... Eu aceito ficar com pé de pano."*|Noel: *"Ótimo, quer dar uma olhada nas armaduras?"*|:one: - *"Sim, vamos lá."*|:two: - *"Agora não, preciso ir. Mas muito obrigado por toda a ajuda."*'],
        'proximos_estados':{
            '1': 49,
            '2': 50
        }
    },
    48: { #dia 2.24
        'frases': ['```Você e Noel caminham até o rancho do lado de fora da cabana```|Noel: *"Aqui está, essas foram as roupas que utilizei durante toda minha jornada de sair deste mundo, a maioria está bem danificada, exceto essa daqui do canto, era a roupa que eu teria que utilizar no dia do desafio final..."*|Noel puxa então uma armadura completa de ferro de dentro do armário, a armadura se encontra novinha, sem nenhum arranhão, junto dela, Noel ainda lhe oferece a sua espada.|:one: - Aceitar o armamento e perguntar pelo cavalo.|:two: - Aceitar o armamento e ir para casa.'],
        'proximos_estados':{
            '1': 52,
            '2': 53
        }
    },
    49: { #dia 2.25
        'frases': ['```Você e Noel caminham até o rancho do lado de fora da cabana```|Noel: "Aqui está, essas foram as roupas que utilizei durante toda minha jornada de sair deste mundo, a maioria está bem danificada, exceto essa daqui do canto, era a roupa que eu teria que utilizar no dia do desafio final..."|Noel puxa então uma armadura completa de ferro de dentro do armário, a armadura se encontra novinha, sem nenhum arranhão, junto dela, Noel ainda lhe oferece a sua espada.|:one: - Aceitar o armamento|:two: - Recusar a armadura e ir para casa'],
        'proximos_estados':{
            '1': 51,
            '2': 50
        }
    },
    50: { #dia 2.26
        'frases': ['Voltando para a vila ao fim da tarde, você é cercado por uma alcateia inteira, com cerca de 7 lobos, por mais que tente fugir, os lobos atacam pé de pano que fica imobilizado no chão, como não tem nenhuma arma em mãos, os lobos vão pra cima de você e não há quem possa te defender.|**Você morreu**|:one: - Voltar para o checkpoint.'],
        'proximos_estados':{
            '1': 22
        }
    },
    51: { #dia 2.27
        'frases': ['Noel: "Bom, isso era tudo que eu tinha para lhe oferecer, e por experiência própria, sei que é tudo que precisa para sair deste mundo caso encontre seu amigo..."|:one: - Ir para vila->Dia 2.30'],
        'proximos_estados':{
            '1': 54
        }
    },
    52: { #dia 2.28
        'frases': ['Noel: "*Vamos lá ver o pé de pano então, me acompanhe.*"|```Noel leva você até seu estábulo```|Noel: "*Esse é o pé de pano, é um cavalo extremamente dócil e saudável, trato ele como meu filho, é o unico companheiro que tenho, mas ele sente muito falta de correr pelos campos e infelizmente não consigo mais levá-lo, se quiser pode ficar com ele, acredito que será de grande ajuda na sua jornada e também irá fazer pé de pano mais feliz.*"|Você:"*É um cavalo bonito, não acredito que ele está a tanto tempo sem correr, seu porte ainda está incrível... Eu aceito ficar com pé de pano.*"|Noel: "*Que bom, fico feliz pelo pé de pano, ele sente falta de uma aventura!*"|:one: - Agradecer por toda a ajuda e ir para casa|:two: - Perguntar se Noel pode lhe ajudar com algo mais'],
        'proximos_estados':{
            '1': 51,
            '2': 51
        }
    },
    53: { #dia 2.29
        'frases': ['Você agredece pelo equipamento que Noel lhe forneceu e começa a caminhar de volta para casa.|No meio do caminho, começa uma imensa nevasca, que lhe pega de maneira desprevinida, você tenta se esconder, acender uma lareira mas nada funciona, e então seus dedos dos pés e das mãos começam a congelar, assim como a ponta do seu nariz e orelhas...|**Você morreu**|:one: - Voltar para o checkpoint.'],
        'proximos_estados':{
            '1': 22
        }
    },
    54: { #dia 2.30
        'frases': ['Voltando para a vila, o tempo começa a esfriar, você percebe que no outro dia se encontra em um novo desafio, a baixa temperatura.|Passaram alguns minutos e você se encontra perto do seu destino, mas então percebe que está sendo seguido por uma alcateia, com cerca de 7 lobos, você precisa tomar uma decisão imediatamente.|:one: - Lutar contra os lobos com os armamentos que Noel lhe forneceu.|:two: Fugir.'],
        'proximos_estados':{
            '1': 55,
            '2': 56
        }
    },
    55: { #dia 2.31
        'frases': ['Quando os lobos se aproximam, você desce do pé de pano e o esconde atrás de alguns arbustos, os lobos então correm em sua direção, você não sente a dor de nenhuma mordida, a armadura e muito resistente, e então, abate os 7 lobos depois de cerca de meia hora de batalha.|Agora seguros, podem continuar seu retorno para a vila, ao chegar, um aldeão lhe pergunta porque sua armadura está com tanto sangue.|Você: "*Fui atacado por uma alcateia, por sorte consegui salvar a mim e ao meu cavalo.*"|Aldeão: "*Ó céus, imagino que esteja exausto, deixa que levo o seu cavalo até o estábulo, pode ir descansar.*"|Você deixa o aldeão levar pé de pano até o estábulo, e vai direto para a casa do aldeão que lhe abrigou no primeiro dia para descansar.|:one: - Continuar História.'],
        'proximos_estados':{
            '1': 57
        }
    },
    56: { #dia 2.32
        'frases': ['Ao perceber a aproximação dos lobos, você começa a correr com pé de pano e consegue fugir de alcateia e chegar na vila em segurança.|Você se encontra extremamente cansado, ao chegar vai direto para o estábulo deixar o pé de pano e em seguida ja vai para casa do aldeão para descansar.|:one: - Continuar história...'],
        'proximos_estados':{
            '1': 57
        }
    },
    57: { #dia 3.0
        'frases': ['```CHECKPOINT```|Dia 3- Você acorda decidido que hoje será o dia que você irá atrás de seu amigo perdido para que consigam chegar ao portal juntos e enfim ir para casa, porém o clima na rua está realmente muito frio, com certos flocos de neve caindo.|```Indo ao estábulo do Pé de pano```|Chegando lá, você repara que ele está meio cabisbaixo, parecendo estar doente, justamente por causa do clima, ele realmente seria útil na jornada atrás do seu amigo.|:one: - Pedir ajuda ao aldeão.|:two: - Continuar sem o pé de pano.'],
        'proximos_estados':{
            '1': 58,
            '2': 59
        }
    },
    58: { #dia 3.1
        'frases': ['Chegando na casa do agricultor você pergunta se ele tem alguma comida que faça o seu cavalo se sentir bem, como uma maçã ou uma cenoura|Aldeão: "Temos sim, geralmente usamos alguma fruta ou legume dourado para alimentar os animais doentes, eles ficam guardados fora da vila, em um galpão na floresta aqui do lado, se quiser ir lá, basta pegar uma maçã dourada em baixo do fardo de feno número 3, mas cuidado com os outros, eles têm baús armadilha em baixo".|Você: "Ok eu acho que...|:one: - ...vou até o galpão buscar então"|:two: - ...vou continuar sem o pé de pano mesmo, se puder olhar o que aconteceu com ele eu agradeço"'],
        'proximos_estados':{
            '1': 60,
            '2': 77
        }
    },
    59: { #dia 3.2
        'frases': ['Você optou por continuar nessa jornada de encontrar seu amigo sem o pé de pano, atualmente você ainda não tem nenhuma pista do que pode ser feito para chegar até seu companheiro, mas está caminhando em direção ao sul e procurando por pistas.|O que deseja fazer?|:one: - Seguir em direção a floresta ao sul e acreditar que irá encontrar alguma pista.|:two: - Procurar ajuda em uma cabana que avistou ao horizonte.'],
        'proximos_estados':{
            '1': 73,
            '2': 74
        }
    },
    60: { #dia 3.3
        'frases': ['```Indo até o galpão```|Chegando lá perto da floresta você avisat um galpão com alguns blocos de trigos jogados pelo lado de fora e um cercado de porcos ao lado, assim que você entra percebe uma estrutura um pouco antiga, e logo ao fundo do galpão pode-se avistar 3 fardos de feno com uns quadros em cima.|No quadro do fardo da esquerda está escrito: O número deste fardo é o resultado da equação (7x5 + 2² - 2⁴)⁰;|No quadro do fardo do meio está escrito: O número deste fardo é a divisão da fração irredutivel da fração 1244/622;|No quadro do fardo da direita está escrito: O número deste fardo são o numero de olhos que um ser humano possúi.|**Qual fardo você irá olhar em baixo?**|:one: - Olhar em baixo do fardo a esquerda|:two: - Olhar em baixo do fardo do meio|:three: - Olhar em baixo do fardo a direita'],
        'proximos_estados':{
            '1': 61,
            '2': 62,
            '3': 63
        }
    },
    61: { #dia 3.4
        'frases': ['Todo número elvado a 0 acaba se tornando 1, e como o aldeão mesmo disse, era necessário tomar cuidado com as armadilhas.|Ao abrir o baú, o chão acaba se abrindo com um mecanismo de redstone e você cai em uma Piscina de lava.**Você morreu**|:one: - Voltar ao último CHeckpoint'],
        'proximos_estados':{
            '1': 57
        }
    },
    62: { #dia 3.5
        'frases': ['A fração irredutivel da fraçao mostrada seria igual a 2/1 então o resultado é 2, e como o aldeão mesmo disse, era necessário tomar cuidado com as armadilhas.|**Você morreu**|:one: - Voltar ao último CHeckpoint'],
        'proximos_estados':{
            '1': 57
        }
    },
    63: { #dia 3.6
        'frases': ['Em todo homem haverá 2 olhos que veem e um que será cego - Enzoquiel 24,18|*Biblia dos Patetas*|Ao olhar em baixo deste fardo você acha um baú com alguns itens dourados dentro, então pega uma maçã dourada e resolve levar até o vilarejo para dar ao seu cavalo.|:one: - Continuar história'],
        'proximos_estados':{
            '1': 64
        }
    },
    64: { #dia 3.7
        'frases': [''],
        'proximos_estados':{
        }
    },
    664: { #dia 3.8
        'frases': [''],
        'proximos_estados':{
        }
    },
    65: { #dia 3.9
        'frases': [''],
        'proximos_estados':{
        }
    },
    66: { #dia 3.10
        'frases': [''],
        'proximos_estados':{
        }
    },
    67: { #dia 3.11
        'frases': [''],
        'proximos_estados':{
        }
    },
    68: { #dia 3.12
        'frases': [''],
        'proximos_estados':{
        }
    },
    69: { #dia 3.13
        'frases': [''],
        'proximos_estados':{
        }
    },
    70: { #dia 3.14
        'frases': [''],
        'proximos_estados':{
        }
    },
    71: { #dia 3.15
        'frases': [''],
        'proximos_estados':{
        }
    },
    72: { #dia 3.16
        'frases': [''],
        'proximos_estados':{
        }
    },
    73: { #dia 3.17
        'frases': [''],
        'proximos_estados':{
        }
    },
    74: { #dia 3.18
        'frases': [''],
        'proximos_estados':{
        }
    },
    75: { #dia 3.19
        'frases': [''],
        'proximos_estados':{
        }
    },
    76: { #dia 3.20 (Diálogo)
        'frases': [''],
        'proximos_estados':{
        }
    },
    77: { #dia 3.21
        'frases': [''],
        'proximos_estados':{
        }
    },
    78: { #dia 3.22
        'frases': [''],
        'proximos_estados':{
        }
    },
    79: { #dia 3.23
        'frases': [''],
        'proximos_estados':{
        }
    },
    80: { #dia 3.24
        'frases': [''],
        'proximos_estados':{
        }
    },
    81: { #dia 3.25
        'frases': [''],
        'proximos_estados':{
        }
    },
    82: { #dia 3.26
        'frases': [''],
        'proximos_estados':{
        }
    },
    83: { #dia 3.27
        'frases': [''],
        'proximos_estados':{
        }
    },
}

partidas = {}