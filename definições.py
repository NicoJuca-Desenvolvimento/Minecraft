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
            '[rR]edstone': 1 #inicio da aventura 1
        }
    },
    1: { #inicio da aventura 1
        'frases': ['**Dia 11/09/2022**, você e seu amigo estavam andando de bicicleta, quando se depara com um celular caído no centro histórico de São José, por conta da curiosidade você pega ele e se depara com uma mensagem, que dizia o seguinte:|*"Finalmente alguem me encontrou, estava ansioso para mostrar o novo mundo que criei, cheio de desafios, você esta pronto para começar a aventura?*" (Digite o número referente a sua decisão)|:one: - Sim, vamos nessa! |:two: - Não, to fora.'],
        'proximos_estados': {
            '1': 2, #inicio da aventura 1.1
            '2': 3 #inicio da aventura 1.2
        }
    },
    2: { #inicio da aventura 1.1
        'frases': ['Olá, parece que você caiu em um mundo estranho, que se assemelha muito ao MINECRAFT, mas seu amigo não está com você!! E você olha para o seu pulso e ve uma pulseira com metade de uma pérola, teria seu amigo a outra metade? Vamos descobrir, afinal a única coisa que você quer é encontrar seu amigo e sair daqui! Vamos começar logo essa jornada, pois não sabemos o que nos aguarda aqui!|O que você deseja fazer primeiro?|:one: - Gritar pelo seu amigo.|:two: - Ir para dentro da floresta.|:three: - Procurar por rastros do seu amigo.'],
        'proximos_estados':{
            '1': 4, #dia 1.1
            '2': 5, #dia 1.2
            '3': 6 #dia 1.3
        } 
    },
    3: { #inicio da aventura 1.2
        'frases': ['Você não consegue mais largar o celular, ele esta completamente grudado em você, a seguinte mensagem apareceu:|"Agora você ja sabe da existencia deste celular, logo, você meio que não tem escolha, vamos logo."|:one: - Bom, então vamos.'],
        'proximos_estados':{
            '1': 2 #inicio da aventura 1.1
        }
    },
    4: { #Dia 1.1
        'frases': ['Você grita por seu amigo por algum tempo e acaba escutando alguns barulhos vindos da floresta, você assustado corre em direção do rio e ao chegar lá, com o sol se pondo, se senta pra descansar mas percebe que está com muita fome. O que fazer?|:one: - Ir atras de comida.|:two: - Ir dormir e procurar comida ao amanhecer.'],
        'proximos_estados':{
            '1': 7, #dia 1.4
            '2': 8 #dia 1.5
        }
    },
    5: { #Dia 1.2
        'frases': ['Você acaba procurando por seu amigo na floresta por um longo tempo na floresta, ve o sol se pondo e percebe que está sentindo muita fome, Que tal ir atrás de comida?|:one: - Ir atrás de comida.|:two: - Ir dormir e procurar comida ao amanhecer.'],
        'proximos_estados':{
            '1': 7, #dia 1.4
            '2': 8 #dia 1.5
        }       
    },
    6: { #Dia 1.3
        'frases': ['Você sai procurando por alguns rastros possivelmente deixados por seu amigo, e depois de um bom tempo andando, percebe que os rastros acabam em um riacho e ao chegar lá, com o sol se pondo, se senta pra descansar mas percebe que está com muita fome. O que fazer?|:one: - Ir atrás de comida.|:two: - Ir dormir e procurar comida ao amanhecer.'],
        'proximos_estados':{
            '1': 7, #dia 1.4
            '2': 8 #dia 1.5
        }        
    },
    7: { #dia 1.4
        'frases': ['Por sorte, logo no inicío da sua jornada atrás de alimento, você encontra um arco e 3 flechas jogados próximo a uma árvore, o arco está bem danificado mais ainda é possível utilizá-lo.|:one: - Pegar arco e flechas.|:two: - continuar sem nenhum armamento.'],
        'proximos_estados':{
            '1': 9, #dia 1.6
            '2': 10 #dia 1.7
        }
    },
    8: { #dia 1.5
        'frases': ['Dormir sem buscar comida não foi uma boa ideia, você acordou com muita fome, como estava desesperado atrás de alimento, pulou no rio para pegar um peixe e acabou sendo atacado por uma enguia elétrica.|**Você Morreu**|:one: - Voltar para o inicio.'],
        'proximos_estados':{
            '1': 2, #inicio da aventura 1.1
        }
    },
    9: { #dia 1.6
        'frases': ['Você coletou o arco e foi para uma planície logo a frente, lá você acerta 2 das 3 flechas e consegue abater 2 galinhas, garantindo comida para passar a noite.|Você está alimentado agora, mas também está extremamente cansado, o que fazer?|:one: - Continuar andando pela planície.|:two: - Dormir embaixo de alguns arbustos.'],
        'proximos_estados':{
            '1':11, #dia 1.12
            '2': 12 #dia 1.10
        }       
    },
    10: { #dia 1.7
        'frases': ['Você optou continuar sem o arco, já que não sabe os perigos desta floresta. Continua caminhando e consegue sair da floresta em que estava, logo você avista várias bagas doces, uma frutinha que cresce nos arbustos da região, você se encontra com muita fome, e não ve mais nada ao horizonte, talvez seja a sua única opção. O que fazer?|:one: - Comer as frutinhas.|:two: - Continuar procurando.'],
        'proximos_estados':{
            '1':13, #dia 1.8
            '2':14 #dia 1.9
        }
    },
    11: { #dia 1.12
        'frases': ['Você continuou andando pela planície e começa a ver bastante fumaça e luzes a frente, ao chegar mais perto vê uma especie de vila, com casas e alguns aldeões, a princípio amigáveis. O que deseja fazer?|:one: - Ir em direção a vila.|:two: - Se afastar da vila.'],
        'proximos_estados':{
            '1': 15, #dia 1.13
            '2': 16 #dia 1.14
        }
    },
    12: { #dia 1.10
        'frases': ['Você é acordado por um grupo de 3 exploradores um pouco estranhos, você fica um pouco assustado, mas eles te acalmam e te convidam a conhecer a pequena vila deles. Apesar de ter comido você ainda estava com fome, provavelmente ir junto com os exploradores é a melhor opção.|:one: - Seguir em direção ao vilarejo.'],
        'proximos_estados':{
            '1': 17, #dia 1.11
        }
    },
    13: { #dia 1.8
        'frases': ['Você andou por muito tempo e não encontrou nada para comer, ficando sem energia por conta da fome. Você avista 2 homens ao horizonte, gasta suas ultimas energias correndo e gritando na direção deles, mas ao chegar perto ve que na verdade eram dois zumbis, que se aproximam de você, que não consegue fugir e desmaia por ali mesmo.|**Você Morreu.**|:one: - Voltar para o inicio.'],
        'proximos_estados':{
            '1': 2 #inicio da aventura 1.1
        }
    },
    14: { #dia 1.9
        'frases': ['As frutinhas não fizeram mal algum, e agora você se encontra muito bem alimentado, porém exausto. O que deseja fazer?|:one: - Continuar andando pela planície.|:two: - Dormir embaixo de alguns arbustos.'],
        'proximos_estados':{
            '1': 11, #dia 1.12
            '2': 12 #dia 1.10
        }
    },
    15: { #dia 1.13
        'frases': ['Andando em direção a vila, você encontra com um homem e ele lhe pergunta o que faz a essa hora andando pelo pasto.|:one: - *"Estou com um pouco de fome, pode me ajudar?"*'],
        'proximos_estados':{
            '1': 18 #dia 1.15
        }    
    },
    16: { #dia 1.14
        'frases': ['Quando você vira as costas para a vila, escuta um homem chamando você e então para conversar um pouco.|Homem desconhecido: *"Olá meu jovem, o que faz essa hora andando pelo pasto? Está precisando de alguma ajuda?"*|:one: - *"Estava em busca de comida, vi essas luzes e decidi me aproximar."*|:two: - *"Estou perdido e não sei o que estou fazendo aqui, pode me ajudar?"*'],
        'proximos_estados':{
            '1': 18, #dia 1.15
            '2': 18 #dia 1.15
        }
    },
    17: { #dia 1.11
        'frases': ['Ao chegar na Vila, os exploradores continuam a sua aventura e você é recebido por um homem que estava lá no local, ele estende a mão para lhe cumprimentar.|:one: - Cumprimentar o homem e falar como está cansado.'],
        'proximos_estados':{
            '1': 18, #dia 1.15
        }
    },
    18: { #dia 1.15
        'frases': ['Homem Desconhecido: *"Certo rapaz, vamos entrar e tomar uma chicará de chá, pelo menos para não passar essa noite na rua, pode confiar na gente, nós somos apenas aldeões que cultivam plantas nesta pequena vila, temos algumas camas sobrando também, vamos entrar?"*|:one: - *"Certo, afinal estou com muito sono mesmo!"*'],
        'proximos_estados':{
            '1': 19 #dia 1.16
        }
    },
    19: { #dia 1.16
        'frases': ['Aldeão: *"Ok, vamos lá!"*|**Dentro da cabana**|Aldeão: *"Bom, aparentemente preciso lhe informar algumas coisas sobre este mundo... Aqui dentro você tem duas opções, vivar para o resto da sua vida cuidando de animais e plantações para sobreviver, ou tentar encontrar o rapaz que veio com você, e seguir as instruções do livro do fim para encontrar o portal de volta para seu mundo, ai você pode voltar a sua vida normal na terra."*|:one: - *"Como você sabe sobre o meu amigo?"*|:two: - *"Conte mais sobre o livro."*'],
        'proximos_estados':{
            '1': 20, #dia 1.17
            '2': 21 #dia 1.18
        }
    },
    20: { #dia 1.17
        'frases': ['Aldeão: *"Ninguém aqui veio sozinho, todos viemos acompanhados de alguem, porém apenas 1 dupla conseguiu se encontrar, o que não adiantou muito já que falharam no desafio final do livro do fim."*|:one: - *"Me conte mais sobre o livro."*'],
        'proximos_estados':{
            '1': 21 #dia 1.18
        }
    },
    21: { #dia 1.18
        'frases': ['Aldeão: *"O livro é bem grande, temos uma cópia dele aqui na vila, posso lhe entregar para dar uma lida se quiser, mas basicamente ele te da 3 desafios antes de voltar para casa... O primeiro, encontrar a pessoa que possui a mesma pulseira que você. O segundo, encontrar o portal do fim e então lá dentro você tem o terceiro desafio, matar o poderoso dragão. A cabeça do dragão lhe permitirá abrir o portal de volta para casa."*|**Você adquiriu o livro do fim**|:one: - *"Muito obrigado pela ajuda, vou descansar um pouco agora."*'],
        'proximos_estados':{
            '1': 22 #dia 2.2
        }
    },
}

partidas = {}

        'frases': [''],
        'proximos_estados':{
            
        }