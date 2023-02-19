def arithmetic_arranger(operazioni):
    operatori=[False,False,False,False]
    numeri=list()
    z=0
    for x in operazioni:
        y=split_pm(x)
        numeri.append(y)
        for oper in x:
            if oper=='+':
                operatori[z]=True
        z+=1
    print('\n\n')
    stampa_numeratore(numeri)
    stampa_operatore_denominatore(numeri,operatori)
    stampa_trattini()
    stampa_risultato(numeri,operatori)

def stampa_numeratore(numeri):               #funzione che stampa la prima linea
    k=0
    for x in numeri:
        if k<=2:
            if unità(x[0]):       #1+1
                print ('       ',x[0], end='\t')
            elif decina(x[0]):
                print ('      ',x[0], end='\t')
            elif centinaia(x[0]):
                print ('    ',x[0], end='\t')
            elif migliaia(x[0]):
                print ('   ',x[0], end='\t')
        else:
            if unità(x[0]):         #1+1
                print('       ',x[0])
            elif decina(x[0]):
                print ('      ',x[0])
            elif centinaia(x[0]):
                print ('    ',x[0])
            elif migliaia(x[0]):
                print ('   ',x[0])
        k+=1

def stampa_operatore_denominatore(numeri,operatori):            #funzione che stampa la seconda linea
    k=0    #contatore
    for x in numeri:
        l=str()
        if operatori[k]==True:
            l='+'
        else:
            l='-'
        if k<=2:
            if unità(x[1]):
                print(f'  {l}   ',x[1], end='\t')
            elif decina(x[1]):
                print(f'  {l}  ',x[1], end='\t')
                
            elif centinaia(x[1]):
                print (f' {l} ',x[1], end='\t')
                
            elif migliaia(x[1]):
                print (f' {l}',x[1], end='\t')
        else:
            if unità(x[1]):
                print(f'  {l}   ',x[1])
            elif decina(x[1]):
                print(f'  {l}  ',x[1])
                
            elif centinaia(x[1]):
                print (f' {l} ',x[1])
                
            elif migliaia(x[1]):
                print (f' {l}',x[1])
        k+=1

def stampa_trattini():          #stampa 3 linea
    k=0
    while k<=4:
        if k<=3:
            print(f' ','-------', end='\t')
        else:
            print(f'    ')
        k+=1

def stampa_risultato(numeri,operatori):       #stampa 4 linea
    k=0
    negativo=False
    positivo=False
    for x in numeri:
        if operatori[k]:
            risultato=int(x[0])+int(x[1])
            positivo=True
        else:
            if int(x[1])>=int(x[0]):
                risultato=int(x[1])-int(x[0])
                negativo=True
            else:
                risultato=int(x[0])-int(x[1])
                positivo=True
        if k<=3:

            if unità(risultato) and negativo:
                print ('      -',risultato, end='\t')   
            elif decina(risultato)and negativo:
                print ('     -',risultato, end='\t')
            elif centinaia(risultato)and negativo:
                print ('    -',risultato, end='\t')
            elif migliaia(risultato) and negativo:
                print ('  -',risultato, end='\t')
            elif milioni(risultato) and negativo:
                print (' -',risultato, end='\t')
            elif miliardo(risultato) and negativo:
                print ('-',risultato, end='\t') 

            negativo=False
            if unità(risultato) and positivo:
                print ('       ',risultato, end='\t')
            elif decina(risultato)and positivo:
                print ('      ',risultato, end='\t')
            elif centinaia(risultato)and positivo:
                print ('    ',risultato, end='\t')
            elif migliaia(risultato)and positivo:
                print ('  ',risultato, end='\t')
            elif milioni(risultato)and positivo:
                print (' ',risultato, end='\t')
            elif miliardo(risultato)and positivo:
                print ('',risultato, end='\t')
            positivo=False
            
        else:
            if unità(risultato) and negativo:
                print ('      -',risultato, end='\t')
            elif decina(risultato)and negativo:
                print ('     -',risultato, end='\t')
            elif centinaia(risultato)and negativo:
                print ('    -',risultato, end='\t')
            elif migliaia(risultato) and negativo:
                print ('  -',risultato, end='\t')
            elif milioni(risultato) and negativo:
                print (' -',risultato, end='\t')
            elif miliardo(risultato) and negativo:
                print ('-',risultato, end='\t') 
            negativo=False
            
            if unità(risultato)and positivo:         
                print('       ',risultato)
            elif decina(risultato)and positivo:
                print ('      ',risultato)
            elif centinaia(risultato)and positivo:
                print ('    ',risultato)
            elif migliaia(risultato)and positivo:
                print ('  ',risultato)
            elif milioni(risultato)and positivo:
                print (' ',risultato)
            elif miliardo(risultato)and positivo:
                print ('',risultato)
            positivo=False
                
        k+=1 # ++contatore


def split_pm(x,l='+',k='-'):     #funzione che divide l'operazione
    if '+' in x:
        z=x.split('+')
        return z
    else:
        z=x.split('-')
        return z

def unità(x):                                              #10
    if int(x) >=0 and int(x)<=9:
        return True

def decina(x):                                             #100
    if int(x) >=10 and int(x)<=99:
        return True

def centinaia(x):                                         #1000
    if int(x) >=100 and int(x)<=999:
        return True

def migliaia(x):                                           #10000
    if int(x)>=1000 and int(x)<=9999:
        return True

def milioni(x):                                             #100000
    if int(x)>=10000 and int(x)<=99999:
        return True
    
def miliardo(x):                                            #10000000
    if int(x)>=100000 and int(x)<=999999:
        return True
