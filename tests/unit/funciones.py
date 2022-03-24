def estandarizar_numeros(sumando_a, sumando_b):
  """
  Esta función estandariza las entradas para que sean valores númericos.
  Transforma fracciones en forma de string a flotante.

  Parameters:
    sumando_a - Primer valor de entrada
    sumando_b - Segundo valor de entrada

  Returns: 
    Los números estandarizados.
  
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
    multiplo_a - Primer valor a multiplicar
    multiplo_b - Segundo valor a multiplicar

  Returns:
    El producto de dos números

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
    sumando_a - Primer valor a sumar
    sumando_b - Segundo valor a sumar

  Returns:
    El agregado de dos números

  >>>suma(2, "4/6")
    2.666...7
  """
  sumando_a, sumando_b = estandarizar_numeros(sumando_a,sumando_b)
  resultado = sumando_a + sumando_b
  
  return resultado

def resta(restando_a, restando_b):
  """
  Realiza la resta de dos números.

  Parameters:
    restando_a - Primer valor a restar
    restando_b - Segundo valor a restar

  Returns:
    La diferencia de dos números

  >>>resta(2, "4/6")
    1.333....
  """
  restando_a, restando_b = estandarizar_numeros(restando_a,restando_b)
  resultado = restando_a - restando_b
    
  return resultado

def division(dividendo, divisor):

  """
  Realiza la división de dos números.

  Parameters:
    dividendo - numerador
    divisor - denominador

  Returns:
    El cociente de dos números

  >>>division(2, "4/6")
    1.333...
  """

  dividendo, divisor = estandarizar_numeros(dividendo, divisor)
  if divisor == 0:
    raise Exception("Division entre cero")
  else:
    resultado = dividendo / divisor 
    return resultado


def fraccion_a_flotante(fraccion):
  num = float(fraccion.split('/')[0])
  den = float(fraccion.split('/')[-1])
  return num/den