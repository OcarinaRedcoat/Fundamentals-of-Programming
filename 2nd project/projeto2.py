# ----------------------- 87699 -- Ricardo Caetano -------------------------------------------

# ----------------------------------Tipo Posicao ----------------------------------
# --- CONSTRUTORES
def faz_pos(l,c):
    '''Recebe: linha e uma coluna
    Devolve: posicao , tuplo de dois argumentos, (linha,coluna)'''
    if tipo(l) and tipo(c) :
        return (l,c)
    else:
        raise ValueError('faz_pos: argumentos errados')

def tipo(x):
    '''Recebe: um agrumento
    Devolve: se o argumento for do tipo inteiro e maior ou igual a zero, devolve True se nao devolve False'''
    if isinstance(x,int) and x >= 0:
        return True
    else:
        False
        
# --- SELETORES
def linha_pos(p):
    '''Recebe: uma posicao
    Devolve: a linha corresponde a essa posicao'''
    return p[0]

def coluna_pos(p):
    '''Recebe: uma posicao
    Devolve: a linha corresponde a essa posicao'''    
    return p[1]

# --- RECONHECEDORES
def e_pos(arg):
    '''Recebe: um agrumento
    Devolve: se o argumento for uma posicao, devolve True se nao devolve False'''    
    if isinstance(arg, tuple):
        if len(arg) == 2:
            if tipo(arg[0]) and tipo(arg[1]):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

# --- TESTES
def pos_iguais(p1,p2):
    '''Recebe: duas posicoes
    Devolve: True se as posicoes forem iguais, se forem diferentes devolve False'''
    return p1 == p2 
    
# ----------------------------------Tipo Chave ----------------------------------
# --- CONSTRUTORES
def e_letras(l):
    '''Funcao auxiliar,
    Recebe: um argumento
    Devolve: True se for letras (25 elementos nao repetidos), se nao devolve False'''
    l_aux = []
    for i in l:
        if i not in l_aux:
            l_aux += i
    if len(l_aux) != len(l) or len(l) != 25:
        return False
    else:
        return True
    
def e_mgc(mgc):
    '''Funcao auxiliar
    Recebe: um argumento
    Devolve: True se for uma mensagem geradora de chave valida (uma string de letras maiusculas), caso contrario devolve False'''
    mgc_aux = mgc
    if not isinstance(mgc,str):
        return False
    return  mgc_aux.upper() == mgc
       
def e_sentido(s):
    '''Funcao auxiliar
    Recebe: um argumento
    Devolve: True se o argumento dor 's' ou 'r' , False caso contrario'''
    return s == 'r' or s == 'c'

def e_pos_espiral(pos):
    '''Funcao auxiliar
    Recebe: posicao
    Devolve: True se a posicao for um dos quatro cantos da chave, False se nao for'''
    return pos_iguais(faz_pos(0,0),pos) or pos_iguais(faz_pos(0,4),pos) or pos_iguais(faz_pos(4,4),pos) or pos_iguais(faz_pos(4,0),pos)

def gera_chave_linhas(l,mgc):
    '''Recebe: letras e mensagem geracao de chave
    Devolve: chave segundo as regras de disposicao em linha 
    Regra: Recebe todos os elementos nao repetidos sem espaco da mgc, e depois junta os elementos da letras que nao sejam os mesmos,
    depois organiza os elementos em 5 listas de 5 elementos por ordem'''
    chave, chave_aux, cont, cont2 =[] ,[] , 0, 5
    if e_letras(l) == False or e_mgc(mgc) == False:
        raise ValueError('gera_chave_linhas: argumentos errados')
    
    for e in mgc:
        if e not in chave_aux and e != chr(32):
            chave_aux += e 
    for i in l:
        if i not in chave_aux:
            chave_aux += i
    for i in range(5) :
        chave += [chave_aux[cont:cont2]] 
        cont += 5
        cont2 += 5
    return (chave)
    
def del_elemento(x,l):
    '''Funcao auxiliar
    Remove o primeiro elemento de l numa range de x'''
    for i in range(x):
        del l[0]    

def gera_chave_espiral_aux(l,mgc):
    '''Funcao auxiliar
    Recebe: letras e mensagem geracao de chave
    Devolve: Chave que comeca na posicao (0,0) no sentido dos ponteiros do relogio segundo as regras da gera_chave_espiral'''
    chave_aux, chave = [], []
    for e in mgc:
        if e not in chave_aux and e != chr(32):
            chave_aux += e
    for i in l:
        if i not in chave_aux:
            chave_aux += i         
    for i in range(5):
        chave += chave_aux[i]
    chave = [chave]
    
    del_elemento(5,chave_aux)
        
    for i in range(4):
        chave += [[0,0,0,0, chave_aux[i]]]
    
    del_elemento(4,chave_aux)          
    
    for i in range(4):
        chave[4][3-i] = chave_aux[i]
        
    del_elemento(4,chave_aux) 
    
    for i in range(3):
        chave[3-i][0] = chave_aux[i]
    
    del_elemento(3,chave_aux)
    
    for i in range(3):
        chave[1][i+1] = chave_aux[i]
        
    del_elemento(3, chave_aux)
    
    for i in range(2):
        chave[i+2][3] = chave_aux[i]
        
    del_elemento(2,chave_aux)
    
    for i in range(2):
        chave[3][2-i] = chave_aux[i]
        
    del_elemento(2,chave_aux)
    
    for i in range(2):
        chave[2][i+1] = chave_aux[i]    
    return chave

def inverte_linhas(linha,chave):
    '''Funcao auxiliar
    Recebe: linha e chave
    Devolve: a respetiva linha da chave, mas invertida'''
    linha_aux = chave[linha]
    linha_invertida = linha_aux[::-1]
    return linha_invertida

def inverte_colunas(coluna,chave):
    '''Funcao auxiliar
    Recebe: coluna e chave
    Devolve: a respetiva coluna da chave, mas invertida'''    
    coluna_aux = []
    for i in range(5):
        coluna_aux += chave[i][coluna]
    coluna_invertida = coluna_aux[::-1]
    return coluna_invertida

def coluna_linha(coluna,chave):
    '''Funcao auxiliar
    Recebe: coluna e chave
    Devolve: a coluna de uma chave mas em forma de linha'''    
    linha = []
    for i in range(5):
        linha += chave[i][coluna]    
    return linha

def gera_chave_espiral(l,mgc,s,pos):
    '''Recebe: letras, mensagem geracao de chave, sentido e posicao
    Devolve: chave segundo as regras da geracao em espiral
    Regras: comeca na posicao pos, de seguida comeca no sentido horario ou contra horario (denpendento de r, horario, e c, contra horario),
    depois coloca todos os elementos de mgc nao repetidos e sem espacos numa coluna e faz rotacao de 90 graus quando chega ao fim ou a uma posicao ja ocupda
    de uma linha ou coluna'''
    if e_letras(l) == False or e_mgc(mgc) == False or e_sentido(s) == False or e_pos_espiral(pos) == False :
        raise ValueError('gera_chave_espiral: argumentos errados')   
    chave_aux = gera_chave_espiral_aux(l,mgc)
    chave = []
    if s == 'r':
        if pos_iguais(faz_pos(0,0),pos) == True:
            return gera_chave_espiral_aux(l,mgc)
        if pos_iguais(faz_pos(0,4),pos) == True:
            for i in range(5):
                chave += [inverte_colunas(i,chave_aux)]
            return chave
        if pos_iguais(faz_pos(4,4),pos) == True:
            for i in range(5):
                chave += [inverte_linhas(4-i,chave_aux)]
            return chave
        if pos_iguais(faz_pos(4,0),pos) == True:
            for i in range(5):
                chave += [coluna_linha(4-i,chave_aux)]
            return chave
    if s == 'c':
        if pos_iguais(faz_pos(0,0),pos) == True:
            for i in range(5):
                chave += [coluna_linha(i,chave_aux)]  
            return chave
        if pos_iguais(faz_pos(0,4),pos) == True:
            for i in range(5):
                chave += [inverte_linhas(i,chave_aux)] 
            return chave
        if pos_iguais(faz_pos(4,4),pos) == True:
            for i in range(5):
                chave += [inverte_colunas(4-i,chave_aux)] 
            return chave
        if pos_iguais(faz_pos(4,0),pos) == True:
            for i in range(5):
                chave += [chave_aux[4-i]]
            return chave
        
# --- SELETOR
def ref_chave(c,p):
    '''Recebe: chave e posicao
    Devolve: letra na respetiva posicao da chave c'''
    return c[linha_pos(p)][coluna_pos(p)]

# --- MODIFICADOR
def muda_chave(c,p,l):
    '''Recebe: chave, posicao, uma letra
    Devolve: a chave mas com a letra substituida na posicao p'''
    if isinstance(l,str) and len(l) != 1:
        raise ValueError('Argumentos invalidos')
    c[linha_pos(p)][coluna_pos(p)] = l
    return c

# --- RECONHECEDORES 
def e_chave(arg): 
    '''Recebe: argumento
    Devolve: True se o argumento for uma chave caso contrario devolve False'''
    x, arg_aux, verifica_upper= 0 , [] , ''
    for e in arg:
        for i in e:
            if i not in arg_aux:
                arg_aux += i
    for i in range(5):
        if len(arg[i]) !=5 or len(arg_aux) != 25 :
            return False
    for i in arg_aux:
        verifica_upper += i
    if verifica_upper.upper() != verifica_upper:
        return False
    return True
            
# --- TRANSFORMADORES  
def string_chave(c):
    '''Recebe: chave c
    Devolve: uma string com os elementos da chave c, com uma mudanca de linha a cada 5 elementos 
    e com um espaco entre cada elemento'''
    chave_aux, cont, cont2, str_chave =  '' , 0 , 10, ''
    for i in range(5):
        for e in range(5):
            chave_aux += c[i][e] + chr(32)
    for i in range(5):
        str_chave += chave_aux[cont:cont2] + '\n'
        cont += 10
        cont2 += 10
    return str_chave

# ----------------------------------FUNCOES A DEVOLVER ----------------------------------

def digramas(mens):
    '''Recebe: mensagem
    Devolve: e devolve a cadeia de caracteres correspondente aos digramas transformados de mens sem espacos
    Digramas tranformados:  Se as letras do digrama forem diferentes: o digrama mantem-se inalterado;
    Se as letras do digrama forem iguais: inserir um X na segunda posicao do digrama
    deslocando assim toda a mensagem uma posicao para a direita;
    Se o ultimo digrama estiver incompleto, por restar apenas uma letra (caso em que
    a mensagem tem um numero impar de letras): inserir um X na segunda letra do
    digrama.'''
    mens_aux, digrama = '', '' 
    for i in mens:
        if i != chr(32):
            mens_aux += i
    for i in range(0, (len(mens_aux)-1), 2):
        if mens_aux[i] == mens_aux[i+1]:
            digrama += mens_aux[i] + 'X' + mens_aux[i+1]
        else:
            digrama += mens_aux[i] + mens_aux[i+1]
    digrama += mens_aux[-1]

    if len(digrama)%2 != 0:
        digrama += 'X'
        
    if digrama[len(digrama)-1] == digrama[len(digrama)-2]:
        digrama = digrama[:len(digrama)-1] + 'X'
    elif digrama[len(digrama)-2] == digrama[len(digrama)-3] and digrama[len(digrama)-1] == 'X':
        digrama = digrama[:len(digrama)-2]
    
    return digrama

def check_pos(l,chave):
    '''Funcao auxiliar
    Recebe: letra e uma chave
    Devolve: a posicao da letra na chave'''
    for i in range(len(chave)):
        for e in range(len(chave[i])):
            if chave[i][e] == l:
                return faz_pos(i,e)
            
def codifica_aux(cod,chave):
    '''Funcao auxiliar
    Recebe: cod (tuplo de 2 posicoes) e chave
    Devolve: uma string com as letras das posicoes corresponentes da chave'''
    return chave[cod[0][0]][cod[0][1]] + chave[cod[1][0]][cod[1][1]]

def figura(digrm,chave):
    '''Recebe: digrama e uma chave
    Devolve: um tuplo de 3 elementos da forma (fig, pos1, pos2)'''
    pos1 = check_pos(digrm[0],chave)
    pos2 = check_pos(digrm[1],chave)
    if linha_pos(pos1) == linha_pos(pos2):
        return ('l',pos1,pos2)
    elif coluna_pos(pos1) == coluna_pos(pos2):
        return ('c',pos1,pos2)
    else:
        return ('r',pos1,pos2)
    
def codifica_l(pos1,pos2,inc):
    '''Recebe: posicao1 posicao2 e um inc (que pode ser 1 ou -1) pos1 e pos2 estao na mesma linha
    Devolve: A funcao devolve um tuplo de 2 posicoes que correspondem as posicoes das letras do digrama encriptado/desencriptado.'''
    if inc == 1:
        if coluna_pos(pos1) == 4:
            pos1_final = faz_pos(linha_pos(pos1),0)
        else:
            pos1_final = faz_pos(linha_pos(pos1),coluna_pos(pos1)+1) 
        if coluna_pos(pos2) == 4:
            pos2_final = faz_pos(linha_pos(pos2),0)
        else:
            pos2_final = faz_pos(linha_pos(pos2),coluna_pos(pos2)+1)
    if inc == -1:
        if coluna_pos(pos1) == 0:
            pos1_final = faz_pos(linha_pos(pos1),4)
        else:
            pos1_final = faz_pos(linha_pos(pos1),coluna_pos(pos1)-1)
        if coluna_pos(pos2) == 0:
            pos2_final = faz_pos(linha_pos(pos2),4)
        else:
            pos2_final = faz_pos(linha_pos(pos2),coluna_pos(pos2)-1)
    return (pos1_final,pos2_final)

def codifica_c(pos1,pos2,inc):
    '''Recebe: posicao1 posicao2 e um inc (que pode ser 1 ou -1) pos1 e pos2 estao na mesma coluna
    Devolve: A funcao devolve um tuplo de 2 posicoes que correspondem as posicoes das letras do digrama encriptado/desencriptado'''    
    if inc == 1:
        if linha_pos(pos1) == 4:
            pos1_final = faz_pos(0,coluna_pos(pos1))
        else:
            pos1_final = faz_pos(linha_pos(pos1)+1,coluna_pos(pos1))
        if linha_pos(pos2) == 4:
            pos2_final = faz_pos(0,pos2[1])
        else:
            pos2_final = faz_pos(linha_pos(pos2)+1,coluna_pos(pos2))
    if inc == -1:
        if linha_pos(pos1) == 0:
            pos1_final = faz_pos(4,coluna_pos(pos1))
        else:
            pos1_final = faz_pos(linha_pos(pos1)-1,coluna_pos(pos1))
        if linha_pos(pos2) == 0:
            pos2_final = faz_pos(4,coluna_pos(pos2))
        else:
            pos2_final = faz_pos(linha_pos(pos2)-1,coluna_pos(pos2))
    return (pos1_final,pos2_final)

def codifica_r(pos1,pos2):
    '''Recebe: posicao1 posicao2 e um inc (que pode ser 1 ou -1) pos1 e pos2 em diferentes linhas e colunas
    Devolve: A funcao devolve um tuplo de 2 posicoes que correspondem as posicoes das letras do digrama encriptado/desencriptado'''     
    return (faz_pos(linha_pos(pos1),coluna_pos(pos2)),faz_pos(linha_pos(pos2),coluna_pos(pos1)))
    
def codifica_digrama(digrm,chave,inc):
    '''Revebe: digrama, chave e um incrementador
    Devolve: digrama codificado/descodificado'''
    aux = figura(digrm, chave)
    if aux[0] == 'l':
        cod = codifica_l(aux[1], aux[2], inc)
    if aux[0] == 'c':
        cod = codifica_c(aux[1], aux[2], inc)
    if aux[0] == 'r':
        cod = codifica_r(aux[1], aux[2])
    return codifica_aux(cod,chave)
    
    
def codifica(mens,chave,inc):
    '''Revebe: mensagem, chave e um incrementador
    Devolve: mensagem codificada/descodificada'''
    mens, cod = digramas(mens), ''
    for i in range(0,len(mens),2):
        cod += codifica_digrama(mens[i:i+2], chave, inc)
    return cod