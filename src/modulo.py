#!/user/bin/python
#! encoding: UTF-8

import sys
import math

PI35DT = 3.1415926535897931159979634685441852
# Podemos hacerlo tambien con una funcion
def calcular_Pi (n):
  sumatorio = 0.0
  ini = 0.0
  intervalos = 1.0 / float (n)
  for i in range (n):
    x_i = ((i+1) - 1.0/2.0) / n
    fx_i = 4.0 / (1+x_i * x_i)
    # print " Subintervalo: [", ini, ",", ini+intervalos, "] x_i:", x_i, "fx_i:", fx_i
    ini += intervalos
    sumatorio += fx_i
  valor_pi = sumatorio / n
  return (valor_pi)
def error (n,aproximaciones,umbral):
  PI35DT = 3.1415926535897931159979634685441852
  intervalo = n
  lista = []
  for i in range (aproximaciones):
    valor = calcular_Pi (intervalo)
    lista.append (valor)   # EL comando append añade a la lista el valor de Pi en cada caso  
    intervalo += n
  diferencia = []
  for i in range (aproximaciones):
    dif = abs (PI35DT - lista[i])
    diferencia.append (dif)
  correcto = 0
  for i in range (aproximaciones):
    if (diferencia[i]<=umbral):
      correcto = correcto +1
  porcentaje = 100.0 * (1.0 -float(correcto)/float (aproximaciones))
  return (porcentaje)
# Programa principal
if (__name__ == "__main__"):
  argumentos = sys.argv[1:]
 # print argumentos         Imprime la lista con los parametros que le des desde la consola
  if (len(argumentos) == 3):# si la lista es de tres elementos (n,aproximaciones,umbral)
    n = int(argumentos[0])
    aproximaciones = int(argumentos[1])
    umbral = float(argumentos[2])
  else:
    print "Introduzca el nº de intervalos (n>0):"
    n = int (raw_input())
    print "Introduzca el nº de aproximaciones (aproximaciones>0):"
    aproximaciones = int(raw_input())
    print "Introduzca el umbral de error:"
    umbral = float(raw_input())
  if (n > 0):
    porcentaje = error (n,aproximaciones,umbral)
    print "El porcentaje de fallos es del ",porcentaje
  else:
    print "EL valor de los intervalos debe ser mayor que 0"
