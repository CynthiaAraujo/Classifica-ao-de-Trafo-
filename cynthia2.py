import sys

def data(num_comp, msg,data_fab,recond,fase,pot,elo,clientes,classifi,teste,aceitou,tap,primario,secundario,tensao_cliente,vazamento):
    texto = open(f'{num_comp}.txt','a')
    if msg != None:
        texto.write(f'{msg}\n')
    texto.write(f'A data de fabricação é {data_fab}\n')
    texto.write(f'{recond}\n')
    texto.write(f'{fase}\n')
    texto.write(f'{pot}\n')
    texto.write(f'{elo}\n')
    texto.write(f'{clientes}\n')
    texto.write(f'{classifi}\n')
    texto.write(f'{teste}\n')
    texto.write(f'{aceitou}\n')
    if tap != None:
         texto.write(f'{tap}\n')
    if primario != None:
        texto.write(f'{primario}\n')
    if secundario != None:
        texto.write(f'{secundario}\n')
    if tensao_cliente != None:
        texto.write(f'{tensao_cliente}\n')
    if vazamento != None:
        texto.write(f'{vazamento}\n')
    texto.write('\n')
    texto.close()

retirou_defeito=''
teste=''
trafo_aceitou=''
teste=''
trafo_aceitou=''
teste_vazio=''
bt=''
pararaio=''
elo_correto=''
primario=''
secundario=''
tap=''
normalizou=''
funcionamento=''

print('---------------- Ocorrência de Trafo --------')
num_comp = input('Qual o número do componente? ')
fase = input('O trafo é monofásico, bifásico ou trifásico? (m, b ou t?) ').lower()
while(fase!='m' and fase!='b' and fase!='t'):
    print("Digite M se o trafo for monofásico, B se fo bifásico ou T se for trifásico!")
    fase = input('O trafo é monofásico, bifásico ou trifásico? (m, b ou t?) ').lower()
pot = input('Qual a potência do transformador? ')

while(True):
    estavazando = input('O trafo está vazando óleo? (s ou n?) ').lower()
    
    if estavazando == 's':
        
        while(True):            
            funcionamento = input('O trafo está funcionando normalmente? (s ou n?) ').lower()

            if funcionamento == 's':
                vazamento = input('Onde é o vazamento do óleo? (t = tampa, p = primário, s = secundário, r = radiador, c = carcaça)? ').lower()
                while ('t' != vazamento != 'p' and 's' != vazamento != 'r' and vazamento != 'c'):
                    print("Digite t se o vazamento for na tampa, p se for no primário, s se for no secundário, r se for no radiador ou c se for na carcaça!")
                    vazamento = input('Onde é o vazamento do óleo? (t = tampa, p = primário, s = secundário, r = radiador, c = carcaça)? ').lower()
                
                intensidade = input('Qual a intensidade do vazamento? (s = Suado, p = Pouco ou i = Intenso)? ').lower()
                while ('s' != intensidade != 'p' and intensidade != 'i'):
                    print("Digite S se o trafo estiver suado, P se o vazamento for pouco ou I se o vazamento for intenso!")
                    intensidade = input('Qual a intensidade do vazamento? (s = Suado, p = Pouco ou i = Intenso)? ').lower()
                
                while(True):
                    percorreu = input('Já Percorreu a rede? (s ou n?) ').lower()
                    
                    if percorreu == 's':
                        
                        while (True):
                            existe_defeito = input('Existe defeito na rede? (s ou n?) ').lower()

                            if existe_defeito == 's':
                                defeito = input('Qual é o defeito? ')
                                
                                while(True):
                                    retirou_defeito = input('O defeito foi retirado? (s ou n?) ').lower()

                                    if retirou_defeito == 's':
                                       
                                        while(True):
                                            teste = input('Fez o teste substituindo o elo? (s ou n?) ').lower()

                                            if teste == 's':
                                                while(True):
                                                    trafo_aceitou = input('O trafo aceitou o teste? (s ou n?) ').lower()

                                                    if trafo_aceitou == 's':
                                                        msg = 'O transformador está avariado!'
                                                        break

                                                    elif trafo_aceitou == 'n':
                                                        msg = 'O transformador está queimado!'
                                                        break

                                                    else:
                                                        print('Digite S se o trafo aceitou o teste ou N se não aceitou')
                                                break
                                            elif teste == 'n':
                                                print('Faça o teste!')

                                            else:
                                                print('Digite S se fez o teste substituindo o elo ou N se não fez ainda!') 
                                        break

                                    elif retirou_defeito == 'n':
                                        print('Retire o defeito!')

                                    else:
                                        print('Digite S se o defeito tiver sido retirado da rede ou N caso contrário!')      
                                
                                break

                            elif existe_defeito == 'n':
                               
                                while (True):
                                    teste = input('Fez o teste substituindo o elo? (s ou n?) ').lower()

                                    if teste =='s':
                                        
                                        while(True):
                                            trafo_aceitou = input('O trafo aceitou o teste? (s ou n?) ').lower()

                                            if trafo_aceitou == 's':
                                                msg = 'O transformador está avariado!'
                                                break

                                            elif trafo_aceitou == 'n':
                                                msg = 'O transformador está queimado!'
                                                break

                                            else:
                                                print('Digite S se o trafo aceitou o teste ou N se não aceitou')

                                        break

                                    elif teste == 'n':
                                        print('Faça o teste!')

                                    else:
                                        print('Digite S se fez o teste substituindo o elo ou N se não fez ainda!')

                                break

                            else:
                                  print("Digite S se existir algum defeito na rede ou N se não existir!")

                        break

                    elif percorreu == 'n':
                        print('Percorra a rede!')

                    else:
                        print("Digite S se a rede já estiver sido percorrida ou N caso contrário!")
                break
            elif funcionamento == 'n':

                while(True):
                    percorreu = input('Já Percorreu a rede? (s ou n?) ').lower()
                    
                    if percorreu == 's':
                        
                        while (True):
                            existe_defeito = input('Existe defeito na rede? (s ou n?) ').lower()

                            if existe_defeito == 's':
                                defeito = input('Qual é o defeito? ')
                                
                                while(True):
                                    retirou_defeito = input('O defeito foi retirado? (s ou n?) ').lower()

                                    if retirou_defeito == 's':
                                        msg = 'O trafo está avariado!'
                                        break

                                    elif retirou_defeito == 'n':
                                        print('Retire o defeito!')

                                    else:
                                        print('Digite S se o defeito tiver sido retirado da rede ou N caso contrário!')      
                                
                                break

                            elif existe_defeito == 'n':
                                msg = 'O trafo está avariado!'
                                break

                            else:
                                  print("Digite S se existir algum defeito na rede ou N se não existir!")

                        break

                    elif percorreu == 'n':
                        print('Percorra a rede!')

                    else:
                        print("Digite S se a rede já estiver sido percorrida ou N caso contrário!")    

                break
            else:
                print("Digite S se o trafo estiver funcionando normalmente ou N se não estiver!")

        break

    elif estavazando == 'n':
        while(True):
            percorreu = input('Já Percorreu a rede? (s ou n?) ').lower()
                    
            if percorreu == 's':
                        
                while (True):
                    existe_defeito = input('Existe defeito na rede? (s ou n?) ').lower()

                    if existe_defeito == 's':
                        defeito = input('Qual é o defeito? ')
                                
                        while(True):
                            retirou_defeito = input('O defeito foi retirado? (s ou n?) ').lower()

                            if retirou_defeito == 's':
                                while(True):
                                    teste_vazio = input('Fez o teste a vazio? (s ou n?)').lower()

                                    if teste_vazio == 's':
                                        while(True):
                                            bt = input("Desconectou a BT? (s ou n?) ").lower()

                                            if bt =='s':
                                                while(True):
                                                    pararaio = input('Desconectou o para-raio? (s ou n?) ').lower()

                                                    if pararaio == 's':
                                                        while(True):
                                                            elo_correto = input('Utilizou o elo correto? (s ou n?) ').lower()

                                                            if elo_correto == 's':
                                                                while (True):
                                                                    trafo_aceitou = input('O trafo aceitou o teste a vazio? (s ou n?) ').lower()

                                                                    if trafo_aceitou == 's':
                                                                        primario = input('Qual a tensão no primário? ')

                                                                        while(True):
                                                                            secundario = input('A tensão no secundário está normal? (s ou n?) ').lower()

                                                                            if secundario == 's':
                                                                                msg = 'O trafo não está avariado! Procure o defeito!'
                                                                                break

                                                                            elif secundario == 'n':
                                                                                if fase == 'm' or fase == 'b':
                                                                                    while(True):
                                                                                        tap = input('Tem a opção de alterar o TAP? (s ou n?) ').lower()
                                                                                        if tap == 's':
                                                                                            while(True):
                                                                                                normalizou = input('Altere! O trafo normalizou? (s ou n?) ').lower()
                                                                                                if normalizou == 's':
                                                                                                    msg = 'O trafo não está avariado! Procure o defeito!'
                                                                                                    break

                                                                                                elif normalizou == 'n':
                                                                                                    msg = 'O trafo está avariado!'
                                                                                                    break

                                                                                                else:
                                                                                                    print('Digite S se o trafo normalizou ou N caso contrário!')

                                                                                            break
                                                                                        
                                                                                        elif tap == 'n':
                                                                                            msg = 'O trafo está avariado!'
                                                                                            break

                                                                                        else:
                                                                                            print('Digite S de tiver a opção de alterar o TAP ou N se não tiver!')

                                                                                elif fase == 't':
                                                                                    msg = 'O trafo está avariado!'
                                                                                    
                                                                                break

                                                                            else:
                                                                                print('Digite S se a tensão no secundário estiver normal ou N caso contrário!')

                                                                        break

                                                                    elif trafo_aceitou == 'n':
                                                                        msg = 'O trafo está queimado!'
                                                                        break

                                                                    else:
                                                                        print('Digite S se o trafo aceitou o teste a vazio ou N se não aceitou!')

                                                                break

                                                            elif elo_correto =='n':
                                                                print("Utilize o elo correto!")
                                                            
                                                            else:
                                                                print('Digite S se o elo correto foi utilizado ou N se não foi!')

                                                        break

                                                    elif pararaio == 'n':
                                                        print('Desconecte o para-raio!')

                                                    else:
                                                        print('Digite S se o para-raio tiver sido desconectado ou N caso contrário!')

                                                break

                                            elif bt == 'n':
                                                print("Desconecte a BT!")

                                            else:
                                                print("Digite S se a BT tiver sido desconectada ou N caso contrário!")

                                        break

                                    elif teste_vazio == 'n':
                                        print('Faça o teste a vazio!')

                                    else:
                                        print('Digite S se o teste a vazio tiver sido feito ou N caso contrário!')

                                break
                            elif retirou_defeito == 'n':
                                msg = 'Acione a manutenção!'
                                break
                            else:
                                print('Digite S se o defeito foi retirado ou N caso contrário!')
                        break
                    elif existe_defeito == 'n':
                        while(True):
                            teste_vazio = input('Fez o teste a vazio? (s ou n?)').lower()

                            if teste_vazio == 's':
                                while(True):
                                    bt = input("Desconectou a BT? (s ou n?) ").lower()

                                    if bt =='s':
                                        while(True):
                                            pararaio = input('Desconectou o para-raio? (s ou n?) ').lower()

                                            if pararaio == 's':
                                                while(True):
                                                    elo_correto = input('Utilizou o elo correto? (s ou n?) ').lower()

                                                    if elo_correto == 's':
                                                        while (True):
                                                            trafo_aceitou = input('O trafo aceitou o teste a vazio? (s ou n?) ').lower()

                                                            if trafo_aceitou == 's':
                                                                primario = input('Tem tensao no Primário? ')

                                                                while(True):
                                                                    secundario = input('A tensão no secundário está normal? (s ou n?) ').lower()

                                                                    if secundario == 's':
                                                                        msg = 'O trafo não está avariado! Procure o defeito!'
                                                                        break

                                                                    elif secundario == 'n':
                                                                        if fase == 'm' or fase == 'b':
                                                                            while(True):
                                                                                tap = input('Tem a opção de alterar o TAP? (s ou n?) ').lower()
                                                                                if tap == 's':
                                                                                    while(True):
                                                                                        normalizou = input('Altere! O trafo normalizou? (s ou n?) ').lower()
                                                                                        if normalizou == 's':
                                                                                            msg = 'O trafo não está avariado! Procure o defeito!'
                                                                                            break

                                                                                        elif normalizou == 'n':
                                                                                            msg = 'O trafo está avariado!'
                                                                                            break

                                                                                        else:
                                                                                            print('Digite S se o trafo normalizou ou N caso contrário!')

                                                                                    break
                                                                                
                                                                                elif tap == 'n':
                                                                                    msg = 'O trafo está avariado!'
                                                                                    break

                                                                                else:
                                                                                    print('Digite S de tiver a opção de alterar o TAP ou N se não tiver!')

                                                                        elif fase == 't':
                                                                            msg = 'O trafo está avariado!'
                                                                            
                                                                        break

                                                                    else:
                                                                        print('Digite S se a tensão no secundário estiver normal ou N caso contrário!')

                                                                break

                                                            elif trafo_aceitou == 'n':
                                                                msg = 'O trafo está queimado!'
                                                                break

                                                            else:
                                                                print('Digite S se o trafo aceitou o teste a vazio ou N se não aceitou!')

                                                        break

                                                    elif elo_correto =='n':
                                                        print("Utilize o elo correto!")
                                                    
                                                    else:
                                                        print('Digite S se o elo correto foi utilizado ou N se não foi!')

                                                break

                                            elif pararaio == 'n':
                                                print('Desconecte o para-raio!')

                                            else:
                                                print('Digite S se o para-raio tiver sido desconectado ou N caso contrário!')

                                        break

                                    elif bt == 'n':
                                        print("Desconecte a BT!")

                                    else:
                                        print("Digite S se a BT tiver sido desconectada ou N caso contrário!")

                                break

                            elif teste_vazio == 'n':
                                print('Faça o teste a vazio!')

                            else:
                                print('Digite S se o teste a vazio tiver sido feito ou N caso contrário!')

                        break

                    else:
                        print('Digite S se existe defeito na rede ou N se não existe!')
                break

            elif percorreu == 'n':
                print('Percorra a rede!')

            else:
                print('Digite S se já tiver percorrido a rede ou N se ainda não tiver!')
        break

    else:
        print("Digite S se o trafo estiver vazando óleo ou N se não estiver!")
print(msg)

acesso = input('Tem acesso ao local? (s ou n?) ').lower()
while ('s' != acesso != 'n'):
    print("Digite S se tem acesso ao local ou N caso contrário!")
    acesso = input('Tem acesso ao local? (s ou n?) ').lower()

estrutura = input('O trafo está na mesma estrutura da chave? (s ou n?) ').lower()
while ('s' != estrutura != 'n'):
    print("Digite S se O trafo estiver na mesma estrutura da chave ou N caso contrário!")
    estrutura = input('O trafo está na mesma estrutura da chave? (s ou n?) ').lower()

glv = input('Tem GLV? (s ou n?) ').lower()
while ('s' != glv != 'n'):
    print("Digite S se tem GLV ou N se não tem GLV!")
    glv = input('Tem GLV? (s ou n?) ').lower()

ss = input('Qual o número da SS? ')

ocorrencia = input('Qual o número da Ocorrência? ')

clientes = input('Qual a quantidade de clientes? ')

local = input ('Qual é o local?')

ponto_refe = input ('Qual é o ponto de referencias?')


#data(num_comp, msg,data_fab,recond,fase,pot,elo,clientes,classifi,teste,aceitou,tap,primario,secundario,tensao_cliente,vazamento)
print(msg,num_comp, fase, pot, estavazando,funcionamento,percorreu,existe_defeito,retirou_defeito,teste,trafo_aceitou,teste_vazio,bt,pararaio,elo_correto,primario,secundario,tap,normalizou,acesso,estrutura,glv,ss,ocorrencia,clientes)