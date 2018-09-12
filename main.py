# -*- coding: utf-8 -*-
import urllib.request
import os
print("=İndirme aracı oluşturucu=")
print("Not: İndirilecek dosyaları sıkıştırılmış yani zip, rar gibi formatlarda yükleyiniz.")
baslik = input("Başlık: ")
link = input("İndirilecek dosya (örn. ornek.com/ornek.zip): ")
isim = input("İndirilen dosyanın ismi ve uzantısı (örn. ornek.zip): ")
ia = open("ia.py", "w")
ia.write('''# -*- coding: utf-8 -*-
import urllib.request
import os
os.system("title '''+baslik+''' - By IAO")
print("='''+baslik+'''=")
print("Indirme baslatiliyor")
indir = urllib.request.urlretrieve("'''+link+'''","'''+isim+'''")
print("Indirme tamamlandi")
print("Kurulum yapiliyor")
os.system("7zip.exe e '''+isim+'''")
print("Kurulum tamamlandi")''')
ia.close()
urllib.request.urlretrieve("https://www.dropbox.com/s/1g1q5ufru08oy78/7z.exe?dl=1","7z.exe")
urllib.request.urlretrieve("https://www.dropbox.com/s/9x694bj1bl97sgc/7z.dll?dl=1","7z.dll")
print("İşlemler tamamlandı dosya ismi: ia.py")
input("Çıkmak için enter basın")
