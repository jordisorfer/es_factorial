def es_factorial(entero,factorial):
    if isinstance(entero,int) and isinstance(factorial,int):
        if entero>0 and factorial>0:
            factorizacion=1
            for i in range(1,entero+1):
                factorizacion=factorizacion*i
            if factorizacion==factorial:
                return True
            return False
        raise ValueError("Els numeros tenen que ser positius")
    raise TypeError("Els numeros tenen que ser enters")
