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
