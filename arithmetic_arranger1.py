import arithmetic_arranger

def main():
    op=[' '," ",' '," "]
    y=0
    while y < 4:
        x=input(f"dammi il {y+1} problema matematico o addizione o sottrazione -> ")
        if '*' in x or 'x'  in x or '/'  in x or '%'  in x or '+' not in x and '-' not in x:
            print('Errore, riprovare') 
            y=y
        else:
            op[y]=x
            y+=1
 
    arithmetic_arranger.arithmetic_arranger(op)
    
if __name__=='__main__':
    main()
