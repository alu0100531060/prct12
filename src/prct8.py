#!/user/bin/python
#! encoding: UTF-8

import sys
import math
import modulo
import time
import timeit
# Programa principal

argumentos = sys.argv[1:]
 # print argumentos         Imprime la lista con los parametros que le des desde la consola
if (len(argumentos) == 8):  # Ocho argumentos
  n = int(argumentos[0])
  aproximaciones = int(argumentos[1])
  umbral = []
  for i in range (2,7):
    umbral.append(float (argumentos[i]))
  nombre_fichero = argumento [7]
else:
  print "Introduzca el nº de intervalos (n>0):"
  n = int (raw_input())
  print "Introduzca el nº de aproximaciones (aproximaciones>0):"
  aproximaciones = int(raw_input())
  print "Introduce 5 umbrales"
  umbral = []
  for i in range (5):
    print "Introduzca el umbral", i,":"
    umbral.append(float(raw_input()))
  print "Introduzca el nombre del fichero para almacenar los resultados:"
  nombre_fichero = raw_input()
if (n > 0):
  try:
    fichero = open (nombre_fichero, "a")      # Intenta abrir el fichero  de  nombre_fichero y si no esta creado lo crea con la linea de except
  except:
    fichero = open (nombre_fichero, "w")
  fichero.write ("Nº de intervalos: %d\n"%(aproximaciones))    # Escribe en el fichero el numero de intervalos
  for i in range (5):
    start=time.time()
    modulo.error (n,aproximaciones,umbral[i])
    finish=time.time()-start
    t1=timeit.Timer("modulo.error(n,aproximaciones,umbral)",setup="from__main__import modulo; n=%d; aproximaciones=%d;umbral=%f" % (n,aproximaciones,umbral[i]))
    print t1.timeit(10)
    fichero.write("Con el umbral [%d] tarda: %2.10f\n" % (i,finish))
    fichero.close()    # cierra fichero
else:
  print "EL valor de los intervalos debe ser mayor que 0"