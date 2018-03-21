#!/usr/bin/env python2

import time
import socket
import RPi.GPIO as GPIO

PIN_TEAM = 2

PIN_CLKPOINT = 3
PIN_ENPOINT = 4

PIN_CLKJEU = 17 
PIN_ENJEU = 27

PIN_RAZPOINT = 22
PIN_RAZJEU = 10

PIN_CLKTM = 9
PIN_SERVICE = 11

TCP_IP = "0.0.0.0"
TCP_PORT = 8004
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
    GPIO.setup(PIN_CLKJEU, GPIO.OUT)
    GPIO.setup(PIN_ENJEU, GPIO.OUT)
    GPIO.setup(PIN_RAZPOINT, GPIO.OUT)
    GPIO.setup(PIN_RAZJEU, GPIO.OUT)
    GPIO.setup(PIN_CLKTM, GPIO.OUT)
    GPIO.setup(PIN_SERVICE, GPIO.OUT)
    waitch()

def chpoint(dirc, team):
    if (dirc == COUNT_UP):
        print("Point+")
        GPIO.output(PIN_ENPOINT, GPIO.LOW)
    else:
        print("Point-")
        GPIO.output(PIN_ENPOINT, GPIO.HIGH)

    selteam(team)
    pulse(PIN_CLKPOINT)

def chjeu(dirc, team):
    if (dirc == COUNT_UP):
        print("Jeu+")
        GPIO.output(PIN_ENJEU, GPIO.LOW)
    else:
        print("Jeu-")
        GPIO.output(PIN_ENJEU, GPIO.HIGH)

    selteam(team)
    pulse(PIN_CLKJEU)


def clrpoint(team):
    selteam(team)
    pulse(PIN_RAZPOINT)

def clrjeu(team):
    selteam(team)
    pulse(PIN_RAZJEU)

def addtime(team):
    selteam(team)
    pulse(PIN_CLKTM)

def chsrvs():
    pulse(PIN_SERVICE)

def gpioaction(data):
    if (data == "0\n"):
        chsrvs()

    elif (data == "1\n"):
        chpoint(COUNT_UP, TEAM_A)
    elif (data == "2\n"):
        chpoint(COUNT_DW, TEAM_A)
    elif (data == "3\n"):
        clrpoint(TEAM_A)

    elif (data == "4\n"):
        chjeu(COUNT_UP, TEAM_A)
    elif (data == "5\n"):
        chjeu(COUNT_DW, TEAM_A)
    elif (data == "6\n"):
        clrjeu(TEAM_A)

    elif ((data == "7\n") or (data == "8\n") or (data == "9\n")):
        addtime(TEAM_A)


    elif (data == "10\n"):
        chsrvs()

    elif (data == "11\n"):
        chpoint(COUNT_UP, TEAM_B)
    elif (data == "12\n"):
        chpoint(COUNT_DW, TEAM_B)
    elif (data == "13\n"):
        clrpoint(TEAM_B)

    elif (data == "14\n"):
        chjeu(COUNT_UP, TEAM_B)
    elif (data == "15\n"):
        chjeu(COUNT_DW, TEAM_B)
    elif (data == "16\n"):
        clrjeu(TEAM_B)

    elif ((data == "17\n") or (data == "18\n") or (data == "19\n")):
        addtime(TEAM_B)

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
