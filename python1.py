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

      #Algodão
      if nomePlanta == 'algodão' or nomePlanta == 'algodao' or nomePlanta == 'Algodão' or nomePlanta == 'Algodao':
            if nomePraga == 'Lagarta-do-cartucho' or nomePraga == 'lagarta-do-cartucho' or nomePraga == 'Lagarta-do-Cartucho' or nomePraga == 'Lagarta do cartucho' or nomePraga == 'lagarta do cartucho' or nomePraga == 'Lagarta do Cartucho':
                  print(f'\n{spodovir}')
                  return spodovir
            elif nomePraga == 'Percevejo-marrom' or nomePraga == 'percevejo-marrom' or nomePraga == 'Percevejo-Marrom' or nomePraga == 'Percevejo marrom' or nomePraga == 'percevejo marrom' or nomePraga == 'Percevejo Marrom':
                  print(f'\n{engeoPlenoS}'
                        '\nObservação: de 200 a 250 mL por hectare com no máximo 3 aplicações, uma a cada 7 dias; o volume da calda deve ser de 150 litros por hectare')
                  return engeoPlenoS
            elif nomePraga == 'Lagarta helicoverpa' or nomePraga == 'lagarta helicoverpa' or nomePraga == 'Lagarta Helicoverpa':
                  print(f'\n{bacillus}')
                  return bacillus
            elif nomePraga == 'Pulgão do algodoeiro' or nomePraga == 'Pulgao do algodoeiro' or nomePraga == 'pulgão do algodoeiro' or nomePraga == 'pulgao do algodoeiro' or nomePraga == 'Pulgão do Algodoeiro' or nomePraga == 'Pulgao do Algodoeiro':
                  print(f'\n{aug}'
                        '\nObservação: de 540 a 720 mL a cada 100kg com no máximo 1 aplicação; o volume da calda deve ser de 500mL a cada 100kg.')
                  return aug
            elif nomePraga == 'Tripes' or nomePraga == 'tripes':
                  print(f'{aug}'
                        '\nObservação: de 540 a 720 mL a cada 100kg com no máximo 1 aplicação; o volume da calda deve ser de 500mL a cada 100kg.')
                  return aug
            elif nomePraga == 'Cupim do montículo' or nomePraga == 'Cupim do monticulo' or nomePraga == 'cupim do montículo' or nomePraga == 'cupim do monticulo' or  nomePraga == 'Cupim do Montículo' or nomePraga == 'Cupim do Monticulo':       
                  print(f'{aug}'
                        '\nObservação: 720 mL a cada 100kg com no máximo 1 aplicação; o volume da calda deve ser de 500mL a cada 100kg.')
                  return aug
            else:
                  print('Essa praga não está em nosso sistema')
      
      #Arroz
      elif nomePlanta == 'arroz' or nomePlanta == 'Arroz':
            if nomePraga == 'Lagarta-do-cartucho' or nomePraga == 'Lagarta do cartucho' or nomePraga == 'lagarta-do-cartucho' or nomePraga == 'lagarta do cartucho' or nomePraga == 'Lagarta-do-Cartucho' or nomePraga == 'Lagarta do Cartucho':
                  print (f'{spodovir}')
                  return spodovir
            elif nomePraga == 'Percevejo-do-arroz' or nomePraga == 'Percevejo do arroz' or nomePraga == 'percevejo-do-arroz' or nomePraga == 'percevejo do arroz' or nomePraga == 'Percevejo-do-Arroz' or nomePraga == 'Percevejo do Arroz':
                  print (f'{engeoPlenoS}'
                         '\nObservação: de 150 a 200 mL por hectare com no máximo 1 aplicação; o volume da calda deve ser de 200 litros por hectare')
                  return engeoPlenoS
            else:
                  print('Essa praga não está em nosso sistema')
      
      #Aveia
      elif nomePlanta == 'aveia' or nomePlanta == 'Aveia':
            if nomePraga == 'Lagarta-do-cartucho' or nomePraga == 'Lagarta do cartucho' or nomePraga == 'lagarta-do-cartucho' or nomePraga == 'lagarta do cartucho' or nomePraga == 'Lagarta-do-Cartucho' or nomePraga == 'Lagarta do Cartucho':
                  print (f'{spodovir}')
                  return spodovir
            else:
                  print('Essa praga não está em nosso sistema')
      
      #Café
      elif nomePlanta == 'cafe' or nomePlanta == 'café' or nomePlanta == 'Cafe' or nomePlanta == 'Café':
            if nomePraga == 'Lagarta helicoverpa' or nomePraga == 'lagarta helicoverpa' or nomePraga == 'Lagarta Helicoverpa':
                  print (f'{bacillus}')
                  return bacillus
            else:
                  print('Essa praga não está em nosso sistema')

      #Cana-de-açúcar
      elif nomePlanta == 'Cana-de-açúcar' or nomePlanta == 'Cana-de-açucar' or nomePlanta == 'Cana-de-acucar' or nomePlanta == 'Cana-de-acúcar' or nomePlanta == 'Cana de açúcar' or nomePlanta == 'Cana de açucar' or nomePlanta == 'Cana de acucar' or nomePlanta == 'Cana de acúcar' or nomePlanta == 'cana-de-açúcar' or nomePlanta == 'cana-de-açucar' or nomePlanta == 'cana-de-acucar' or nomePlanta == 'cana-de-acúcar' or nomePlanta == 'cana de açúcar' or nomePlanta == 'cana de açucar' or nomePlanta == 'cana de acucar' or nomePlanta == 'cana de acúcar' or nomePlanta == 'Cana-de-Açúcar' or nomePlanta == 'Cana-de-Açucar' or nomePlanta == 'Cana-de-Acucar' or nomePlanta == 'Cana-de-Acúcar' or nomePlanta == 'Cana de Açúcar' or nomePlanta == 'Cana de Açucar' or nomePlanta == 'Cana de Acucar' or nomePlanta == 'Cana de Acúcar':
            if nomePraga == 'Lagarta-do-cartucho' or nomePraga == 'Lagarta do cartucho' or nomePraga == 'lagarta-do-cartucho' or nomePraga == 'lagarta do cartucho' or nomePraga == 'Lagarta-do-Cartucho' or nomePraga == 'Lagarta do Cartucho':
                  print(f'{spodovir}')
                  return spodovir
            else:
                  print('Essa praga não está em nosso sistema')
      
      #Feijão
      elif nomePlanta == 'Feijao' or nomePlanta == 'Feijão' or nomePlanta == 'feijao' or nomePlanta == 'Feijão':
            if nomePraga == 'Lagarta-do-cartucho' or nomePraga == 'Lagarta do cartucho' or nomePraga == 'lagarta-do-cartucho' or nomePraga == 'lagarta do cartucho' or nomePraga == 'Lagarta-do-Cartucho' or nomePraga == 'Lagarta do Cartucho':
                  print(f'{spodovir}')
                  return spodovir
            elif nomePraga == 'Lagarta helicoverpa' or nomePraga == 'lagarta helicoverpa' or nomePraga == 'Lagarta Helicoverpa':
                  print (f'{bacillus}')
                  return bacillus
            else:
                  print('Essa praga não está em nosso sistema')
      
      #Girassol
      elif nomePlanta == 'girassol' or nomePlanta == 'Girassol':
            if nomePraga == 'Percevejo-verde-pequeno' or nomePraga == 'Percevejo-Verde-Pequeno' or nomePraga == 'percevejo-verde-pequeno' or nomePraga == 'Percevejo verde pequeno' or nomePraga == 'Percevejo verde pequeno' or nomePraga == 'percevejo verde pequeno':
                  print(f'{engeoPlenoS}'
                        '\nObservação: de 300 a 400 mL por hectare com no máximo 2 aplicações, uma a cada 7 dias; o volume da calda deve ser de 150 litros por hectare')
                  return engeoPlenoS
            elif nomePraga == 'Percevejo-da-soja' or nomePraga == 'percevejo-da-soja' or nomePraga == 'Percevejo-da-Soja' or nomePraga == 'Percevejo da soja' or nomePraga == 'percevejo da soja' or nomePraga == 'Percevejo da Soja':
                  print(f'{engeoPlenoS}'
                        '\nObservação: de 300 a 400 mL por hectare com no máximo 2 aplicações, uma a cada 7 dias; o volume da calda deve ser de 150 litros por hectare')
                  return engeoPlenoS
            elif nomePraga == 'Percevejo-marrom' or nomePraga == 'percevejo-marrom' or nomePraga == 'Percevejo-Marrom' or nomePraga == 'Percevejo marrom' or nomePraga == 'percevejo marrom' or nomePraga == 'Percevejo Marrom':
                  print(f'{engeoPlenoS}'
                        '\nObservação: de 300 a 400 mL por hectare com no máximo 2 aplicações, uma a cada 7 dias; o volume da calda deve ser de 150 litros por hectare')
                  return engeoPlenoS
            else:
                  print('Essa praga não está em nosso sistema')
      
      #Milho
      elif nomePlanta == 'milho' or nomePlanta == 'Milho':
            if nomePraga == 'Percevejo-barriga-verde' or nomePraga == 'Percevejo-Barriga-Verde' or nomePraga == 'percevejo-barriga-verde' or nomePraga == 'Percevejo barriga verde' or nomePraga == 'Percevejo Barriga Verde' or nomePraga == 'percevejo-barriga-verde':
                  print(f'{engeoPlenoS}'
                        '\nObservação: de 150 a 250 mL por hectare com no máximo 2 aplicações, uma a cada 7 dias; o volume da calda deve ser de 200 litros por hectare')
                  return engeoPlenoS
            elif nomePraga == 'Lagarta helicoverpa' or nomePraga == 'lagarta helicoverpa' or nomePraga == 'Lagarta Helicoverpa':
                  print (f'{bacillus}')
                  return bacillus
            elif nomePraga == 'Cigarrinha do milho' or nomePraga == 'cigarrinha do milho' or nomePraga == 'Cigarrinha do Milho':
                  print (f'{aug}'
                         '\nObservação: 960 mL para cada 100kg com apenas uma aplicação; o volume da calda deve ser 500 mL para cada 100kg')
                  return aug
            elif nomePraga == 'Vaquinha verde amarela' or nomePraga == 'vaquinha verde amarela' or nomePraga == 'Vaquinha Verde Amarela':
                  print(f'{aug}'
                        '\nObservação: 960 mL para cada 100kg com apenas uma aplicação; o volume da calda deve ser 500 mL para cada 100kg')
                  return aug
            elif nomePraga == 'Cupim' or nomePraga == 'cupim':
                  print(f'{aug}'
                        '\nObservação: 300 mL para cada 100kg com apenas uma aplicação; o volume da calda deve ser 500 mL para cada 100kg')
                  return aug
            elif nomePraga == 'Pulgão' or nomePraga == 'Pulgao' or nomePraga == 'pulgão' or nomePraga == 'pulgao':
                  print(f'{aug}'
                        '\nObservação: 480 mL para cada 100kg com apenas uma aplicação; o volume da calda deve ser 500 mL para cada 100kg')
                  return aug
            else:
                  print('Essa praga não está em nosso sistema')
      
      #Soja
      elif nomePlanta == 'soja' or nomePlanta == 'Soja':
            if nomePraga == 'Lagarta-do-cartucho' or nomePraga == 'Lagarta do cartucho' or nomePraga == 'lagarta-do-cartucho' or nomePraga == 'lagarta do cartucho' or nomePraga == 'Lagarta-do-Cartucho' or nomePraga == 'Lagarta do Cartucho':
                  print(f'{spodovir}')
                  return spodovir
            elif nomePraga == 'Percevejo-marrom' or nomePraga == 'percevejo-marrom' or nomePraga == 'Percevejo-Marrom' or nomePraga == 'Percevejo marrom' or nomePraga == 'percevejo marrom' or nomePraga == 'Percevejo Marrom':
                  print(f'{engeoPlenoS}'
                        '\nObservação: 200 mL por hectare com no máximo 2 aplicações, uma a cada 7 dias; o volume da calda deve ser de 200 litros por hectare.')
                  return engeoPlenoS
            elif nomePraga == 'Percevejo-verde-pequeno' or nomePraga == 'Percevejo-Verde-Pequeno' or nomePraga == 'percevejo-verde-pequeno' or nomePraga == 'Percevejo verde pequeno' or nomePraga == 'Percevejo verde pequeno' or nomePraga == 'percevejo verde pequeno':
                  print(f'{engeoPlenoS}'
                        '\nObservação: de 150 a 180 mL por hectare com no máximo 2 aplicações, uma a cada 7 dias; o volume da calda deve ser de 200 litros por hectare')
                  return engeoPlenoS
            elif nomePraga == 'Percevejo-da-soja' or nomePraga == 'percevejo-da-soja' or nomePraga == 'Percevejo-da-Soja' or nomePraga == 'Percevejo da soja' or nomePraga == 'percevejo da soja' or nomePraga == 'Percevejo da Soja':
                  print(f'{engeoPlenoS}'
                        '\nObservação: de 150 a 180 mL por hectare com no máximo 2 aplicações, uma a cada 7 dias; o volume da calda deve ser de 200 litros por hectare')
                  return engeoPlenoS
            elif nomePraga == 'Lagarta helicoverpa' or nomePraga == 'lagarta helicoverpa' or nomePraga == 'Lagarta Helicoverpa':
                  print (f'{bacillus}')
                  return bacillus
            else:
                  print('Essa praga não está em nosso sistema')
            
      #Trigo
      elif nomePlanta == 'trigo' or nomePlanta == 'Trigo':
            if nomePraga == 'Lagarta-do-cartucho' or nomePraga == 'Lagarta do cartucho' or nomePraga == 'lagarta-do-cartucho' or nomePraga == 'lagarta do cartucho' or nomePraga == 'Lagarta-do-Cartucho' or nomePraga == 'Lagarta do Cartucho':
                  print(f'{spodovir}')
                  return spodovir
            elif nomePraga == 'Percevejo-barriga-verde' or nomePraga == 'Percevejo-Barriga-Verde' or nomePraga == 'percevejo-barriga-verde' or nomePraga == 'Percevejo barriga verde' or nomePraga == 'Percevejo Barriga Verde' or nomePraga == 'percevejo-barriga-verde':
                  print(f'{engeoPlenoS}'
                        '\nObservação: 150 mL por hectare com no máximo 2 aplicações, uma a cada 7 dias; o volume da calda deve ser de 200 litros por hectare')
                  return engeoPlenoS
            else:
                  print('Essa praga não está em nosso sistema')
      else:
            print('Essa planta não está em nosso sistema')

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
opcaoMenu = 0
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

#Opção 1 do menu: desejo saber mais sobre a missão da PlanTech ---- Colocar o primeiro e o último parágrafo do
#   arquivo "Descrição geral da solução 2"
      if opcaoMenu == 1:
            print("\n---- PlanTech ----"
                        + "\n A fome e a insegurança alimentar são problemas mundiais que afetam milhões de pessoas e acarretam muitos" 
                        + " outros problemas, como o nanismo e a caquexia. São muitos os fatores que podem levar à fome, tais como a falta de agricultura sustentável," 
                        + " falta de acesso à alimentos, desigualdades, desemprego, alimentos não-nutritivos, entre outros fatores. Pensando nisso," 
                        + " a PlanTech desenvolveu um projeto que visa a diminuição do desperdício de alimentos e o cultivo de alimentos mais saudáveis com o combate de pragas" 
                        + " ainda em sua fase inicial de ataque nas plantações.   "
                        + "\n Os benefícios dessa tecnologia é a detecção da praga em fase inicial, o que reduz o nível de perda de alimentos e o valor do produto final," 
                        + " a preservação do solo e das plantações e a garantia de uma alimentação saudável e nutritiva – pois a indicação de tratamento da plantação é saudável." 
                        + " Essa tecnologia pode ser levada para agricultores familiares e regiões mais afastadas que muito sofrem com esse problema, pois, dessa forma," 
                        + " contribuirá com o acesso à uma tecnologia capaz de diminuir suas perdas de alimentos por pragas. Além disso, estes pequenos agricultores se sentirão mais confiantes" 
                        + " em expandir sua área de plantio, já que não terá a preocupação com a perda de sua plantação.")

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
      if opcaoMenu == 3:
            print("\nA PlanTech ainda é um projeto em desenvolvimento, ainda não é possível realizar a compra dos drones.")
            opcSimulacao = input("\nDeseja realizar uma simulação da compra dos drone que serão disponibilizados pela PlanTech? \n(1) - Sim \n(2) - Não \nEscolha uma opção: ")
            opcSimulacaoup = opcSimulacao.upper()
            if opcSimulacaoup == "1" or  opcSimulacaoup == "SIM":
                 Cadastro()




#Opção 4 do menu: Identifiquei uma praga na plantação. O que faço agora?
      if opcaoMenu == 4:
            print(Indicacao())

#Opção 5 do menu: quem faz parte do projeto PlanTech? ---- Colocar o nome e RM de todos do grupo
      if opcaoMenu == 5:
            print("\nTodas as pessoas responsáveis pelo projeto PlanTech são: \nDouglas Magalhães de Araujo - rm552008 \nGustavo Arguello Bertacci - rm551304 \nIgor Ribeiro Anccilotto - rm550415 \nLuiz Fillipe Farias - rm99519 \nRafaella Monique do Carmo Bastos - rm552425")

#Opção 6 do menu: quero indicar o tratamento para uma praga ---- Deixar com que o usuário informe o nome de uma 
#   praga, o tipo de plantação que essa praga ataca e o tipo de tratamento que essa praga combinada com essa 
#   plantação pode receber; Mostrar uma mensagem agradecendo e dizendo que essas informações vão para análise e
#   se estiver tudo correto, serão incluídas no sistema PlanTech
      if opcaoMenu == 6:
            print("-")

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