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

      nomePlanta = nomePlanta.upper()
      nomePraga = nomePraga.upper()

      #Algodão
      if nomePlanta == 'ALGODÃO' or nomePlanta == 'ALGODAO':
            if nomePraga == 'LAGARTA-DO-CARTUCHO' or 'LAGARTA DO CARTUCHO':
                  print(f'\n{spodovir}')
                  return spodovir
            
            elif nomePraga == 'PERCEVEJO-MARROM' or nomePraga == 'PERCEVEJO MARROM':
                  print(f'\n{engeoPlenoS}')
                  print('\nObservação: de 200 a 250 mL por hectare com no máximo 3 aplicações, uma a cada 7 dias; o volume da calda deve ser de 150 litros por hectare')
                  return engeoPlenoS
            
            elif nomePraga == 'LAGARTA HELICOVERPA':
                  print(f'\n{bacillus}')
                  return bacillus
            
            elif nomePraga == 'PULGÃO DE ALGODOEIRO' or nomePraga == 'PULGAO DE ALGODOEIRO':
                  print(f'\n{aug}')
                  print('\nObservação: de 540 a 720 mL a cada 100kg com no máximo 1 aplicação; o volume da calda deve ser de 500mL a cada 100kg.')
                  return aug
            
            elif nomePraga == 'TRIPES':
                  print(f'{aug}')
                  print('\nObservação: de 540 a 720 mL a cada 100kg com no máximo 1 aplicação; o volume da calda deve ser de 500mL a cada 100kg.')
                  return aug
            
            elif nomePraga == 'CUPIM DO MONTÍCULO' or nomePraga == 'CUPIM DO MONTICULO':       
                  print(f'{aug}')
                  print('\nObservação: 720 mL a cada 100kg com no máximo 1 aplicação; o volume da calda deve ser de 500mL a cada 100kg.')
                  return aug
            else:
                  print('Essa praga não está em nosso sistema')
      

      #Arroz
      elif nomePlanta == 'ARROZ':
            if nomePraga == 'LAGARTA-DO-CARTUCHO' or nomePraga == 'LAGARTA DO CARTUCHO':
                  print (f'{spodovir}')
                  return spodovir
            
            elif nomePraga == 'PERCEVEJO-DO-ARROZ' or nomePraga == 'PERCEVEJO DO ARROZ':
                  print (f'{engeoPlenoS}')
                  print('\nObservação: de 150 a 200 mL por hectare com no máximo 1 aplicação; o volume da calda deve ser de 200 litros por hectare')
                  return engeoPlenoS
            else:
                  print('Essa praga não está em nosso sistema')
      

      #Aveia
      elif nomePlanta == 'AVEIA':
            if nomePraga == 'LAGARTA-DO-CARTUCHO' or nomePraga == 'LAGARTA DO CARTUCHO':
                  print (f'{spodovir}')
                  return spodovir
            else:
                  print('Essa praga não está em nosso sistema')
      

      #Café
      elif nomePlanta == 'CAFÉ' or nomePlanta == 'CAFE':
            if nomePraga == 'LAGARTA HELICOVERPA':
                  print (f'{bacillus}')
                  return bacillus
            else:
                  print('Essa praga não está em nosso sistema')


      #Cana-de-açúcar
      elif nomePlanta == 'CANA-DE-AÇÚCAR' or 'CANA-DE-AÇUCAR' or 'CANA-DE-ACUCAR' or 'CANA DE AÇÚCAR' or 'CANA DE AÇUCAR' or 'CANA DE AÇUCAR' or 'CANA DE ACUCAR':
            if nomePraga == 'LAGARTA-DO-CARTUCHO' or nomePraga == 'LAGARTA DO CARTUCHO':
                  print(f'{spodovir}')
                  return spodovir
            else:
                  print('Essa praga não está em nosso sistema')
      

      #Feijão
      elif nomePlanta == 'FEIJAO' or nomePlanta == 'FEIJÃO':
            if nomePraga == 'LAGARTA-DO-CARTUCHO' or nomePraga == 'LAGARTA DO CARTUCHO':
                  print(f'{spodovir}')
                  return spodovir
            
            elif nomePraga == 'LAGARTA HELICOVERPA':
                  print (f'{bacillus}')
                  return bacillus
            else:
                  print('Essa praga não está em nosso sistema')
      

      #Girassol
      elif nomePlanta == 'GIRASSOL':
            if nomePraga == 'PERCEVEJO-VERDE-PEQUENO' or nomePraga == 'PERCEVEJO VERDE PEQUENO':
                  print(f'{engeoPlenoS}')
                  print('\nObservação: de 300 a 400 mL por hectare com no máximo 2 aplicações, uma a cada 7 dias; o volume da calda deve ser de 150 litros por hectare')
                  return engeoPlenoS
            
            elif nomePraga == 'PERCEVEJO-DA-SOJA' or nomePraga == 'PERCEVEJO DA SOJA':
                  print(f'{engeoPlenoS}')
                  print('\nObservação: de 300 a 400 mL por hectare com no máximo 2 aplicações, uma a cada 7 dias; o volume da calda deve ser de 150 litros por hectare')
                  return engeoPlenoS
            
            elif nomePraga == 'PERCEVEJO-MARROM' or nomePraga == 'PERCEVEJO MARROM':
                  print(f'{engeoPlenoS}')
                  print('\nObservação: de 300 a 400 mL por hectare com no máximo 2 aplicações, uma a cada 7 dias; o volume da calda deve ser de 150 litros por hectare')
                  return engeoPlenoS
            else:
                  print('Essa praga não está em nosso sistema')
      
      
      #Milho
      elif nomePlanta == 'MILHO':
            if nomePraga == 'PERCEVEJO-BARRIGA-VERDE' or nomePraga == 'PERCEVEJO BARRIGA VERDE':
                  print(f'{engeoPlenoS}')
                  print('\nObservação: de 150 a 250 mL por hectare com no máximo 2 aplicações, uma a cada 7 dias; o volume da calda deve ser de 200 litros por hectare')
                  return engeoPlenoS
            
            elif nomePraga == 'LAGARTA HELICOVERPA':
                  print (f'{bacillus}')
                  return bacillus
            
            elif nomePraga == 'CIGARRINHA DO MILHO':
                  print (f'{aug}')
                  print('\nObservação: 960 mL para cada 100kg com apenas uma aplicação; o volume da calda deve ser 500 mL para cada 100kg')
                  return aug
            
            elif nomePraga == 'VAQUINHA VERDE AMARELA':
                  print(f'{aug}')
                  print('\nObservação: 960 mL para cada 100kg com apenas uma aplicação; o volume da calda deve ser 500 mL para cada 100kg')
                  return aug
            
            elif nomePraga == 'CUPIM':
                  print(f'{aug}')
                  print('\nObservação: 300 mL para cada 100kg com apenas uma aplicação; o volume da calda deve ser 500 mL para cada 100kg')
                  return aug
            
            elif nomePraga == 'PULGÃO' or nomePraga == 'PULGAO':
                  print(f'{aug}')
                  print('\nObservação: 480 mL para cada 100kg com apenas uma aplicação; o volume da calda deve ser 500 mL para cada 100kg')
                  return aug
            else:
                  print('Essa praga não está em nosso sistema')
      

      #Soja
      elif nomePlanta == 'SOJA':
            if nomePraga == 'LAGARTA-DO-CARTUCHO' or nomePraga == 'LAGARTA DO CARTUCHO':
                  print(f'{spodovir}')
                  return spodovir
            
            elif nomePraga == 'PERCEVEJO-MARROM' or nomePraga == 'PERCEVEJO MARROM':
                  print(f'{engeoPlenoS}')
                  print('\nObservação: 200 mL por hectare com no máximo 2 aplicações, uma a cada 7 dias; o volume da calda deve ser de 200 litros por hectare.')
                  return engeoPlenoS
            
            elif nomePraga == 'PERCEVEJO-VERDE-PEQUENO' or nomePraga == 'PERCEVEJO VERDE PEQUENO':
                  print(f'{engeoPlenoS}')
                  print('\nObservação: de 150 a 180 mL por hectare com no máximo 2 aplicações, uma a cada 7 dias; o volume da calda deve ser de 200 litros por hectare')
                  return engeoPlenoS
            
            elif nomePraga == 'PERCEVEJO-DA-SOJA' or nomePraga == 'PERCEVEJO DA SOJA':
                  print(f'{engeoPlenoS}')
                  print('\nObservação: de 150 a 180 mL por hectare com no máximo 2 aplicações, uma a cada 7 dias; o volume da calda deve ser de 200 litros por hectare')
                  return engeoPlenoS
            
            elif nomePraga == 'LAGARTA HELICOVERPA':
                  print (f'{bacillus}')
                  return bacillus
            else:
                  print('Essa praga não está em nosso sistema')


      #Trigo
      elif nomePlanta == 'TRIGO':
            if nomePraga == 'LAGARTA-DO-CARTUCHO' or nomePraga == 'LAGARTA DO CARTUCHO':
                  print(f'{spodovir}')
                  return spodovir
            
            elif nomePraga == 'PERCEVEJO-BARRIGA-VERDE' or nomePraga == 'PERCEVEJO BARRIGA VERDE':
                  print(f'{engeoPlenoS}')
                  print('\nObservação: 150 mL por hectare com no máximo 2 aplicações, uma a cada 7 dias; o volume da calda deve ser de 200 litros por hectare')
                  return engeoPlenoS
            else:
                  print('Essa praga não está em nosso sistema')
      else:
            print('Essa planta não está em nosso sistema')

#Função para fazer o cadastro
def Cadastro():
      confirmCadastroup = ''
      print('\nPor favor realize o cadastro: ')
      while confirmCadastroup != "1" and confirmCadastroup != "SIM":
            opcIdentup = ''
            opcIdent2up = ''
            opcComplementoup = ''
            confirmCadastroup = ''
            rg = ''
            telefone = ''
            cep = ''
            cnh = ''
            NomeCompleto = ''
            email = ''
            rua = ''
            nmrResidencia = ''
            pais = ''
            estado = ''
            cidade = ''
            bairro = ''

            while NomeCompleto == '':
                  NomeCompleto = input("\nDigite seu nome: ")
            while opcIdentup != "1" and opcIdentup != "RG" and opcIdentup != "2" and opcIdentup != "CNH":
                  opcIdent = input("\n(1) - RG \n(2) - CNH \nEscolha qual você deseja informar: ")
                  opcIdentup = opcIdent.upper()
                  if opcIdentup == "1" or opcIdentup == "RG":
                        while len(rg) != 9:      
                              rg = input("\nRG: ")
                              if  len(rg) != 9:
                                    print("RG inválido! Digite apenas números.")
                        
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
            print("Lembramos que foi apenas uma simulação, a PlanTech está em desenvolvimento e, portanto, os drones não serão enviados.")
      else:
            print("O limite de drones é de 1 a 999.")

#menu
opcaoMenu = 0
while opcaoMenu != 9:
      print('\nSeja bem vindo à PlanTech! No que podemos te ajudar?'
            '\n'
            '\n1. Desejo saber mais sobre a missão da PlanTech'
            '\n2. Desejo saber sobre o funcionamento do drone' #Igor
            '\n3. Quero comprar um drone para detectar pragas'
            '\n4. Identifiquei uma praga na plantação. O que faço agora?'
            '\n5. Quem faz parte do projeto PlanTech?'
            '\n6. Quero indicar um tratamento para uma praga' #Gustavo
            '\n7. Feedback'
            '\n8. Outro'
            '\n9. Encerrar')
      opcaoMenu = int(input('Selecione uma das opções acima: '))

#Opção 1 do menu: desejo saber mais sobre a missão da PlanTech
      if opcaoMenu == 1:
            print('\n---- PlanTech ----'
                        + '\n A fome e a insegurança alimentar são problemas mundiais que afetam milhões de pessoas e acarretam muitos'
                        + ' outros problemas, como o nanismo e a caquexia. São muitos os fatores que podem levar à fome, tais como a falta de agricultura sustentável,'
                        + ' falta de acesso à alimentos, desigualdades, desemprego, alimentos não-nutritivos, entre outros fatores. Pensando nisso,'
                        + ' a PlanTech desenvolveu um projeto que visa a diminuição do desperdício de alimentos e o cultivo de alimentos mais saudáveis com o combate de pragas'
                        + ' ainda em sua fase inicial de ataque nas plantações.   '
                        + '\n Os benefícios dessa tecnologia é a detecção da praga em fase inicial, o que reduz o nível de perda de alimentos e o valor do produto final,'
                        + ' a preservação do solo e das plantações e a garantia de uma alimentação saudável e nutritiva – pois a indicação de tratamento da plantação é saudável.'
                        + ' Essa tecnologia pode ser levada para agricultores familiares e regiões mais afastadas que muito sofrem com esse problema, pois, dessa forma,'
                        + ' contribuirá com o acesso à uma tecnologia capaz de diminuir suas perdas de alimentos por pragas. Além disso, estes pequenos agricultores se sentirão mais confiantes'
                        + ' em expandir sua área de plantio, já que não terá a preocupação com a perda de sua plantação.')


#Opção 2 do menu: desejo saber sobre o funcionamenento do drone ---- Colocar o segundo parágrafo do arquivo
#   "Descrição geral da solução 2"
      if opcaoMenu == 2:
            print("-")


#Opção 3 do menu: quero comprar um drone para detectar pragas 
      if opcaoMenu == 3:
            print("\nA PlanTech ainda é um projeto em desenvolvimento e, por isso, não é possível realizar a compra dos drones.")
            opcSimulacao = input("\nDeseja realizar uma simulação da compra dos drone que serão disponibilizados pela PlanTech? \n(1) - Sim \n(2) - Não \nEscolha uma opção: ")
            opcSimulacaoup = opcSimulacao.upper()
            if opcSimulacaoup == "1" or  opcSimulacaoup == "SIM":
                 Cadastro()


#Opção 4 do menu: Identifiquei uma praga na plantação. O que faço agora?
      if opcaoMenu == 4:
            print(Indicacao())


#Opção 5 do menu: quem faz parte do projeto PlanTech? ---- Colocar o nome e RM de todos do grupo
      if opcaoMenu == 5:
            print('\nTodas as pessoas responsáveis pelo projeto PlanTech são: \nDouglas Magalhães de Araujo - rm552008 \nGustavo Arguello Bertacci - rm551304 \nIgor Ribeiro Anccilotto - rm550415 \nLuiz Fillipe Farias - rm99519 \nRafaella Monique do Carmo Bastos - rm552425')


#Opção 6 do menu: quero indicar o tratamento para uma praga ---- Deixar com que o usuário informe o nome de uma 
#   praga, o tipo de plantação que essa praga ataca e o tipo de tratamento que essa praga combinada com essa 
#   plantação pode receber; Mostrar uma mensagem agradecendo e dizendo que essas informações vão para análise e
#   se estiver tudo correto, serão incluídas no sistema PlanTech
      if opcaoMenu == 6:
            print("-")


#Opção 7 do menu: feedback
      if opcaoMenu == 7:
            #menu que pergunta para o usuário a escolha do feedback.
            feedback = int(input('\nPrimeiro, informe o tipo do feedback: \n(1) - Resolução de suas dúvidas \n(2) - Performace do sistema \n(3) - Indicação dos tratamentos para as plantações \n(4) - Usabilidade do projeto \n(5) - Experiência com o site'))
            #se o usuário digitar um número maior ou menor, aparece uma mensagem de erro.
            if feedback < 1 or feedback > 5:
                  print('Escolha incorreta! Escolha um número de 1 a 5.')

            #O usuário digita a nota do feedback de 0 até 10, e depois escreve uma observação.
            elif feedback == 1:
                  notaFeedback = int(input('Digite a nota que desejar (0-10): '))
                  
                  #Se o usuário digitar um número maior ou menor, aparece uma mensagem de erro.
                  if notaFeedback < 0 or notaFeedback > 10:
                        print('Os números permitidos são apenas de 0 a 10!')
                  else:
                        reclamacao = input('Escreva sua reclamação ou aperte ENTER para enviar: ')
                        print(f'\nA PlanTech agradece pelo seu feedback!')
            elif feedback == 2:
                  notaFeedback = int(input('Digite a nota que desejar (0-10): '))
                  if notaFeedback < 0 or notaFeedback > 10:
                        print('Os números permitidos são apenas de 0 a 10!')
                  else:
                        reclamacao = input('Escreva sua reclamação ou aperte ENTER para enviar: ')
                        print(f'\nA PlanTech agradece pelo seu feedback!')
            elif feedback == 3:
                  notaFeedback = int(input('Digite a nota que desejar (0-10): '))
                  if notaFeedback < 0 or notaFeedback > 10:
                        print('Os números permitidos são apenas de 0 a 10!')
                  else:
                        reclamacao = input('Escreva sua reclamação ou aperte ENTER para enviar: ')
                        print(f'\nA PlanTech agradece pelo seu feedback!')
            elif feedback == 4:
                  notaFeedback = int(input('Digite a nota que desejar (0-10): '))
                  if notaFeedback < 0 or notaFeedback > 10:
                        print('Os números permitidos são apenas de 0 a 10!')
                  else:
                        reclamacao = input('Escreva sua reclamação ou aperte ENTER para enviar: ')
                        print(f'\nA PlanTech agradece pelo seu feedback!')
            elif feedback == 5:
                  notaFeedback = int(input('Digite a nota que desejar (0-10): '))
                  if notaFeedback < 0 or notaFeedback > 10:
                        print('Os números permitidos são apenas de 0 a 10!')
                  else:
                        reclamacao = input('Escreva sua reclamação ou aperte ENTER para enviar: ')
                        print(f'\nA PlanTech agradece pelo seu feedback!')


#Opção 8 do menu: outro
      if opcaoMenu == 8:
            print('\nVeja só:')
            print('1. Se quiser retirar suas dúvidas mais específicas, entre no nosso ChatBot que ele te auxiliará')
            print('2. Se quer textos mais explicativos como agricultura sustentável, uso de IAs generativas na produção, distribuição de alimentos pelo mundo, modelos de cultivos eficientes, calendário de controle de pragas ou outros textos, entre no site da PlanTech')


#Opção 9 do menu: encerramento
      if opcaoMenu == 9:
            print('\nMuito obrigado, até a próxima!')