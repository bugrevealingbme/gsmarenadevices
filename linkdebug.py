# -*- coding: utf-8 -*- 

import requests
from bs4 import BeautifulSoup
import urllib.request
import mysql.connector
from sys import argv

cihazexport = open("butunmarkalar.txt", "wb")
while True:
  url = "https://www.gsmarena.com/makers.php3"
  headers = {'User-Agent': 'Mozilla/5.0'}
  url_oku = requests.get(url, headers=headers)
  html_content = url_oku.text
  soup = BeautifulSoup(html_content,'html.parser')
  
  cihazyazilacak = soup.find('div',{'class':'st-text'})
  cihazexport = open("butunmarkalar.txt", "ab")
  cihazexport.close()
	
  for cihazyazilacak in cihazyazilacak.findAll('a', href=True):
    cihazexport = open("butunmarkalar.txt", "ab")
    cihazexport.write("https://www.gsmarena.com/".encode('utf-8')+str(cihazyazilacak['href'].strip()).encode('utf-8'))
    cihazexport.write(str("\n").encode('utf-8'))

  break
	
	
cihazexport = open("sayfalar.txt", "wb")
#bitti

sayac=0
while True:
  f=open('butunmarkalar.txt')
  lines = f.readlines()
  try:
    if (str(lines[sayac]) == ""):
      print("Bitti.")
      break
  except:
    print("Bitti.")
    break  
  url = lines[sayac].strip()
  cihazexport = open("sayfalar.txt", "ab")
  cihazexport.write(str(url).encode('utf-8'))
  cihazexport.write(str("\n").encode('utf-8'))
  cihazexport.close()  
  headers = {'User-Agent': 'Mozilla/5.0'}
  sayac+=1
  url_oku = requests.get(url, headers=headers)
  html_content = url_oku.text
  soup = BeautifulSoup(html_content,'html.parser')
  
  cihazyazilacak = soup.find('div',{'class':'nav-pages'})
  if (cihazyazilacak is not None):
    for cihazyazilacak in cihazyazilacak.findAll('a', href=True):
      cihazexport = open("sayfalar.txt", "ab")
      cihazexport.write("https://www.gsmarena.com/".encode('utf-8')+str(cihazyazilacak['href'].strip()).encode('utf-8'))
      cihazexport.write(str("\n").encode('utf-8'))

  print("Markanın listesi çıkartıldı.")


cihazexport = open("butuncihazlar.txt", "wb")
sayac=0
while True:
  print ("Uzun sürebilir...")
  f=open('sayfalar.txt')
  lines = f.readlines()
  try:
    if (str(lines[sayac]) == ""):
      print("Bitti.")
      break
  except:
    print("Bitti.")
    break  
  url = lines[sayac].strip() 
  headers = {'User-Agent': 'Mozilla/5.0'}
  sayac+=1
  url_oku = requests.get(url, headers=headers)
  html_content = url_oku.text
  soup = BeautifulSoup(html_content,'html.parser')

  cihazyazilacak = soup.find('div',{'class':'makers'})
  for cihazyazilacak in cihazyazilacak.findAll('a', href=True):
    cihazexport = open("butuncihazlar.txt", "ab")
    cihazexport.write("https://www.gsmarena.com/".encode('utf-8')+str(cihazyazilacak['href'].strip()).encode('utf-8'))
    cihazexport.write(str("\n").encode('utf-8'))
