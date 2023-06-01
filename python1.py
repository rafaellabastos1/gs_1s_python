#Função que compara cada tipo de plantação com cada praga e retorna o tratamento mais adequado para a situação
def Indicacao():
      spodovir = ('\nTratamento para a sua plantação: Spodovir'
                  '\n1. É um biodefensivo e inseticida microbiológico'
                  '\n2. Deve ser utilizado assim que a praga for identificada ou de 10 a 22 dias após a germinação das plantações'
                  '\n3. É recomendado pulverizar o produto sobre a cultura com a utilização do volume da calda de 150 litros do produto por hectare se for por via terrestre ou 50 litros do produto por hectare se for por via aérea'
                  '\n4. Uma dose pode ser diluída em 1 litro de água'
                  '\n5. Para informações de como fazer, precauções e mais, leia a bula que vem junto ao produto no momento da compra.')
      
      engeoPlenoS = ('\nTratamento para a sua platação: Engeo Pleno S'
                     '\n1. Para informações de como fazer, precauções e mais, leia a bula que vem junto ao produto no momento da compra.') 
      
      bacillus = ('\nTratamento para a sua plantação: Bacillus Thuringienses'
                  '\n1. É um inseticida biológico'
                  '\n2. Inseticida biológico com a recomendação de pulverização sobre a cultura com a utilização de 500 a 750 gramas por hectare, sendo a utilização do volume da calda de 200 litros por hectare'
                  '\n3. Para informações de como fazer, precauções e mais, leia a bula que vem junto ao produto no momento da compra.')
      
      aug = ('\nTratamento para a sua plantação: AUG 106'
             '\n1. É um inseticida de suspensão concentrada'
             '\n2. Para informações de como fazer, precauções e mais, leia a bula que vem junto ao produto no momento da compra.')
      
      nomePlanta = input('\nQual o nome da plantação atacada? ')
      nomePraga = input('Qual o nome da praga? ')

     
      
     

#Cadastro

def Cadastro():
      confirmCadastroup = ""
      print("\nPor favor realize o cadastro: ")
      while confirmCadastroup != "1" and confirmCadastroup != "SIM":
            opcIdentup = ""
            opcIdent2up = ""
            opcComplementoup = ""
            confirmCadastroup = ""
            rg = ""
            telefone = ""
            cep = ""
            cnh = ''
            NomeCompleto = ""
            email = ""
            rua = ""
            nmrResidencia = ""
            pais = ""
            estado = ""
            cidade = ""
            bairro = ""
            while NomeCompleto == "":
                  NomeCompleto = input("\nDigite seu nome: ")
            while opcIdentup != "1" and opcIdentup != "RG" and opcIdentup != "2" and opcIdentup != "CNH":
                  opcIdent = input("\n(1) - RG \n(2) - CNH \nEscolha qual você deseja informar: ")
                  opcIdentup = opcIdent.upper()
                  if opcIdentup == "1" or opcIdentup == "RG":
                        while len(rg) != 9:      
                              rg = input("\nRG: ")
                              if  len(rg) != 9:
                                    print("RG inválido! Digite apenas números.")
                        
                        #print("Digite apenas números!")
                  elif opcIdentup == "2" or opcIdentup == "CNH":
                        while len(cnh) != 10:
                              cnh = input("\nCNH: ")
                              if len(cnh) != 10:
                                    print("Digite um CNH válido. Não utilize indicadores.")
            while opcIdent2up != "1" and opcIdent2up != "CPF" and opcIdent2up and "2" and opcIdent2up != "CNPJ":
                  opcIdent2 = input("\n(1) - CPF \n(2) - CNPJ \nEscolha qual você deseja informar: ")
                  opcIdent2up = opcIdent2.upper()
                  if opcIdent2up == "1" or opcIdent2up == "CPF":
                        while len(cpf) != 11:
                              cpf = input("\nCPF: ")
                              if len(cpf) != 11:
                                    print("Digite um CPF válido. Utilize apenas números.")
                  elif opcIdent2up == "2" or opcIdent2up == "CNPJ":
                        while len(cnpj) != 14:
                              cnpj = input("\nCNPJ: ")
                              if len(cnpj) != 14:
                                    print("Digite um CNPJ válido. Não utilize indicadores.")
            while email == "": 
                  email = input("\nE-mail: ")
            while len(telefone) != 14:
                  telefone = input("\nTelefone: ")
                  if len(telefone) != 14:
                        print("Digite um telefone válido. Ex(+5511999999999).")
            while rua == "":
                  rua = input("\nRua: ")
            while nmrResidencia == "":
                  nmrResidencia = input("\nNúmero de Residência: ")
            while opcComplementoup != "1" and opcComplementoup != "SIM" and opcComplementoup != "2" and opcComplementoup != "NAO" and opcComplementoup != "NÃO":
                  opcComplemento = input("\n(1) - Sim \n(2) - Não \nDeseja informar um complemento?: ")
                  opcComplementoup = opcComplemento.upper()
                  if opcComplementoup == "1" or opcComplementoup == "SIM":
                        complemento = input("\nComplemento: ")
                  elif opcComplementoup == "2" or opcComplementoup == "NAO" or opcComplementoup == "NÃO":
                        print("")
            while pais == "":
                  pais = input("\nPaís: ")
            while estado == "":
                  estado = input("\nEstado: ")
            while cidade == "":
                  cidade = input("\nCidade: ")
            while bairro == "":
                  bairro = input("\nBairro: ")
            while len(cep) !=8:
                  cep = input("\nCEP: ")
                  if len(cep) != 8:
                        print("Digite um CEP válido. Use apenas números.")
            print("\nConfirme as informações: ")
            while confirmCadastroup != "1" and confirmCadastroup != "SIM" and confirmCadastroup != "2" and confirmCadastroup != "NAO" and confirmCadastroup != "NÃO" :
            
                  print("\n--- Dados Pessoais ---")
                  print(f"Nome:  {NomeCompleto}")
                  if opcIdentup == "1" or opcIdentup == "RG":
                        print(f"RG: {rg}")
                  if opcIdentup == "2" or opcIdentup == "CNH":
                        print(f"CNH: {cnh}")
                  if opcIdent2up == "1" or opcIdent2up == "CPF":
                        print(f"CPF: {cpf}")
                  if opcIdent2up == "2" or opcIdent2up == "CNPJ":
                        print(f"CNPJ: {cnpj}")
                  print(f"E-mail: {email}")
                  print(f"Telefone: {telefone}")
                  print("\n--- Endereço ---")
                  print(f"Rua: {rua}")
                  print(f"Número de Residência: {nmrResidencia}")
                  if opcComplementoup == "1" or opcComplementoup == "SIM":
                        print(f"Complemento: {complemento}")
                  print(f"País: {pais}")
                  print(f"Estado: {estado}")
                  print(f"Cidade: {cidade}")
                  print(f"Bairro: {bairro}")
                  print(f"CEP: {cep}")
                  confirmCadastro = input("\n(1) - Sim \n(2) - Não \nOs dados estão corretos? \nEscolha uma opção: ")
                  confirmCadastroup = confirmCadastro.upper()
                  if confirmCadastroup == "1" or confirmCadastroup == "SIM": 
                        print("Concluímos seu cadastro!")
                  elif confirmCadastroup == "2" or confirmCadastroup == "NAO" or confirmCadastroup == "NÃO":
                        print("Faça novamente o cadastro!")
      qntdDrone = int(input("\nQuantos drones você deseja comprar? \nDrones: "))
      if qntdDrone > 0 and qntdDrone < 999:
            print(f"Obrigado pela compra! Seus {qntdDrone} drones chegaram em até 15 dias úteis.")
            print("Lembramos que foi apenas uma simulação, a PlanTech está em desenvolvimento portanto os drones não serão enviados.")
      else:
            print("O limite de drones é de 1 a 999.")

#menu
opcaoMenu = 2
while opcaoMenu != 9:
      print('\nSeja bem vindo à PlanTech! No que podemos te ajudar?'
            '\n'
            '\n1. Desejo saber mais sobre a missão da PlanTech' #Luiz
            '\n2. Desejo saber sobre o funcionamento do drone' #Igor
            '\n3. Quero comprar um drone para detectar pragas' #Luiz
            '\n4. Identifiquei uma praga na plantação. O que faço agora?'
            '\n5. Quem faz parte do projeto PlanTech?' #Douglas
            '\n6. Quero indicar um tratamento para uma praga' #Gustavo
            '\n7. Feedback' #Douglas
            '\n8. Outro'
            '\n9. Encerrar')
      opcaoMenu = int(input('Selecione uma das opções acima: '))



#Opção 2 do menu: desejo saber sobre o funcionamenento do drone ---- Colocar o segundo parágrafo do arquivo
#   "Descrição geral da solução 2"
      if opcaoMenu == 2:
            print("\n----PlanTech ----"
                        +"\n Para isso, será desenvolvido um drone robô  drone robô que detecta pragas nas plantações e informa suas localidades para o combate."
                        +"Essa detecção é por meio de uma IA generativa que identifica as pragas nas plantações com infravermelho ainda na fase inicial e informa ao dono da plantação o nome da praga e o seu local no visor do drone."
                        +"Com essa informação, o dono da plantação entra no sistema da PlanTech e informa o nome da praga e qual plantação ela está atacando para que, dessa forma, seja indicado um tratamento saudável e sustentável para que aquela plantação não seja perdida, danificada e nem tenha alastramento das pragas."
                        +"Com essa informação, o dono da plantação entra no sistema da PlanTech e informa o nome da praga e qual plantação ela está atacando para que, dessa forma, seja indicado um tratamento saudável e sustentável para que aquela plantação não seja perdida, danificada e nem tenha alastramento das pragas. "
                        +"Este drone funciona sozinho e é recarregável, sendo necessário somente ligar ele para que ele sobrevoe a plantação em busca de possíveis pragas."
                        +"O usuário pode também entrar em contato com o nosso ChatBot para solucionar possíveis dúvidas, dar seu feedback e entrar no site da PlanTech para mais informações sobre agricultura ou semelhantes. "
                        +"Além disso, o agricultor pode contribuir com informações de pragas e tratamentos que não tenham no site.")








#Opção 5 do menu: quem faz parte do projeto PlanTech? ---- Colocar o nome e RM de todos do grupo
      if opcaoMenu == 5:
            print("\nTodas as pessoas responsáveis pelo projeto PlanTech são: \nDouglas Magalhães de Araujo - rm552008 \nGustavo Arguello Bertacci - rm551304 \nIgor Ribeiro Anccilotto - rm550415 \nLuiz Fillipe Farias - rm99519 \nRafaella Monique do Carmo Bastos - rm552425")



#Opção 7 do menu: feedback ---- o usuário pode dar um feedback sobre a resolução de suas dúvidas, da performace do
#   sistema, sobre a indicação dos tratamentos para as plantações, sobre a usabilidade do projeto e experiência com 
#   o site
      if opcaoMenu == 7:
            #menu que pergunta para o usuário a escolha do feedback.
            feedback = int(input("\nPrimeiro, informe o tipo do feedback: \n(1) - Resolução de suas dúvidas \n(2) - Performace do sistema \n(3) - Indicação dos tratamentos para as plantações \n(4) - Usabilidade do projeto \n(5) - Experiência com o site"))
            #se o usuário digitar um número maior ou menor, aparece uma mensagem de erro.
            if feedback < 1 or feedback > 5:
                  print("Escolha incorreta! Escolha um número de 1 a 5.")
            
            #O usuário digita a nota do feedback de 0 até 10, e depois escreve uma observação.
            elif feedback == 1:
                  notaFeedback = int(input("Digite a nota que desejar (0-10): "))
                  
                  #Se o usuário digitar um número maior ou menor, aparece uma mensagem de erro.
                  if notaFeedback < 0 or notaFeedback > 10:
                        print("Os números permitidos são apenas de 0 a 10!")
                  else:
                        reclamacao = input("Escreva sua reclamação ou aperte ENTER para enviar: ")
                        print(f"A PlanTech agradece pelo seu feedback!")
            elif feedback == 2:
                  notaFeedback = int(input("Digite a nota que desejar (0-10): "))
                  if notaFeedback < 0 or notaFeedback > 10:
                        print("Os números permitidos são apenas de 0 a 10!")
                  else:
                        reclamacao = input("Escreva sua reclamação ou aperte ENTER para enviar:")
                        print(f"A PlanTech agradece pelo seu feedback!")
            elif feedback == 3:
                  notaFeedback = int(input("Digite a nota que desejar (0-10): "))
                  if notaFeedback < 0 or notaFeedback > 10:
                        print("Os números permitidos são apenas de 0 a 10!")
                  else:
                        reclamacao = input("Escreva sua reclamação ou aperte ENTER para enviar: ")
                        print(f"A PlanTech agradece pelo seu feedback!")
            elif feedback == 4:
                  notaFeedback = int(input("Digite a nota que desejar (0-10): "))
                  if notaFeedback < 0 or notaFeedback > 10:
                        print("Os números permitidos são apenas de 0 a 10!")
                  else:
                        reclamacao = input("Escreva sua reclamação ou aperte ENTER para enviar: ")
                        print(f"A PlanTech agradece pelo seu feedback!")
            elif feedback == 5:
                  notaFeedback = int(input("Digite a nota que desejar (0-10): "))
                  if notaFeedback < 0 or notaFeedback > 10:
                        print("Os números permitidos são apenas de 0 a 10!")
                  else:
                        reclamacao = input("Escreva sua reclamação ou aperte ENTER para enviar: ")
                        print(f"A PlanTech agradece pelo seu feedback!")

      if opcaoMenu == 7:
            print("-")

#Opção 8 do menu: outro
      if opcaoMenu == 8:
            print('\nVeja só:')
            print('1. Se quiser retirar suas dúvidas mais específicas, entre no nosso ChatBot que ele te auxiliará')
            print('2. Se quer textos mais explicativos como agricultura sustentável, uso de IAs generativas na produção, distribuição de alimentos pelo mundo, modelos de cultivos eficientes, calendário de controle de pragas ou outros textos, entre no site da PlanTech')

#Opção 9 do menu: encerramento
      if opcaoMenu == 9:
            print('\nMuito obrigado, até a próxima!')