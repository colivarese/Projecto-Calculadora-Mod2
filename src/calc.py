def estandarizar_numeros(sumando_a, sumando_b):
    """
    Esta función estandariza las entradas para que sean valores númericos.
    Transforma fracciones en forma de string a flotante.

    Parameters:
      :param sumando_a: Primer valor de entrada
      :param sumando_b: Segundo valor de entrada
      :returns: Los números estandarizados.

    >>>estandarizar_numeros(5, "1/3")
        5, 0.333
    """
    tipo_sumando_a = type(sumando_a)
    tipo_sumando_b = type(sumando_b)

    if tipo_sumando_a == str:
        if '/' in sumando_a:
            fracc = fraccion_a_flotante(sumando_a)
            sumando_a = fracc

    if tipo_sumando_b == str:
        if '/' in sumando_b:
            fracc = fraccion_a_flotante(sumando_b)
            sumando_b = fracc

    return sumando_a, sumando_b


def multiplicacion(multiplo_a, multiplo_b):
    """
    Realiza la multiplicación de dos números.

    Parameters:
      :param multiplo_a: Primer valor a multiplicar
      :param multiplo_b: Segundo valor a multiplicar
      :returns: El producto de dos números

    >>>multiplicacion(2, "4/6")
      1.333...
    """
    multiplo_a, multiplo_b = estandarizar_numeros(multiplo_a, multiplo_b)
    resultado = multiplo_a * multiplo_b
    return multiplo_a * multiplo_b


def suma(sumando_a, sumando_b):
    """
    Realiza la suma de dos números.

    Parameters:
      :param sumando_a: Primer valor a sumar
      :param sumando_b: Segundo valor a sumar
      :returns: El agregado de dos números

    >>>suma(2, "4/6")
      2.666...7
    """
    sumando_a, sumando_b = estandarizar_numeros(sumando_a, sumando_b)
    resultado = sumando_a + sumando_b
    return resultado


def fraccion_a_flotante(fraccion):
  num = float(fraccion.split('/')[0])
  den = float(fraccion.split('/')[-1])
  return num/den
