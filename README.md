#Server System Program for Scoreboard

## What is this ?
This is Server program which I developed in IUT de Tours GEII.
It drive a scoreboard device depending on a cntroller signal.

## Device
Raspberry Pi 3
Only Pi3 includes Wi-Fi Module.

## How to use it ?

### 1. Install Apps
Install hostapd and dnsmasq
$ sudo apt-get install hostapd dnsmasq

### 2. Copy
Copy files to your system.
$ sudo cp ./interfaces /etc/network/interfaces
$ sudo cp ./hostapd.conf /etc/hostapd/hostapd.conf
$ sudo cp ./dnsmasq.conf /etc/dnsmasq.conf

### 3. Reboot
Reboot your system
$ sudo reboot

### 4. Start program
Start hostapd
$ sudo /usr/sbin/hostapd /etc/hostapd/hostapd.conf
Open another (your favorite) terminal
Start server.py
$ sudo python2 ./server.py

## How it works ?
The server.py is waiting on 172.24.1.1 TCP 8004 port.
If recive the number (button ID), it drives GPIOs to send a corresponding signal.
You can find GPIO pin assigns at head of server.py.


## I can not understand what you are saying !!
Ask me.
Twitter: @KTokunn
