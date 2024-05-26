#convertir la cifra de segundos en dias minutos y segundos
seg=288325
a=(seg/60)/60
b=(a%int(a))*60
c=(b%int(b))*60
print(seg, "segundos son...", int(a), "horas...", int(b), "minutos...", int(c), "segundos")