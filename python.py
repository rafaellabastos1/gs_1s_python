def Tratamentos():
      spodovir = ''
      engeoPlenoS = ''
      bacillus = ''
      aug = ''

def Plantacao():
      algodao = ''
      arroz = ''
      aveia = ''
      cafe = ''
      cana = ''
      feijao = ''
      girassol = ''
      milho = ''
      milhoSafrinha = ''
      soja = ''
      trigo = ''


def Pragas():
      cigarrinhaMilho = ''
      cupimMonticulo = ''
      lagartaCartucho = ''
      lagartaHelicoverpa = ''
      percevejoMarrom = ''
      percevejoVerdePeq = ''
      percevejoSoja = ''
      percevejoArroz = ''
      percevejoBarrigaVerde = ''
      phyllophaga = ''
      pulgao = ''
      pulgaoAlgodoeiro = ''
      tripes = ''
      vaquinhaVerdeAmarela = ''


#menu
opcaoMenu = 0
print('Seja bem vindo à PlanTech! No que podemos te ajudar?'
      '\n'
      '\n1. Desejo saber mais sobre a missão da PlanTech' #Luiz
      '\n2. Desejo saber sobre o funcionamento do drone' #Igor
      '\n3. Quero comprar um drone para detectar pragas' #Luiz
      '\n4. Identifiquei uma praga na plantação. O que faço agora?' #Rafa
      '\n5. Quem faz parte do projeto PlanTech?' #Douglas
      '\n6. Quero indicar um tratamento para uma praga' #Gustavo
      '\n7. Feedback' #Douglas
      '\n8. Outro') #Rafa
opcaoMenu = int(input('Selecione uma das opções acima: '))

match opcaoMenu:
#Opção 1 do menu: desejo saber mais sobre a missão da PlanTech ---- Colocar o primeiro e o último parágrafo do
#   arquivo "Descrição geral da solução 2"
      case 1:
            print("-")

#Opção 2 do menu: desejo saber sobre o funcionamenento do drone ---- Colocar o segundo parágrafo do arquivo
#   "Descrição geral da solução 2"
      case 2:
            print("-")

#Opção 3 do menu: quero comprar um drone para detectar pragas ---- 1º: Falar que a PlanTech ainda é um projeto e, por 
#   isso, ainda não foi desenvolvido drones para a venda; Perguntar se o usuário deseja fazer uma simulação de como
#   seria essa etapa. Se não: dizer obrigada e retornar ao menu; 
#   Se sim 2º: fazer cadastro do cliente com os dados (nome completo, RG ou CNH, CPF ou CNPJ, e-mail, telefone, rua,
#   número de residência, se precisar de complemento, país, estado, cidade, bairro, CEP); Sistema deve validar todos
#   esses dados. 
#   3º: mostrar os dados informados pelo cliente e perguntar se eles estão corretos; 
#   4º: perguntar quantos drones o usuário deseja comprar; 
#   5º: dizer obrigada e que x drones serão entregues em até 15 dias no endereço mencionado; fazer uma observação 
#   para dizer também que, como foi dito, este era apenas um teste e que, por isso, não foi pedido dados de
#   pagamento e nem os drones serão entregues de fato ao endereço mencionado.
      case 3:
            print("-")

#Opção 4 do menu: identifiquei uma praga na plantação. O que faço agora? ---- Fazer um sistema com x tratamentos 
#   para pragas e x tratamentos que x plantações pode receber. A partir disso, fazer todas as combinações possíveis 
#   em comum. O usuário deve ter a opção de digitar o nome da praga e o nome da plantação atacada; Se colocar uma
#   praga ou plantação que não tenha no sistema, dizer que ainda não há esse no sistema
      case 4:
            print("-")


#Opção 5 do menu: quem faz parte do projeto PlanTech? ---- Colocar o nome e RM de todos do grupo
      case 5:
            print("\nTodas as pessoas responsáveis pelo projeto PlanTech são: \nDouglas Magalhães de Araujo - rm552008 \nGustavo Arguello Bertacci - rm551304 \nIgor Ribeiro Anccilotto - rm550415 \nLuiz Fillipe Farias - rm99519 \nRafaella Monique do Carmo Bastos - rm552425")


#Opção 6 do menu: quero indicar o tratamento para uma praga ---- Deixar com que o usuário informe o nome de uma 
#   praga, o tipo de plantação que essa praga ataca e o tipo de tratamento que essa praga combinada com essa 
#   plantação pode receber; Mostrar uma mensagem agradecendo e dizendo que essas informações vão para análise e
#   se estiver tudo correto, serão incluídas no sistema PlanTech
      case 6:
            print("-")




#Opção 7 do menu: feedback ---- o usuário pode dar um feedback sobre a resolução de suas dúvidas, da performace do
#   sistema, sobre a indicação dos tratamentos para as plantações, sobre a usabilidade do projeto e experiência com 
#   o site
      case 7:
            #menu que pergunta para o usuário a escolha do feedback.
            feedback = int(input("\nPrimeiro, informe o tipo do feedback: \n(1) - Resolução de suas dúvidas \n(2) - Performace do sistema \n(3) - Indicação dos tratamentos para as plantações \n(4) - Usabilidade do projeto \n(5) - Experiência com o site"))
            #se o usuário digitar um número maior ou menor, aparece uma mensagem de erro.
            if feedback < 1 or feedback > 5:
                  print("Escolha incorreta! Escolha um número de 1 a 5.")
            #o usuário digita a nota do feedback de 0 até 10, e depois escreve uma observação.
            elif feedback == 1:
                  notaFeedback = int(input("Digite a nota que desejar (0-10)"))
                  #se o usuário digitar um número maior ou menor, aparece uma mensagem de erro.
                  if notaFeedback < 0 or notaFeedback > 10:
                        print("Os números permitidos são apenas de 0 a 10!")
                  else:
                        reclamacao = input("Escreva sua reclamação, ou, aperte ENTER para enviar")
                        print(f"A PlanTech agradece pelo seu feedback!")
            elif feedback == 2:
                  notaFeedback = int(input("Digite a nota que desejar (0-10)"))
                  if notaFeedback < 0 or notaFeedback > 10:
                        print("Os números permitidos são apenas de 0 a 10!")
                  else:
                        reclamacao = input("Escreva sua reclamação, ou, aperte ENTER para enviar")
                        print(f"A PlanTech agradece pelo seu feedback!")
            elif feedback == 3:
                  notaFeedback = int(input("Digite a nota que desejar (0-10)"))
                  if notaFeedback < 0 or notaFeedback > 10:
                        print("Os números permitidos são apenas de 0 a 10!")
                  else:
                        reclamacao = input("Escreva sua reclamação, ou, aperte ENTER para enviar")
                        print(f"A PlanTech agradece pelo seu feedback!")
            elif feedback == 4:
                  notaFeedback = int(input("Digite a nota que desejar (0-10)"))
                  if notaFeedback < 0 or notaFeedback > 10:
                        print("Os números permitidos são apenas de 0 a 10!")
                  else:
                        reclamacao = input("Escreva sua reclamação, ou, aperte ENTER para enviar")
                        print(f"A PlanTech agradece pelo seu feedback!")
            elif feedback == 5:
                  notaFeedback = int(input("Digite a nota que desejar (0-10)"))
                  if notaFeedback < 0 or notaFeedback > 10:
                        print("Os números permitidos são apenas de 0 a 10!")
                  else:
                        reclamacao = input("Escreva sua reclamação, ou, aperte ENTER para enviar")
                        print(f"A PlanTech agradece pelo seu feedback!")


#Opção 8 do menu: outro ---- Colocar pequenas informações e onde pode encontrá-las: se quer tirar dúvidas mais
#   específicas, entrar no nosso ChatBot; Se quer textos mais explicativos como agricultura sustentável, uso de
#   IA's generativas na produção, distribuição de alimentos pelo mundo, modelos de cultivos eficientes e calendário
#   de controle de pragas, entrar no site da PlanTech.
      case 8:
            print("-")