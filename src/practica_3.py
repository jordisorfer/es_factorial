"""
Aquest mòdul conté una funció per comprovar si un número és el factorial d'un altre.
"""
def es_factorial(entero,factorial):
    """
    Comprova si el factorial proporcionat és el factorial de l'enter donat.

    :param entero: Un enter positiu.
    :param factorial: El suposat factorial de l'enter.
    :return: True si el factorial és correcte, False altrament.
    :raises ValueError: Si els nombres no són positius.
    :raises TypeError: Si els nombres no són enters.
    """
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
