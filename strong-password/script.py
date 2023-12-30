import sen, sys

if len(sys.argv)==1:
    s=str(input("senha = "))
    print("nova senha -> "+str(sen.mod_word(s)))
elif len(sys.argv)==2:
    arq = open(sys.argv[1],'r')
    v=arq.read().splitlines()
    arq.close()
    w=sen.mod_lista_senhas(v)
    arq = open('output.txt','w')
    for i in range(0,len(w)):
        arq.write(w[i]+'\n')
    arq.close()
    print("lido arquivo "+"'"+sys.argv[1]+"'")
    print("resultado em "+"'output.txt'")
else:
    w=sen.mod_lista_senhas(sys.argv[1:])
    print("ENTRADA -> "+str(sys.argv[1:]))
    print("SAIDA   -> "+str(w))
    
