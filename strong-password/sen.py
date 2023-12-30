import random

# lista de caracteres
chars = ['!','@','#','$','%','&','*','-','_','+','=','?','|','<','>',':','.',',',';','/','\\','\"','\'','(',')','[',']','{','}','~','^']
digitos = ['0','1','2','3','4','5','6','7','8','9']
letras_lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letras_upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
vogais = ['a','e','i','o','u','A','E','I','O','U']


dic = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}


def substuicao(c1,c,c2):
    x='$'
    if (c in letras_upper) or (c in letras_lower):
        if c1.isalpha() and c2.isalpha():
            d=random.randint(0,1)
            if d==0:
                r=random.randint(0,(len(chars)-1))
                x=chars[r]
            else:
                r=random.randint(0,(len(digitos)-1))
                x=digitos[r]
        elif c1.isalpha() and (c2 in digitos):
            x=letras_lower[(dic[c]+3)%26]
        elif c1.isalpha() and (c2 in chars):
            x=letras_upper[(dic[c]+3)%26]
        elif (c1 in digitos) and c2.isalpha():
            x=letras_upper[(dic[c]+13)%26]
        elif (c1 in digitos) and (c2 in digitos):
            x=letras_upper[25-dic[c]]
        elif (c1 in digitos) and (c2 in chars):
            x=letras_lower[(dic[c]+13)%26]
        elif (c1 in chars) and c2.isalpha():
            if c in vogais:
                x='0'
            else:
                x='1'
        elif (c1 in chars) and (c2 in digitos):
            x=letras_lower[25-dic[c]]
        elif (c1 in chars) and (c2 in chars):
            if x.islower():
                x='0'
            else:
                x='1'
    elif c in digitos:
        if c1.isalpha() and c2.isalpha():
            x=str((int(c))%2)
        elif c1.isalpha() and (c2 in digitos):
            a=int(c)
            if a==1:
                x='!'
            elif a==2:
                x='@'
            elif a==3:
                x='#'
            elif a==4:
                x='$'
            elif a==5:
                x='%'
            elif a==6:
                x='^'
            elif a==7:
                x='&'
            elif a==8:
                x='*'
            elif a==9:
                x='('
            elif a==0:
                x=')'
        elif c1.isalpha() and (c2 in chars):
            x=abs(9-(int(c)))
        elif (c1 in digitos) and c2.isalpha():
            r=random.randint(0,(len(chars)-1))
            x=chars[r]
        elif (c1 in digitos) and (c2 in digitos):
            a=int(c1)
            b=int(c2)
            if b==(a+1):
                x='+'
            elif b==(a-1):
                x='-'
            elif a==b:
                x='='
            elif b>a:
                x='>'
            elif b<a:
                x='<'
        elif (c1 in digitos) and (c2 in chars):
            x=letras_upper[25-(int(c))]
        elif (c1 in chars) and c2.isalpha():
            r=randint(0,1)
            v=[-1,1]
            x=str(((int(c))+v[r])%10)
        elif (c1 in chars) and (c2 in digitos):
            x=letras_upper[int(c)]
        elif (c1 in chars) and (c2 in chars):
            r=random.randint(10,15)
            x=letras_upper[r]
    elif c in chars:
        if c1.isalpha() and c2.isalpha():
            x='.'
        elif c1.isalpha() and (c2 in digitos):
            x=','
        elif c1.isalpha() and (c2 in chars):
            x=';'
        elif (c1 in digitos) and c2.isalpha():
            x='?'
        elif (c1 in digitos) and (c2 in digitos):
            x=':'
        elif (c1 in digitos) and (c2 in chars):
            x='!'
        elif (c1 in chars) and c2.isalpha():
            x='C'
        elif (c1 in chars) and (c2 in digitos):
            x='S'
        elif (c1 in chars) and (c2 in chars):
            x='K'
    return x

def mod_senha(senha):
    s=list(senha)
    if len(s)>=5:
        r=random.sample(range(1,(len(s)-1)), 3)
        c1 = substuicao(s[r[0]-1],s[r[0]],s[r[0]+1])
        c2 = substuicao(s[r[1]-1],s[r[1]],s[r[1]+1])
        c3 = substuicao(s[r[2]-1],s[r[2]],s[r[2]+1])
        s[r[0]] = c1
        s[r[1]] = c2
        s[r[2]] = c3
    elif len(s)==4: 
        c1 = substuicao(s[0],s[1],s[2])
        c2 = substuicao(s[1],s[2],s[3])
        s[1] = c1
        s[2] = c2
        ch=chars[random.randint(0,(len(chars)-1))]
        r=random.randint(0,1)
        if r==0:
            s[0]=ch
        else:
            s[3]=ch
    elif len(s)==3:
        c=substuicao(s[0],s[1],s[2])
        s[1] = c
        s[0]=chars[random.randint(0,(len(chars)-1))]
        s[2]=chars[random.randint(0,(len(chars)-1))]
    elif len(s)==2:
        s[0]=chars[random.randint(0,(len(chars)-1))]
        s[1]=chars[random.randint(0,(len(chars)-1))]
    elif len(s)==1:
        s[0]=chars[random.randint(0,(len(chars)-1))]
        
    nova_senha=''.join(s)
    return nova_senha

def mod_lista_senhas(v):
    w=[]
    for i in range(0,len(v)):
        s=mod_senha(v[i])
        w.append(s)
    return w

def mod_word(s):
    return mod_senha(s)

