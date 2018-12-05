#Kegiatan1

berkas = open("L200183174","w")
berkas.write("L200183174 \n")
berkas.write("02-09-2000 \n")
berkas.write("Azie Melasari")
file.close()



#Kegiatan 2

berkas = open("L200183174","r")
NIM = berkas.readline()
TTL = berkas.readline()
Name = berkas.readline()
a = TTL[:3]; b = TTL[3:6]; c = TTL[6:]
TTL = b + a + c
print (Name)
print ("Sragen,",TTL)
print (NIM)
berkas.close()



#Kegiatan 3
import shelve

berkas = open("L200183174","r")
NIM = berkas.readline()
TTL = berkas.readline()
Name = berkas.readline()
F = shelve.open("Azi")
F["Biodata"] = [NIM, TTL, Name]
F.close()



#Kegiatan 4

import shelve

F = shelve.open("Azi")
print(F['Biodata'][0])
print(F['Biodata'][1])
print(F['Biodata'][2])
data.close()
