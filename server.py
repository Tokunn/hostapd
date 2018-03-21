#!/usr/bin/env python2

import time
import socket
import RPi.GPIO as GPIO

PIN_TEAM = 2

PIN_CLKPOINT = 3
PIN_ENPOINT = 4

PIN_CLKJEU = 17 
PIN_ENJEU = 27

TCP_IP = "0.0.0.0"
TCP_PORT = 8001
BUFFER_SIZE = 4000

TEAM_A = 0
TEAM_B = 1

COUNT_UP = 0
COUNT_DW = 1 

def waitch():
    time.sleep(0.1)

def waitpls():
    time.sleep(0.1)

def pulse(pin):
    waitpls()
    GPIO.output(pin, GPIO.HIGH)
    waitpls()
    GPIO.output(pin, GPIO.LOW)
    waitpls()

def selteam(team):
    if (team == TEAM_A):
        print("Team A")
        GPIO.output(PIN_TEAM, GPIO.LOW)
    else:
        print("Team B")
        GPIO.output(PIN_TEAM, GPIO.HIGH)


def initgpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_TEAM, GPIO.OUT)
    GPIO.setup(PIN_CLKPOINT, GPIO.OUT)
    GPIO.setup(PIN_ENPOINT, GPIO.OUT)
    waitch()

def chpoint(dirc, team):
    if (dirc == COUNT_UP):
        print("Point+")
        GPIO.output(PIN_ENPOINT, GPIO.LOW)
    else:
        print("Point-")
        GPIO.output(PIN_ENPOINT, GPIO.HIGH)

    selteam(team)
    waitch()
    pulse(PIN_CLKPOINT)
    waitch()

def chjeu(dirc, team):
    if (dirc == COUNT_UP):
        print("Jeu+")
        GPIO.output(PIN_ENJEU, GPIO.LOW)
    else:
        print("Jeu-")
        GPIO.output(PIN_ENJEU, GPIO.HIGH)

    selteam(team)
    waitch()
    pulse(PIN_CLKJEU)
    waitch()


def clrpoint(team):
    pass

def clrjeu(team):
    pass

def addtime(team):
    pass

def chsrvs():
    pass

def gpioaction(data):
    if (data == "1\n"):
        chpoint(COUNT_UP, TEAM_A)
    elif (data == "2\n"):
        chpoint(COUNT_DW, TEAM_A)

    elif (data == "4\n"):
        chjeu(COUNT_UP, TEAM_A)
    elif (data == "5\n"):
        chjeu(COUNT_DW, TEAM_A)

    elif (data == "11\n"):
        chpoint(COUNT_UP, TEAM_B)
    elif (data == "12\n"):
        chpoint(COUNT_DW, TEAM_B)

    elif (data == "14\n"):
        chjeu(COUNT_UP, TEAM_B)
    elif (data == "15\n"):
        chjeu(COUNT_DW, TEAM_B)

    else:
        print("Not detected")
    print("\n")

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(10)

    initgpio()

    while 1:
        conn, addr = s.accept()
        print "Connection address:", addr
        while 1:
            data = conn.recv(BUFFER_SIZE)
            if not data: break
            print "received data:", data[:-1]
            gpioaction(data)
            #conn.send(data)
    conn.close()

if __name__ == "__main__":
    print "main start"
    main()
