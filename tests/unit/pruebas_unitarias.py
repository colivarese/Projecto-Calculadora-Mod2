import pytest
import funciones as tf

def test_suma_1():
  assert tf.suma(3,5) == 8

def test_suma_2():
  assert tf.suma('2/3','1/3') == 1

def test_fraccion_a_flotante():
  assert tf.fraccion_a_flotante('2/4') == 0.5

def test_mul():
  assert tf.multiplicacion(3,3) == 9

def test_resta():
  assert tf.resta(3,4) == -1

def test_division():
  assert tf.division(20,'2/4') == 40