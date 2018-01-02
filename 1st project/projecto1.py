#-------> Ricardo Caetano, 87699



#---------------------------Versao Simplificada---------------------------------


from math import sqrt

def gera_chave1(letras):
    '''A funcao devolve um tuplo de 5 tuplos de caracteres com 5 elementos.'''    
    return ((letras[0:5]) , (letras[5:10]) , (letras[10:15]) ,\
        (letras[15:20]) , (letras[20:25]))


def obtem_codigo1(car,chave):
    '''A funcao devolve 2 caracteres, correspondendo ao \
    codigo do caracter de acordo com a chave.'''
    for i in range(len(chave)): 
        #neste ciclo obtem se o indice do tuplo onde o caracter se encontra
        for e in range(len(chave[i])): 
            #neste ciclo obtem se em que indice o caracter se emcontra no subtuplo
            if chave[i][e] == car:
                return str(i)+ str(e)
            
def codifica1(cad,chave):
    '''A funcao utiliza a funcao obtem_codigo1 e devolve uma cadeia de \
    caracteres correspondente a encriptacao de cad.'''
    cad_car_encript=''
    for i in cad:
        cad_car_encript+=obtem_codigo1(i,chave)
    return cad_car_encript

            
def obtem_car1(cod,chave):
    '''A funcao devolve caractere correspondente ao codigo. '''
    cod = int(cod)
    i , e = cod // 10 , cod % 10    
    #ao fazer a divisao inteira e o resto da divisao inteira por 10 sabemos os indices do tuploe do elemento no subtuplo
    caracter = chave[i][e]
    return caracter


def descodifica1(cad_codificada,chave):
    '''A funcao utiliza a funcao obtem_car1 e devolve uma cadeia de \
    caracteres correspondentes a mensagem original.'''
    cad_car_origin=''
    for i in range(0,len(cad_codificada)-1,2) :
        cad_car_origin+=obtem_car1(cad_codificada[i:(i+2)],chave)
        #vai de dois em dois para os caracteres poderem ser avaliados aos parem em obtem_car1
    return cad_car_origin


#-------------------------------Versao Final------------------------------------  



def gera_chave2(letras):
    '''A funcao devolve um tuplo de tuplos  '''
    comprimento, cont, chave_final, cont1 = sqrt(len(letras)), 0, (), 1
    #cont e cont1 : contadores
    
    if (comprimento % 10 != 0 and (comprimento*10%10) != 0):  #obter o numero de tuplos 
        num_tuplos = ( int(comprimento)+1)
    else:
        num_tuplos =  int(comprimento)
    num_elemntos = len(letras)/num_tuplos
    
    if (num_elemntos%10 != 0 ) and (num_elemntos*10%10): #obter o numero de elementos em cada tuplo
        num_elemntos = ((int(num_elemntos)+1))
    else:
        num_elemntos = int(num_elemntos)
        
    while num_tuplos >= cont1 :
        # o contador faz com que os elemtos fiquem organizados no numero exato dee tuplos calculados no primeiro if
        chave_final = chave_final + (letras[cont:(cont+num_elemntos)],)
        cont+=num_elemntos
        cont1 +=1
    return chave_final    
    
    
    
    
def obtem_codigo2(car,chave):
    '''A funcao devolve  uma cadeia de 2 caracteres, correspondendo\
    ao codigo do caracter de acordo com a chave. Se o caracter nao pertencer \
    a chave a funcao devolve XX.'''
    for i in range(len(chave)):
        #neste ciclo obtem se o indice do tuplo onde o caracter se encontra
            for e in range(len(chave[i])):
                #neste ciclo obtem se em que indice o caracter se emcontra no subtuplo
                if chave[i][e] == car:
                    return str(i)+ str(e)
    return 'XX'


def codifica2(cad,chave):
    '''A funcao utiliza a funcao obtem_codigo2 e devolve uma cadeia\
    de caracteres, correspondendo a encriptacao de cad.'''
    cad_car_encript=''
    for i in cad:
        cad_car_encript+=obtem_codigo2(i,chave) 
    return cad_car_encript

def obtem_car2(cod,chave):
    '''A funcao recebe cad, uma cadeia de 2 digitos ou XX, depois a \
    funcao devolve o caracter correspondente aos dois digitos,\
    no caso de ser XX devolve ?. '''
    if str(cod) == 'XX':
        return '?'

    cod = int(cod)
    i , e = cod // 10 , cod % 10    
    # ao fazer a divisao inteira e o resto da divisao inteira por 10 sabemos os indices do tuploe do elemento no subtuplo
    caracter = chave[i][e]
    return caracter
    
def descodifica2(cad_codificada,chave):
    '''A funcao utilia a funcao obtem_car2 e devolve uma cadeia de caracteres,\
    correspondendo a mensagem original.'''
    cad_car_origin = ''
    for i in range(0,len(cad_codificada)-1,2) :
        cad_car_origin+=obtem_car2(cad_codificada[i:(i+2)],chave)
        #vai de dois em dois para os caracteres poderem ser avaliados aos parem em obtem_car2
    return cad_car_origin     