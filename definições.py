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
        'frases': ['Olá, parece que você caiu em um mundo estranho, que se assemelha muito ao MINECRAFT, mas seu amigo não está com você!! E você olha para o seu pulso e ve uma pulseira com metade de uma pérola, teria seu amigo a outra metade? Vamos descobrir, afinal a única coisa que você quer é encontrar seu amigo e sair daqui! Vamos começar logo essa jornada, pois não sabemos o que nos aguarda aqui!|O que você deseja fazer primeiro'],
        'proximos_estados':{
            '1': 4,
            '2': 5,
            '3': 6
        } 
    },
    3: { #inicio da aventura 1.2
        'frases': ['Você não consegue mais largar o celular, ele esta completamente grudado em você, a seguinte mensagem apareceu:|"Agora você ja sabe da existencia deste celular, logo, você meio que não tem escolha, vamos logo."'],
        'proximos_estados':{
            '1': 7
        }
    }
}

partidas = {}