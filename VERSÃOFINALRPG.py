#Ditadura do Linguini
PV=100
AE=0
FL=0
HW=0
CV=0
import sys
print("Uma Noite pra Lá de Maluca")
    #Instruções
print("Instruções: ao longo da história, você enfrentará diversas situações onde você terá que fazer escolhas.")
print("Suas escolhas influenciarão no decorrer do jogo.")
print("Você começa com 100 pontos de vida (PV). Ao longo do jogo, você pode se ferir e perder PV.")
print("Tenha cuidado, isso vai afetar a sua pontuação final.")
input("Aperte Enter para continuar ")
    #Começo da História
print("A história se passa em uma cidadezinha no interior de Rustyville. ")
print("Você estuda turismo na universidade local.")
nome=input("Seu nome é: ")
if nome=="":
    nome="sem nome"
input("Todo final de semana você sai com os seus amigos da faculdade para beber. ") 
input("A população local não vê seu grupo com bons olhos devido a problemas envolvendo a polícia. ")
input("Enquanto vocês bebiam, seu amigo Tomás lhe faz uma pergunta:")
print("- E aí ",nome,", vai fazer o quê esse final de semana?")
print("Para fazer a sua escolha, você deve digitar o número referente a resposta que você optar. ")
input("Aperte Enter para continuar. ")
print("O que você vai fazer no final de semana?")
print("1- Vou estudar para a prova de segunda.")
print("2- Vou virar a noite jogando fogaréu gratuito.")
e1=input("Escolha uma opção: ")
while e1!="1" and e1!="2":
    print("A sua escolha é inválida. Tente novamente.")
    print("1- Vou estudar para a prova de segunda.")
    print("2- Vou virar a noite jogando fogaréu gratuito.")
    e1=input("O que você vai fazer no final de semana? ")
print("-Que porcaria de plano.")
print("-A gente tinha que fazer ele pixar o muro da igreja")
print("-Pois é, geral aqui do grupo já pixou o muro da igreja menos ele.")
input("-Então é isso, esse Zé Ruela vai pixar o muro assim que a gente acabar de beber. ")
input("Você aceita o desafio, pois queria se entrosar melhor com o grupo. ")
input("Assim que vocês saem do bar, vão direto para a igreja.")
input("Quando vocês chegam lá, seu amigo Tomás pega uma lata de tinta da mala e pergunta:")
print("Coé menor, vai pixar mesmo ou já arregou?")
print("1- Quem cê ta chamando de arregão? Vou pixar essa parede é agora!")
print("2- Sim, vou arregar, adeus.")
e2=input("Escolha uma opção: ")
while e2!="1" and e2!="2":
    print("A sua escolha é inválida. Tente novamente.")
    print("1- Quem cê ta chamando de arregão? Vou pixar essa parede é agora!")
    print("2- Sim, vou arregar, adeus.")
    e2=input("Coé menor, vai pixar mesmo ou já arregou?")
if e2=="1":
    input("Você está relutante em pixar o muro, mas fica com medo do que podem falar de você caso não o faça.")
    input("Assim que você pixa o muro, você ouve uma voz grossa e irada de dentro da igreja:")
    input("-O QUE VOCÊS ESTÃO FAZENDO COM A CASA DE DEUS?!?! SEUS VÂNDALOS MALDITOS!! EU JURO QUE MATO VOCÊS UM DIA!!!")
    input("Você e seus amigos ficam assustados e correm o mais rápido que podem. Assim que você se acalma, percebe que você se separou de seus amigos e decide voltar para sua casa.")
    #Igreja
    print("PV = 100")
    print("No dia seguinte, você acorda com uma sensação estranha, como se estivesse deitado em um chão de concreto. ")
    input("Porque você estava. Assim que você se levanta, percebe que não está em casa.")
    input("Você olha os arredores, parece estar em um quarto velho e mal cuidado. A porta está aberta. ")
    print("O que você faz? ")
    print("1-Vasculhar o quarto. ")
    print("2-Sair do Quarto. ")
    e3=input("Escolha uma das opções dadas: ")
    while e3!="1" and e3!="2":
        print("A sua escolha é inválida. Tente novamente. ")
        print("1-Vasculhar o quarto. ")
        print("2-Sair do Quarto. ")
        e3=input("O que você faz? ")
    if e3=="1":
        input("Você não encontra nada muito chamativo no quarto, apenas uma chave e uma lanterna. Você pega os dois e decide sair do quarto.")
        CV=1
        FL=1
    else:
        input("Assustado com a sua situação, você decide sair do quarto o mais rápido possível. ")
    input("Você sai do quarto em um grande e escuro corredor, tão mal cuidado quanto o quarto. ")
    input("Do lado direito do corredor havia uma porta. ")
    #O Vulto
    input("De repente você avista de relance um vulto entrando em uma porta, e fica sem reação. ")
    print("Após se recuperar do choque, o que você faz? ")
    print("1-Tenta chamar a atenção do vulto. ")
    print("2-Ignora o vulto e segue em frente. ")
    print("3-Entra pela porta e vai atrás do vulto discretamente. ")
    e4=input("Escolha uma das opções dadas: ")
    while e4!="1" and e4!="2" and e4!="3":
        print("A sua escolha é inválida. Tente novamente. ")
        print("1-Tenta chamar a atenção do vulto. ")
        print("2-Ignora o vulto e segue em frente. ")
        print("3-Entra pela porta e vai atrás do vulto discretamente. ")
        e4=input("O que você faz? ")
    if e4=="1":
        input("Tentar chamar a atenção do vulto não foi uma boa ideia, você morreu. ")
        print("Final #02: Não confie em vultos. ")
        PV=PV*0
        PF=PV+FL*25+AE*25+HW*25+CV*25
        print("Pontuação final = ", PF)
        print("Game Over")
        input("Aperte Enter para sair do programa")
        sys.exit(input("Aperte Enter para sair do programa"))
    if e4=="2":
        print("Você passa cuidadosamente pelo corredor para não chamar a atenção do homem, e ele parece não te perceber. ")
    if e4=="3":
        input("Cuidadosamente, você segue o vulto para tentar descobrir o que ele é. ")
        input("Você vê uma figura que se parece um homem muito magro de costas, a figura está segurando uma adaga ensanguentada. ")
        if CV==0:
            input("Não demorou muito para o homem perceber você atrás dele, ele te persegue pelo corredor, até que você escorrega em uma casca de banana. ")
            input("O homem começa a cascar o bico com a sua desgraça, enquanto entope seu peito de facadas.")
            print("Final #03: Podia ser pior (eu acho).")
            PV=PV*0
            PF=PV+FL*25+AE*25+HW*25+CV*25
            print("Pontuação final = ", PF)
            print("Game Over")
            input("Aperte Enter para sair do programa")
            sys.exit(input("Aperte Enter para sair do programa"))
        if CV==1:
            input("Em uma tentativa de se livrar desse perigo de uma vez, você tenta trancar a porta com a chave que você achou no quarto. ")
            input("Porém, o homem percebe e dispara em sua direção, tentando esfaqueá-lo. ")
            print("Ele consegue te acertar um golpe, mas, com muita sorte, você consegue fechar a porta no braço dele,")
            input("deixando sua adaga cair")
            print("Você quer pegar a adaga ensanguentada?")
            print("1-Sim.")
            print("2-Não.")
            e5=input("Escolha uma das opções: ")
            while e5!="1" and e5!="2":
                print("A sua escolha é inválida. Tente novamente. ")
                print("1-Sim.")
                print("2-Não.")
                e5=input("Você pega a adaga?")
            if e5=="1":
                print("Você decide pegar a adaga. ")
                AE=1
            if e5=="2":
                print("Você decide não levar a adaga consigo. ")
            PV=PV-25
            print("PV=",PV)
            print("O homem começa a bater na porta e a gritar: ")
            input("-A ÁGUA SAGRADA QUEIMA, QUEIMAAAAAAAA!!! ")
            input("Você, assustado com a loucura e agressividade do homem, decide seguir em frente. ")
    #Corredor Principal
    input("Seguindo até o final do corredor, você sai em uma sala com um altar enorme, que dá acesso à dois outros corredores. ")
    print("Após uma rápida análise dos dois corredores, você decide investigar um deles, qual caminho você percorrerá? ")
    print("1- O primeiro caminho, um corredor iluminado por velas e com algumas teias de aranha. ")
    print("2- O segundo caminho, um corredor sujo e mal iluminado, com uma vidraça no final dele. ")
    e6=input("Escolha uma das opções dadas: ")
    while e6!="1" and e6!="2":
        print("A sua escolha é inválida. Tente novamente. ")
        print("1- O primeiro caminho, um corredor iluminado por velas e com algumas teias de aranha. ")
        print("2- O segundo caminho, um corredor sujo e mal iluminado, com uma vidraça no final dele. ")
        e6=input("O que você faz? ")
    #Corredor 1
    if e6=="1":
        input("Você segue pelo longo corredor das velas e encontra no final dele um altar com um pequeno frasco ornamentado com um líquido misterioso. ")
        print("Você pega o frasco ou não? ")
        print("1-Sim, eu pego o frasco. ")
        print("2-Não, eu deixo o frasco no lugar. ")
        e7=input("O que você faz? ")
        while e7!="1" and e7!="2":
            print("A sua escolha é inválida. Tente novamente. ")
            print("1-Sim, eu pego o frasco. ")
            print("2-Não, eu deixo o frasco no lugar. ")
            e7=input("Você pega o frasco ou não? ")
        if e7=="1":
            print("Você decide pegar o frasco. ")
    #O Gordo        
            input("Assim que você pega o frasco, é agarrado pelo ombro e jogado contra a parede. ")
            PV=PV-20
            print("PV=",PV)
            input("Você se recupera do golpe e identifica o agressor: ")
            input("Um homem extremamente grande e gordo, olhando fixamente para você. ")
            if AE==1:
                input("Você pega a adaga ensanguentada e rapidamente golpeia ele, que depois de levar uma forte facada, começa a grunhir de dor e desmaia. ")
                input("Aterrorizado com o que ouve, você grita de desespero sai correndo ")
                HW=1
            if AE==0:
                input("Sem muitas opções para revidar, você joga o frasco nele, estourando o frasco e espalhando o líquido misterioso. ")
                input("O gordo, atordoado, esbarra numa das velas. ")
                input("Assim que ele encosta na vela, seu corpo rapidamente começa a pegar fogo. ")
                input("Em chamas, ele começa a agonizar e cai no chão. ")
                input("Desesperado, o gordo se agarra em sua perna, fazendo com que você se queimasse também. ")
                input("Você chuta a cabeça dele e aproveita a oportunidade para fugir da terrível cena que acabou de presenciar. ")
                PV=PV-20
                print("PV=",PV)
            input("Você se esconde desesperado em uma sala do corredor. ")
            input("O peso de ter matado uma pessoa começa a te atingir, mas você sabe que não pode parar agora. ")
        if e7=="2":
            input("O frasco não parece ter utilidade alguma em sua fuga, então você o deixa no lugar e entra na sala ao seu lado. ")
    #O Musculoso 
        input("Você começa então a observar a sala em que se encontra. ")
        input("De todos os lugares que você presenciou, este é o pior de todos. ")
        input("Para qualquer lado que você olha tem diversos equipamentos de tortura, que você tenta ignorar. ")
        input("No extremo oposto da sala, há uma outra porta, aparentemente trancada. ")
        input("Porém, de repente, a porta é golpeada pelo outro lado, quebrando-a em pedaços. ")
        input("Entra no quarto então um homem musculoso, gigante e com seu rosto desfigurado. Ele anda lentamente em sua direção. ")
        if HW==1:
            input("Você tenta atacar o homem com a adaga, mas ele pega a lámina da mesma e a amassa sem nenhum esforço. ")
            input("O homem então te da um socão, fazendo você voar para fora do quarto. ")
            input("Em um ato desesperado, você joga o frasco na cara dele. ")
            input("O frasco quebra na cara do robusto homem, deixando-o atordoado. ")
            input("Considerando o que o lunático disse antes, você pega uma vela e joga no gigante, fazendo-o explodir em chamas. ")
            input("Você aproveita a chance para atravessar o quarto em um outro corredor. ")
        if HW==0:
            print("Enfrentar o Musculoso na raça? ")
            input("Grande erro. O musculoso pega você pela perna e te joga em uma parede. ")
            input("Contudo, o impacto faz com que o teto rache acima do Musculoso, quebrando em pedaços e rachando a cabeça dele. ")
            print("A porrada foi muito forte, e como você ignorou um item a mostra dentro de um RPG, ") 
            print("você vai tomar 75 de dano pra largar de ser otário. ")
            input("(é pegadinha professora, nós lhe admiramos e espero que essa brincadeira não influencie em nossa nota. Desde já agradecemos sua atenção.) ")
            PV=PV-75
            print("PV = ",PV)
            input("Você então segue para a próxima sala, que se parece com mais um corredor. ")
    #Corredor 2 - Marimbondos
    if e6=="2":
        input("Você segue pelo longo corredor sujo e mal iluminado, ele está repleto de teias de aranha, dificultando sua passagem. ")
        input("Até o estado do chão dificultava sua passagem, pois estava coberto de sangue. ")
        input("Um cheiro de ferro domina o lugar, você tem um péssimo pressentimento, mas você continua mesmo assim. ")
        input("Você percebe este corredor esta impregnado por marimbondos, indo em alta velocidade em sua direção. ")
        print("Sem muito tempo para pensar, você tem que rapidamente decidir o que fazer. ")
    #Com a lanterna
        if FL==1:
            print("1-Sair correndo no meio dos marimbondos. ")
            print("2-Utilizar a lanterna.")
            e7=input("O que você faz? ")
            while e7!="1" and e7!="2":
                print("A sua escolha é inválida. Tente novamente. ")
                print("1-Sair correndo no meio dos marimbondos")
                print("2-Utilizar a lanterna.")
                input("O que você faz? ") 
            if e7=="1":
                input("Você avança pelo corredor desesperadamente tentando não ser atingido pelos insetos voando atrás de você. ")
                PV=PV-75
                print("PV=",PV)
                input("Você chega ao final do corredor cheio de ferimentos. ")
           
            if e7=="2":
                input("Após analisar a situação, você liga a lanterna e aponta nos marimbondos.")
                input("Surpreendentemente, os marimbondos se afastam à medida que você aponta um feixe de luz.")
                input("Você escapa do enxame sem nenhum arranhão e chega até o final do corredor.")
    #Sem a lanterna
        if FL==0:
            print("1-Sair correndo no meio dos marimbondos. ")
            print("2-Ficar parado")
            e7=input("O que você faz? ")
            while e7!="1" and e7!="2":
                print("A sua escolha é inválida. Tente novamente. ")
                print("1-Sair correndo no meio dos marimbondos. ")
                print("2-Ficar parado")
                e7=input("O que você faz? ")
            if e7=="1":
                input("Você avança pelo corredor desesperadamente tentando não ser atingido pelos insetos voando atrás de você. ")
                PV=PV-75
                print("PV=",PV)
                input("Você chega ao final do corredor cheio de ferimentos. ")
            if e7=="2":
                input("Achando ser uma boa ideia, você decide ficar parado.")        
                input("Infelizmente você estava errado e você acaba sendo picado até a morte. ")
                PV=PV*0
                print("Final #05: TOMA PICADA E TOMA PICADA E TOMA PICADA FATAL ")
                PF=PV+FL*25+AE*25+HW*25+CV*25
                print("Pontuação final = ", PF)
                print("Game Over")
                input("Aperte Enter para sair do programa")
                sys.exit(input("Aperte Enter para sair do programa"))
    #Final Principal
    
    input("No final do corredor você avista um pequeno altar com uma alavanca. ")
    input("Observando a alavanca a sua frente, você percebe que não tem mais saídas daquela sala, então você decide puxá-la. ")
    input("Ao puxar a alavanca você escuta um barulho vindo da sala do altar e decide voltar para investigar")
    input("Ao chegar lá você descobre uma nova passagem.")
    if PV>0:
        input("Avançando nessa passagem, você avista uma silhueta e tem a impressão de que conhece o ser por trás desta.")
        print("Tomás: -Olá ",nome," parabéns por não arregar. ")
        input("Tomás: -Para ser honesto, não esperava que fosse realmente pixar aquela parede. ")
        input("Tomás: -Mas também, não esperava que fosse sobreviver até aqui")
        input("Tomás: -Afinal, nenhum de nossos amigos chegou tão longe.")
        input("Tomás: -Admito que estou feliz que sou eu quem vai poder acabar com você.")
        input("- TOMÁS??!! Então era você por trás disso o tempo todo?!?!")
        input("- Mas e aquela voz? Aquela que gritou conosco e nos ameaçou de morte. ")
        input("Tomás: -Aquela voz que nos jurou vingança ontem? Meu pai.")
        input("Tomás: -Você não entende? Tudo isso, a morte de todos nossos amigos, SUA MORTE, tudo estava planajado desde o inicio. ")
        input("- Não acredito que confiei em você, maldito. ")
        input("Você começa a se aproximar de Tomás. ")
        input("Tomás: -Oh? Você está se aproximando de mim? ")
        input("Tomás: -Ao invés de fugir, você está vindo diretamente em minha direção?! ")
        input("- Seu Zé Ruela, eu não posso te encher de porrada sem me aproximar. ")
        input("Tomás: -OH HO!! Então aproxime-se o quanto quiser. ")
        input("Tomás e você começam a luta do século, porrada para todo lado. ")
        input("Tomado por um surto de adrenalina, você parte pra cima de Tomás, desferindo uma sequência de socos. ")  
        input("Em desvantagem, Tomás consegue lhe dar uma cabeçada, escapando de seus golpes. ")
        input("Vendo que brigar desse jeito não levaria a nada, Tomás lhe faz uma proposta inusitada. ")
        input("Tomás: -Chega disso! Já passou da hora de decidirmos isso que nem homens! ")
        input("-Você está falando de...?! ")
        print("Tomás: -É isso mesmo que você está pensando, ",nome,"... ")
        input("BATALHA DE RAP ")
        input("Tomás então começa a rimar: ")
        print("Tomás: -Salve rapaziada, não vim aqui para perder, esse babaca na minha frente daqui a pouco vai morrer. ")
        input("Tomás: -Tá achando que vai escapar sem nenhum problema, mas sou que vou ferrar com todo o seu esquema. ")
        input("Você então devolve com a rima mais braba possível: ")
        print("Morrer não vou nada, o pai aqui é blindado, quem tentar me matar hoje vou ficar chateado. ")
        input("Se tentar me matar, é tentativa sem sucesso, encosta em mim de novo que você ganha processo. ")
        input("A rima aqui é braba, a batalha tá uma delícia, enquanto rolava essa treta eu chamei a polícia. ")
        input("A polícia então chega na igreja e prende Tomás por sequestro e ameaça. ")
        input("Enquanto Tomás era levado à viatura, sua curiosidade o levou a perguntar: ")
        input("Tomás: -Como você chamou a polícia?")
        print("-Tá louco, você nem pegou meu celular, eu liguei pra polícia assim que acordei. ") 
        input("-Só que a polícia demorou até agora pra mandar uma viatura. ")
        input("Tomás: -... ")
        input("Tomás: -Entendo. ")
        input("Assim que você teve sua última conversa com seu velho amigo Tomás, ele é levado pela polícia e você finalmente pôde voltar para casa.")
        input("Chegando em casa, seu pai te deixa de castigo por pixar a uma igreja, seu delinquente.")
        print("Final #05: O mundo gira e vacilão roda.")
    if PV<=0:
        input("Avançando nessa passagem, você avista uma silhueta e tem a impressão de que conhece o ser por trás desta.")
        print("Mas antes de poder continuar, sua visão vai lentamente ficando escura")
        input("Antes de cair no chão você escuta uma última coisa: ")
        print("Que pena ",nome,", chegou mais longe do que pensei que chegaria, mas ainda assim, perdeu no final.")
        input("Essa voz era familiar, mas você não teve tempo de distingui-la, pois acabou desmaiando")
        input("Infelizmente, todos os ferimentos que levou até agora fez com que seu corpo não te aguente mais")
        input("Você acorda com o som das sirenes")
        input("Tomás: -Aqui está ele! Ele que matou os meus amigos!")
        input("Você é levado para a viatura sem entender o que esta havendo, enquanto Tomás lhe rogava pragas pelos amigos mortos. ")
        print("Final #06: Psé man, vai ver o Sol nascer quadrado. ")
else:
    input("Você se sente incomodado pela ideia de vandalizar a igreja e vai embora. Aperte Enter para continuar")
    input("No dia seguinte, você ouve a notícia de que seus amigos estão desaparecidos.")
    print("Final #01: Parece que você se safou dessa vez, arregão.")
PF=PV+FL*25+HW*25+CV*25+AE*25
if PF>=50 and PF<80:
    print("Jogou bem, mas poderia melhorar. ")
    print("Pontuação final = ", PF)
elif PF<50:
    input("Parabéns, foi ó")
    print("uma bosta. ")
    print("Pontuação final = ", PF)
elif PF>80 and PF<150:
    print("Boa",nome, "jogou até que bem.")
    print("Pontuação final = ", PF)
elif PF>=150:
    print("Bom trabalho, jogou o fino do fino. ")
    print("Pontuação final = ", PF)
input("Créditos: Guilherme Chiarelli, Guilherme Valente e Rafael Pezeiro.")
print("Obrigado por Jogar! | Thanks for Playing! | Gracias por Jugar! ")
print("Game Over")
