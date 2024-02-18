def es_factorial(entero,factorial):
    if isinstance(entero,int) and isinstance(factorial,int):
        if entero>0 and factorial>0:
            factorizacion=1
            for i in range(1,entero+1):
                 factorizacion=factorizacion*i
            if factorizacion==factorial:
                    return True
            else:
                return False
        else:
             raise(ValueError)
                
    else:
        raise(TypeError)