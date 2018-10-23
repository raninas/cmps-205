# Ranin


def towers(orig, dest, aux, n):
        if n==1:
            return(orig),(dest)
        else:
            return[towers(orig,aux,dest,n-1) ,(towers(orig,dest,aux,1)),(towers(aux,dest,orig,n-1))]
       
        
    
print(towers('A','B','C',3))     