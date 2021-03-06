#!/usr/bin/python

import time		# dla operacji czasowych
import RPi.GPIO as GPIO # do pracy z GPIO
import sys		# do wyswietlenia wersji Pythona

# Podstawowe informacje:

print "Wersja Pythona:"
print sys.version
print "Wersja Raspberry Pi:"
print GPIO.RPI_REVISION
print "Wersja modulu RPi.GPIO:"
print GPIO.VERSION

# uzywanie numeracji pinow z plytki RPi
GPIO.setmode(GPIO.BOARD)

# zgodnie z rysunkiem
GPIO_wyzwalacz = 16
GPIO_rejestrator = 18
GPIO_dioda = 22
# Przygotowanie pinow
GPIO.setup(GPIO_wyzwalacz,GPIO.OUT)	# Trigger
GPIO.setup(GPIO_rejestrator,GPIO.IN)	# Echo
GPIO.setup(GPIO_dioda,GPIO.OUT)		#dioda
# Ustawienie wyzwalacza na 0V
GPIO.output(GPIO_wyzwalacz, False)
GPIO.output(GPIO_dioda, False)

# Czas dla modulu:
time.sleep(1)

try:
	while True:
		print "Ctrl+C aby przerwac!"

		# Wysylanie impulsu 10us do wyzwalacza:
		GPIO.output(GPIO_wyzwalacz, True)
		time.sleep(0.00001)
		GPIO.output(GPIO_wyzwalacz, False)
		#start = time.time()
		while GPIO.input(GPIO_rejestrator)==0:
  			start = time.time()

		while GPIO.input(GPIO_rejestrator)==1:
  			stop = time.time()
	
	
		# Obliczanie czasu pomiedzy wyslaniem sygnalu a jego odebraniem
		czas_trwania = stop-start
		#print czas_trwania
		# Powyzszy czas pomnozony przez predkosc dzwieku w cm/s da nam
		# odleglosc_calkowita jaka przebyl impuls
		odleglosc_calkowita = czas_trwania * 34320

		# Odleglosc od obiektu bedzie wiec polowa tej odleglosci:
		odleglosc = odleglosc_calkowita / 2
		#time.sleep(1)
		print "Odleglosc to : %.1f [cm]" % odleglosc
		if odleglosc < 30:
			print "Ktos przeszedl!"
			GPIO.output(GPIO_dioda, True)
			time.sleep(0.1)
		else :
			GPIO.output(GPIO_dioda, False)
			time.sleep(0.1)


except KeyboardInterrupt:
	print "Pa!"
	GPIO.cleanup()
