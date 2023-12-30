"""
input <- senha
output <- senha forte

Passos do Algoritmo de Fortalecimento de Senha

1 - cada caracter da senha que seja letra e' transformado em upper ou lower case aleatoriamente
2 - e' gerado duas strings aleatorias: 1 string com caracteres especiais e uma string com digitos
3 - pega-se o primeiro e o ultimo caracter
4 - a string da senha é invertida em orientacao
5 - dividimos a senha original em 2 partes de modo aleatório
6 - repetimos 1 vez em cada uma das 2 partes obtidas da senha original o primeiro e o ultimo caracter
7 - anexamos no inicio em cada parte da senha original o caracter 's'
8 - anexamos no fim em cada parte da senha original o caracter 'S'
9 - selecionamos 2 caracteres especiais aleatorios usados na string de caracteres especiais
10 - criamos uma string com esses 2 caracteres dois a dois, ou seja, de modo alternado
11 - anexamos a essa string no inicio e no final um numero aleatorio de numeros aleatorios no inicio e no final dessa string
12 - colocamos essa string entre as 2 partes obtidas da senha original e chamamos de raiz
13 - definimos a nova senha fortalecida nessa 4 opcoes, selecionadas aleatoriamente:
    1) primeiro_caracter+string_ch_especiais+raiz+string_ch_digitos+ultimo_caracter
    2) ultimo_caracter+string_ch_especiais+raiz+string_ch_digitos+primeiro_caracter
    3) primeiro_caracter+string_ch_digitos+raiz+string_ch_especiais+ultimo_caracter
    4) ultimo_caracter+string_ch_digitos+raiz+string_ch_especiais+primeiro_caracter
"""

import random

# lista de caracteres
chars = ['!','@','#','$','%','&','*','-','_','+','=','?','|','<','>',':','.',',',';','/','\\','\"','\'','(',')','[',']','{','}','~','^']
digitos = ['0','1','2','3','4','5','6','7','8','9']
letras_lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letras_upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# gera uma cadeia de caracteres aleatoria a partir de uma lista de caracteres
def rand_string(n,v):
    s=""
    for i in range(0,n):
        r = random.randint(0,len(v)-1)
        s += v[r]
    return list(s)

# torna um caracter upper ou lower case aleatoriamente
def upper_or_lower(s,size):
    for i in range(0,size):
        if s[i].isalpha():
            r=random.randint(0,1)
            if r==0:
                s[i]=s[i].lower()
            else:
                s[i]=s[i].upper()

# reverte a senha, divide em 2 partes a senha e retorna o primeiro e ultimo elemento
def mod_password(s):
    size=len(s)
    nova_senha = list(senha[::-1])
    upper_or_lower(nova_senha,size)
    first, last = nova_senha[0], nova_senha[size-1]
    r=random.randint(1,size-2)
    s1, s2 = nova_senha[0:r], nova_senha[r:size]

    return first,last,s1,s2

# cria a string que fica no meio entre as 2 partes da string obtida pela senha original
def create_middle(sd,sc):
    r = random.randint(1,7)
    r1 = random.randint(0,len(sc)-1)
    r2 = random.randint(0,len(sc)-1)
    n1 = int((random.random())*(10**r))
    n2 = int((random.random())*(10**(8-r)))
    p=[]
    for i in range(0,8):
        if i%2==0:
            p+=[sc[r1]]
        else:
            p+=[sc[r2]]
    p=list(str(n1))+p+list(str(n2))

    return p

# obtem a cadeia de caracteres de digitos e de caracteres especiais
def create_corner():
    r = random.randint(1,7)
    sd = rand_string(r,digitos)
    sc = rand_string(8-r,chars)
    return sd,sc

# ordena as partes para a criar a nova senha
def create_new_password(first,last,sd,sc,p,piece_word1,piece_word2):
    r=random.randint(1,4)
    s = piece_word1+p+piece_word2
    if r==1:
        nova_senha = [first]+sc+s+sd+[last]
    elif r==2:
        nova_senha = [last]+sc+s+sd+[first]
    elif r==3:
        nova_senha = [first]+sd+s+sc+[last]
    elif r==4:
        nova_senha = [last]+sd+s+sc+[first]

    return nova_senha


## input
senha = str(input("senha = "))

## calc
first,last,s1,s2 = mod_password(senha)
sd,sc = create_corner()
p = create_middle(sd,sc)
piece_word1=['s']+[s1[0]]+s1+[s1[len(s1)-1]]+['S']
piece_word2=['s']+[s2[0]]+s2+[s2[len(s2)-1]]+['S']
nova_senha = create_new_password(first,last,sd,sc,p,piece_word1,piece_word2)    
nova_senha=''.join(nova_senha)

## output
print("------------------------------------------------")
print("primeiro caracter-> "+"'"+first+"'")
print("ultimo caracter -> "+"'"+last+"'")
print("string do meio -> "+"'"+''.join(p)+"'")
print("string de caracteres especiais -> "+"'"+''.join(sc)+"'")
print("string de digitos -> "+"'"+''.join(sd)+"'")
print("parte 1 da senha original -> "+"'"+''.join(piece_word1)+"'")
print("parte 2 da senha original -> "+"'"+''.join(piece_word2)+"'")
print("------------------------------------------------")
print("senha original -> "+senha)
print("nova senha -> "+nova_senha)
print("tamanho da senha original -> "+str(len(senha)))
print("tamanho da nova senha -> "+str(len(nova_senha)))
print("------------------------------------------------")
