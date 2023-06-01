def Indicacao():
      spodovir = ('Tratamento para a sua plantação: Spodovir'
                  '\n1. É um biodefensivo e inseticida microbiológico'
                  '\n2. Deve ser utilizado assim que a praga for identificada ou de 10 a 22 dias após a germinação das plantações'
                  '\n3. É recomendado pulverizar o produto sobre a cultura com a utilização do volume da calda de 150 litros do produto por hectare se for por via terrestre ou 50 litros do produto por hectare se for por via aérea'
                  '\n4. Uma dose pode ser diluída em 1 litro de água'
                  '\n5. Para informações de como fazer, precauções e mais, leia a bula que vem junto ao produto no momento da compra.')
      
      engeoPlenoS = ('Tratamento para a sua platação: Engeo Pleno S'
                     '\n1. Para informações de como fazer, precauções e mais, leia a bula que vem junto ao produto no momento da compra.') 
      
      bacillus = ('Tratamento para a sua plantação: Bacillus Thuringienses'
                  '\n1. É um inseticida biológico'
                  '\n2. Inseticida biológico com a recomendação de pulverização sobre a cultura com a utilização de 500 a 750 gramas por hectare, sendo a utilização do volume da calda de 200 litros por hectare'
                  '\n3. Para informações de como fazer, precauções e mais, leia a bula que vem junto ao produto no momento da compra.')
      
      aug = ('Tratamento para a sua plantação: AUG 106'
             '\n1. É um inseticida de suspensão concentrada'
             '\n2. Para informações de como fazer, precauções e mais, leia a bula que vem junto ao produto no momento da compra.')
      
      nomePlanta = input('Qual o nome da plantação atacada? ')
      nomePraga = input('Qual o nome da praga? ')

      if nomePlanta == 'algodão' or nomePlanta == 'algodao' or nomePlanta == 'Algodão' or nomePlanta == 'Algodao':
            if nomePraga == 'Lagarta-do-cartucho' or nomePraga == 'lagarta-do-cartucho' or nomePraga == 'Lagarta-do-Cartucho' or nomePraga == 'Lagarta do cartucho' or nomePraga == 'lagarta do cartucho' or nomePraga == 'Lagarta do Cartucho':
                  print(f'\n{spodovir}')
            elif nomePraga == 'Percevejo-marrom' or nomePraga == 'percevejo-marrom' or nomePraga == 'Percevejo-Marrom' or nomePraga == 'Percevejo marrom' or nomePraga == 'percevejo marrom' or nomePraga == 'Percevejo Marrom':
                  print(f'\n{engeoPlenoS}'
                        '\nObservação: de 200 a 250 mL por hectare com no máximo 3 aplicações, uma a cada 7 dias; o volume da calda deve ser de 150 litros por hectare')
            elif nomePraga == 'Lagarta helicoverpa' or nomePraga == 'lagarta helicoverpa' or nomePraga == 'Lagarta Helicoverpa':
                  print(f'\n{bacillus}')
            elif nomePraga == 'Pulgão do algodoeiro' or nomePraga == 'Pulgao do algodoeiro' or nomePraga == 'pulgão do algodoeiro' or nomePraga == 'pulgao do algodoeiro' or nomePraga == 'Pulgão do Algodoeiro' or nomePraga == 'Pulgao do Algodoeiro':
                  print(f'\n{aug}'
                        '\nObservação: de 540 a 720 mL a cada 100kg com no máximo 1 aplicação; o volume da calda deve ser de 500mL a cada 100kg.')
            elif nomePraga == 'Tripes' or nomePraga == 'tripes':
                  print(f'{aug}'
                        '\nObservação: de 540 a 720 mL a cada 100kg com no máximo 1 aplicação; o volume da calda deve ser de 500mL a cada 100kg.')
            elif nomePraga == 'Cupim do montículo' or nomePraga == 'Cupim do monticulo' or nomePraga == 'cupim do montículo' or nomePraga == 'cupim do monticulo' or  nomePraga == 'Cupim do Montículo' or nomePraga == 'Cupim do Monticulo':       
                  print(f'{aug}'
                        '\nObservação: 720 mL a cada 100kg com no máximo 1 aplicação; o volume da calda deve ser de 500mL a cada 100kg.')
            else:
                  print('Essa praga não está em nosso sistema')
      
      elif nomePlanta == 'arroz' or nomePlanta == 'Arroz':
            if nomePraga == 'Lagarta-do-cartucho' or nomePraga == 'Lagarta do cartucho' or nomePraga == 'lagarta-do-cartucho' or nomePraga == 'lagarta do cartucho' or nomePraga == 'Lagarta-do-Cartucho' or nomePraga == 'Lagarta do Cartucho':
                  print (f'{spodovir}')
            elif nomePraga == 'Percevejo-do-arroz' or nomePraga == 'Percevejo do arroz' or nomePraga == 'percevejo-do-arroz' or nomePraga == 'percevejo do arroz' or nomePraga == 'Percevejo-do-Arroz' or nomePraga == 'Percevejo do Arroz':
                  print (f'{engeoPlenoS}'
                         '\nObservação: de 150 a 200 mL por hectare com no máximo 1 aplicação; o volume da calda deve ser de 200 litros por hectare')
            else:
                  print('Essa praga não está em nosso sistema')
      
      elif nomePlanta == 'aveia' or nomePlanta == 'Aveia':
            if nomePraga == 'Lagarta-do-cartucho' or nomePraga == 'Lagarta do cartucho' or nomePraga == 'lagarta-do-cartucho' or nomePraga == 'lagarta do cartucho' or nomePraga == 'Lagarta-do-Cartucho' or nomePraga == 'Lagarta do Cartucho':
                  print (f'{spodovir}')
            else:
                  print('Essa praga não está em nosso sistema')
      
      elif nomePlanta == 'cafe' or nomePlanta == 'café' or nomePlanta == 'Cafe' or nomePlanta == 'Café':
            if nomePraga == 'Lagarta helicoverpa' or nomePraga == 'lagarta helicoverpa' or nomePraga == 'Lagarta Helicoverpa':
                  print (f'{bacillus}')
            else:
                  print('Essa praga não está em nosso sistema')

      elif nomePlanta == 'Cana-de-açúcar' or nomePlanta == 'Cana-de-açucar' or nomePlanta == 'Cana-de-acucar' or nomePlanta == 'Cana-de-acúcar' or nomePlanta == 'Cana de açúcar' or nomePlanta == 'Cana de açucar' or nomePlanta == 'Cana de acucar' or nomePlanta == 'Cana de acúcar' or nomePlanta == 'cana-de-açúcar' or nomePlanta == 'cana-de-açucar' or nomePlanta == 'cana-de-acucar' or nomePlanta == 'cana-de-acúcar' or nomePlanta == 'cana de açúcar' or nomePlanta == 'cana de açucar' or nomePlanta == 'cana de acucar' or nomePlanta == 'cana de acúcar' or nomePlanta == 'Cana-de-Açúcar' or nomePlanta == 'Cana-de-Açucar' or nomePlanta == 'Cana-de-Acucar' or nomePlanta == 'Cana-de-Acúcar' or nomePlanta == 'Cana de Açúcar' or nomePlanta == 'Cana de Açucar' or nomePlanta == 'Cana de Acucar' or nomePlanta == 'Cana de Acúcar':
            if nomePraga == 'Lagarta-do-cartucho' or nomePraga == 'Lagarta do cartucho' or nomePraga == 'lagarta-do-cartucho' or nomePraga == 'lagarta do cartucho' or nomePraga == 'Lagarta-do-Cartucho' or nomePraga == 'Lagarta do Cartucho':
                  print(f'{spodovir}')
            else:
                  print('Essa praga não está em nosso sistema')
      
      elif nomePlanta == 'Feijao' or nomePlanta == 'Feijão' or nomePlanta == 'feijao' or nomePlanta == 'Feijão':
            if nomePraga == 'Lagarta-do-cartucho' or nomePraga == 'Lagarta do cartucho' or nomePraga == 'lagarta-do-cartucho' or nomePraga == 'lagarta do cartucho' or nomePraga == 'Lagarta-do-Cartucho' or nomePraga == 'Lagarta do Cartucho':
                  print(f'{spodovir}')
            elif nomePraga == 'Lagarta helicoverpa' or nomePraga == 'lagarta helicoverpa' or nomePraga == 'Lagarta Helicoverpa':
                  print (f'{bacillus}')
            else:
                  print('Essa praga não está em nosso sistema')
      
      elif nomePlanta == 'girassol' or nomePlanta == 'Girassol':
            if nomePraga == 'Percevejo-verde-pequeno' or nomePraga == 'Percevejo-Verde-Pequeno' or nomePraga == 'percevejo-verde-pequeno' or nomePraga == 'Percevejo verde pequeno' or nomePraga == 'Percevejo verde pequeno' or nomePraga == 'percevejo verde pequeno':
                  print(f'{engeoPlenoS}'
                        '\nObservação: de 300 a 400 mL por hectare com no máximo 2 aplicações, uma a cada 7 dias; o volume da calda deve ser de 150 litros por hectare')
            elif nomePraga == 'Percevejo-da-soja' or nomePraga == 'percevejo-da-soja' or nomePraga == 'Percevejo-da-Soja' or nomePraga == 'Percevejo da soja' or nomePraga == 'percevejo da soja' or nomePraga == 'Percevejo da Soja':
                  print(f'{engeoPlenoS}'
                        '\nObservação: de 300 a 400 mL por hectare com no máximo 2 aplicações, uma a cada 7 dias; o volume da calda deve ser de 150 litros por hectare')
            elif nomePraga == 'Percevejo-marrom' or nomePraga == 'percevejo-marrom' or nomePraga == 'Percevejo-Marrom' or nomePraga == 'Percevejo marrom' or nomePraga == 'percevejo marrom' or nomePraga == 'Percevejo Marrom':
                  print(f'{engeoPlenoS}'
                        '\nObservação: de 300 a 400 mL por hectare com no máximo 2 aplicações, uma a cada 7 dias; o volume da calda deve ser de 150 litros por hectare')
            else:
                  print('Essa praga não está em nosso sistema')
      
      elif nomePlanta == 'milho' or nomePlanta == 'Milho':
            if nomePraga == 'Percevejo-barriga-verde' or nomePraga == 'Percevejo-Barriga-Verde' or nomePraga == 'percevejo-barriga-verde' or nomePraga == 'Percevejo barriga verde' or nomePraga == 'Percevejo Barriga Verde' or nomePraga == 'percevejo-barriga-verde':
                  print(f'{engeoPlenoS}'
                        '\nObservação: de 150 a 250 mL por hectare com no máximo 2 aplicações, uma a cada 7 dias; o volume da calda deve ser de 200 litros por hectare')
            elif nomePraga == 'Lagarta helicoverpa' or nomePraga == 'lagarta helicoverpa' or nomePraga == 'Lagarta Helicoverpa':
                  print (f'{bacillus}')
            elif nomePraga == 'Cigarrinha do milho' or nomePraga == 'cigarrinha do milho' or nomePraga == 'Cigarrinha do Milho':
                  print (f'{aug}'
                         '\nObservação: 960 mL para cada 100kg com apenas uma aplicação; o volume da calda deve ser 500 mL para cada 100kg')
            elif nomePraga == 'Vaquinha verde amarela' or nomePraga == 'vaquinha verde amarela' or nomePraga == 'Vaquinha Verde Amarela':
                  print(f'{aug}'
                        '\nObservação: 960 mL para cada 100kg com apenas uma aplicação; o volume da calda deve ser 500 mL para cada 100kg')
            elif nomePraga == 'Cupim' or nomePraga == 'cupim':
                  print(f'{aug}'
                        '\nObservação: 300 mL para cada 100kg com apenas uma aplicação; o volume da calda deve ser 500 mL para cada 100kg')
            elif nomePraga == 'Pulgão' or nomePraga == 'Pulgao' or nomePraga == 'pulgão' or nomePraga == 'pulgao':
                  print(f'{aug}'
                        '\nObservação: 480 mL para cada 100kg com apenas uma aplicação; o volume da calda deve ser 500 mL para cada 100kg')
            else:
                  print('Essa praga não está em nosso sistema')
      
      elif nomePlanta == 'soja' or nomePlanta == 'Soja':
            if nomePraga == 'Lagarta-do-cartucho' or nomePraga == 'Lagarta do cartucho' or nomePraga == 'lagarta-do-cartucho' or nomePraga == 'lagarta do cartucho' or nomePraga == 'Lagarta-do-Cartucho' or nomePraga == 'Lagarta do Cartucho':
                  print(f'{spodovir}')
            elif nomePraga == 'Percevejo-marrom' or nomePraga == 'percevejo-marrom' or nomePraga == 'Percevejo-Marrom' or nomePraga == 'Percevejo marrom' or nomePraga == 'percevejo marrom' or nomePraga == 'Percevejo Marrom':
                  print(f'{engeoPlenoS}'
                        '\nObservação: 200 mL por hectare com no máximo 2 aplicações, uma a cada 7 dias; o volume da calda deve ser de 200 litros por hectare.')
            elif nomePraga == 'Percevejo-verde-pequeno' or nomePraga == 'Percevejo-Verde-Pequeno' or nomePraga == 'percevejo-verde-pequeno' or nomePraga == 'Percevejo verde pequeno' or nomePraga == 'Percevejo verde pequeno' or nomePraga == 'percevejo verde pequeno':
                  print(f'{engeoPlenoS}'
                        '\nObservação: de 150 a 180 mL por hectare com no máximo 2 aplicações, uma a cada 7 dias; o volume da calda deve ser de 200 litros por hectare')
            elif nomePraga == 'Percevejo-da-soja' or nomePraga == 'percevejo-da-soja' or nomePraga == 'Percevejo-da-Soja' or nomePraga == 'Percevejo da soja' or nomePraga == 'percevejo da soja' or nomePraga == 'Percevejo da Soja':
                  print(f'{engeoPlenoS}'
                        '\nObservação: de 150 a 180 mL por hectare com no máximo 2 aplicações, uma a cada 7 dias; o volume da calda deve ser de 200 litros por hectare')
            elif nomePraga == 'Lagarta helicoverpa' or nomePraga == 'lagarta helicoverpa' or nomePraga == 'Lagarta Helicoverpa':
                  print (f'{bacillus}')
            else:
                  print('Essa praga não está em nosso sistema')
            
      elif nomePlanta == 'trigo' or nomePlanta == 'Trigo':
            if nomePraga == 'Lagarta-do-cartucho' or nomePraga == 'Lagarta do cartucho' or nomePraga == 'lagarta-do-cartucho' or nomePraga == 'lagarta do cartucho' or nomePraga == 'Lagarta-do-Cartucho' or nomePraga == 'Lagarta do Cartucho':
                  print(f'{spodovir}')
            elif nomePraga == 'Percevejo-barriga-verde' or nomePraga == 'Percevejo-Barriga-Verde' or nomePraga == 'percevejo-barriga-verde' or nomePraga == 'Percevejo barriga verde' or nomePraga == 'Percevejo Barriga Verde' or nomePraga == 'percevejo-barriga-verde':
                  print(f'{engeoPlenoS}'
                        '\nObservação: 150 mL por hectare com no máximo 2 aplicações, uma a cada 7 dias; o volume da calda deve ser de 200 litros por hectare')
            else:
                  print('Essa praga não está em nosso sistema')
      else:
            print('Essa planta não está em nosso sistema')

#menu
opcaoMenu = 0
while opcaoMenu != 9:
      print('Seja bem vindo à PlanTech! No que podemos te ajudar?'
            '\n'
            '\n1. Desejo saber mais sobre a missão da PlanTech' #Luiz
            '\n2. Desejo saber sobre o funcionamento do drone' #Igor
            '\n3. Quero comprar um drone para detectar pragas' #Luiz
            '\n4. Identifiquei uma praga na plantação. O que faço agora?' #Rafa
            '\n5. Quem faz parte do projeto PlanTech?' #Douglas
            '\n6. Quero indicar um tratamento para uma praga' #Gustavo
            '\n7. Feedback' #Douglas
            '\n8. Outro' #Rafa
            '\n9. Encerrar') #Rafa
      opcaoMenu = int(input('Selecione uma das opções acima: '))

      match opcaoMenu:
#Opção 1 do menu: desejo saber mais sobre a missão da PlanTech ---- Colocar o primeiro e o último parágrafo do
#   arquivo "Descrição geral da solução 2"
            case 1:
                  print("-")
                  break

#Opção 2 do menu: desejo saber sobre o funcionamenento do drone ---- Colocar o segundo parágrafo do arquivo
#   "Descrição geral da solução 2"
            case 2:
                  print("-")
                  break

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
                  break

#Opção 4 do menu: identifiquei uma praga na plantação. O que faço agora? ---- Fazer um sistema com x tratamentos 
#   para pragas e x tratamentos que x plantações pode receber. A partir disso, fazer todas as combinações possíveis 
#   em comum. O usuário deve ter a opção de digitar o nome da praga e o nome da plantação atacada; Se colocar uma
#   praga ou plantação que não tenha no sistema, dizer que ainda não há esse no sistema
            case 4:
                  print(Indicacao())
                  break

#Opção 5 do menu: quem faz parte do projeto PlanTech? ---- Colocar o nome e RM de todos do grupo
            case 5:
                  print("-")
                  break

#Opção 6 do menu: quero indicar o tratamento para uma praga ---- Deixar com que o usuário informe o nome de uma 
#   praga, o tipo de plantação que essa praga ataca e o tipo de tratamento que essa praga combinada com essa 
#   plantação pode receber; Mostrar uma mensagem agradecendo e dizendo que essas informações vão para análise e
#   se estiver tudo correto, serão incluídas no sistema PlanTech
            case 6:
                  print("-")
                  break

#Opção 7 do menu: feedback ---- o usuário pode dar um feedback sobre a resolução de suas dúvidas, da performace do
#   sistema, sobre a indicação dos tratamentos para as plantações, sobre a usabilidade do projeto e experiência com 
#   o site
            case 7:
                  print("-")
                  break

#Opção 8 do menu: outro ---- Colocar pequenas informações e onde pode encontrá-las: se quer tirar dúvidas mais
#   específicas, entrar no nosso ChatBot; Se quer textos mais explicativos como agricultura sustentável, uso de
#   IA's generativas na produção, distribuição de alimentos pelo mundo, modelos de cultivos eficientes e calendário
#   de controle de pragas, entrar no site da PlanTech.
            case 8:
                  print("-")
                  break

#Opção 9 do menu: encerramento
            case 9:
                  print("-")
                  break