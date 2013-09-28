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
GPIO_TRIGGER = 16
GPIO_ECHO = 18

while True:
	print "hello"
	time.sleep(1)

print("Done!")
