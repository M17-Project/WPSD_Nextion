#!/usr/bin/python3
# coding=utf-8

# this file has been modified for DVMEGA-Cast by PE1MSZ (ruud@combitronics.nl)
# Py3 update by W0CHP - WPSD Project
# Further updates by KC1AWV - M17 Project

import threading
import time
import os
import sys
import serial
from alive_progress import alive_bar

debug = 0

if len(sys.argv) != 4:
	print("usage: python %s [/dev/port] [baudrate] [FILE]" % sys.argv[0])
	exit(2)

port = sys.argv[1]
baud = int(sys.argv[2])
file_path = sys.argv[3]
check_model = str(sys.argv[3])[:-4]

print(' _      _____  _______ \n| | /| / / _ \/ __/ _ \\ \n| |/ |/ / ___/\ \/ // /\n|__/|__/_/  /___/____/\nNextion TFT Uploader\n')

if os.path.isfile(file_path):
	print("Uploading %s..." % (file_path))
else:
	print("File not found!")
	exit(1)

fsize = os.path.getsize(file_path)
print("Filesize: " + str(fsize))

ser = serial.Serial(port, timeout=.1)

acked = threading.Event()
stop_thread = threading.Event()

def reader():
    global acked
    global ser
    while stop_thread.is_set() == False:
        r = ser.read(1)
        if r == '':
            continue
        elif b'\x05' in r:
            acked.set()
            continue
        else:
            if debug:
                print("<%r>" % r)
            else:
                continue

def upload():
    global acked
    global ser
    global stop_thread
    ser.write(b'\xff\xff\xff')
    ser.write(b'whmi-wri %i,%i,0' % (fsize, baud))
    ser.write(b'\xff\xff\xff')
    time.sleep(0.01)
    r = ser.read(128)
    ser.flush()
    acked.clear()
    ser.timeout = 1
    threader.start()
    print("Waiting for ACK...")
    print("Uploading...")
    with open(file_path, 'rb') as hmif:
        with alive_bar(manual=True) as bar:
            dcount = 0
            while True:
                time.sleep(.1)
                data = hmif.read(4096)
                if len(data) == 0: break
                dcount += len(data)
                ser.write(data)
                acked.clear()
                bar(dcount/ float(fsize))
                acked.wait()
    stop_thread.set()
    threader.join(1)


threader = threading.Thread(target = reader)
threader.daemon = True

no_connect = True

ser.baudrate = baud
ser.timeout = 3000/baud + 1.5
print("Trying with " + str(baud) + "...")
ser.write(b'\xff\xff\xff')
ser.write(b'\xe0\x0c\x04\xff\x00\x00\x00\x00\x00\x00\x00\x00')
time.sleep(1)
ser.write(b'\xff\xff\xff')
ser.write(b'connect')
ser.write(b'\xff\xff\xff')
time.sleep(0.25)
response = ser.read(128)
if b'comok' in response:
    print("Connected with " + str(baud) + "!")
    no_connect = False
    if debug:
        print(response.strip(b'\xff\x00'))
    status, reserved, model, fw_version, mcu_code, serial_no, flash_size = response.strip(b'\xff\x00').split(b',')
    if debug:
        print(str(status))
        print(str(model))
        print(str(fw_version))
        print(str(mcu_code))
        print(str(serial_no))
        print(str(flash_size))
    else:
        print("Status: " + str(status.decode()))
        print("Model: " + str(model.decode()))
        print("Version: " + str(fw_version.decode()))
        print("MCU Code: " + str(mcu_code.decode()))
        print("Serial: " + str(serial_no.decode()))
        print("Flash size: " + str(flash_size.decode()))
    if fsize > int(flash_size):
        print("File too big!")
        exit(1)
    if not check_model in str(model):
        print("Wrong Display!")
        exit(1)
    upload()

if no_connect:
    print("No connection!")
else:
    print("File written to Display!")

ser.close()
exit(0)