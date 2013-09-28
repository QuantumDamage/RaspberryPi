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

# Przygotowanie pinow
GPIO.setup(GPIO_wyzwalacz,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_rejestrator,GPIO.IN)   # Echo

# Ustawienie wyzwalacza na 0V
GPIO.output(GPIO_wyzwalacz, False)

# Czas dla modulu:
time.sleep(1)

while True:
	print "Ctrl+C aby przerwac!"

	# Wysylanie impulsu 10us do wyzwalacza:
	GPIO.output(GPIO_wyzwalacz, True)
	time.sleep(0.00001)
	GPIO.output(GPIO_wyzwalacz, False)
	start = time.time()
	while True:
  		if GPIO.input(GPIO_rejestrator)==1:
			stop = time.time()
			break
	
	
	# Calculate pulse length
	elapsed = stop-start

	# Distance pulse travelled in that time is time
	# multiplied by the speed of sound (cm/s)
	distance = elapsed * 34000

	# That was the distance there and back so halve the value
	distance = distance / 2

	print "Distance : %.1f" % distance

	time.sleep(1)

