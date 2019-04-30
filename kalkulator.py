# Menjumlahkan bilangan
def tambah(x, y):
   return x + y
# Pengurangan bilangan
def kurang(x, y):
   return x - y
# Pengkalian bilangan
def kali(x, y):
   return x * y
# Pembagian bilangan
def bagi(x, y):
   return x / y

print("Option Kalkulator")
print("1.Kalkulator")
print("2.exit")


   
def hitung():               
   print("1.Jumlah")
   print("2.Kurang")
   print("3.Kali")
   print("4.Bagi")

   arit = input("pilih no 1-4 : ")
   print("========================")
   no1 = int(input("angka pertama: "))
   no2 = int(input("angka kedua: "))
   print("========================")
   print("Hasil")
   if arit == '1':
      print(no1,"+",no2,"=", float(tambah(no1,no2)))
      print ("Try Again [Y/N] ? ")
      coba = input().upper()
      if coba == "Y":
            hitung()
      else:
            exit()
   elif arit == '2':
      print(no1,"-",no2,"=", float(kurang(no1,no2)))
      print ("Try Again [Y/N] ? ")
      coba = input().upper()
      if coba == "Y":
            hitung()
      else:
            exit()
   elif arit == '3':
      print(no1,"*",no2,"=", float(kali(no1,no2)))
      print ("Try Again [Y/N] ? ")
      coba = input().upper()
      if coba == "Y":
            hitung()
      else:
            exit()
   elif arit == '4':
      print(no1,"/",no2,"=", (bagi(no1,no2)))
      print ("Try Again [Y/N] ? ")
      coba = input().upper()
      if coba == "Y":
            hitung()
      else:
            exit()
   else:
      print("data yang diinput salah!!")

print("========================")
nop = input("pilih : ")
print("========================")
if (nop == '1'):
   hitung()
elif(nop =='2'):
   exit()
else:
   print("inputan salah,coba lagi!")

