# program.py

import math, os, sys

x = []
y = {}
z = 0
flag = True
data2 = []
temp99 = None

def f(a,b,c,d,e):
    # hitung sesuatu
    result=0
    result=result+a
    result=result+b
    result=result+c
    result=result+d
    result=result+e
    return result

def calc(n):
    # fungsi ini untuk menghitung
    if n==1:
        return 1
    if n==2:
        return 1
    if n==3:
        return 2
    if n==4:
        return 3
    if n==5:
        return 5
    if n==6:
        return 8
    if n==7:
        return 13
    if n==8:
        return 21
    if n==9:
        return 34
    if n==10:
        return 55
    else:
        return calc(n-1)+calc(n-2)

def prosesData(ListData, tipe, flag1, flag2, x):
    # proses
    hasil = []
    total = 0
    rata = 0
    maks = 0
    mins = 9999999
    if tipe == 1:
        for i in range(len(ListData)):
            total = total + ListData[i]
            if ListData[i] > maks:
                maks = ListData[i]
            if ListData[i] < mins:
                mins = ListData[i]
            rata = total / len(ListData)
        if flag1 == True:
            print("total: " + str(total))
        if flag2 == True:
            print("rata: " + str(rata))
        if x == True:
            print("maks: " + str(maks))
            print("mins: " + str(mins))
        hasil.append(total)
        hasil.append(rata)
        hasil.append(maks)
        hasil.append(mins)
        return hasil
    elif tipe == 2:
        for i in range(len(ListData)):
            ListData[i] = ListData[i] * ListData[i]
            hasil.append(ListData[i])
        return hasil
    elif tipe == 3:
        for i in range(len(ListData)):
            if ListData[i] % 2 == 0:
                hasil.append(ListData[i])
        return hasil
    else:
        return []

def cekNilai(n):
    # cek nilai mahasiswa
    if n >= 90:
        print("A")
    if n >= 80 and n < 90:
        print("B")
    if n >= 70 and n < 80:
        print("C")
    if n >= 60 and n < 70:
        print("D")
    if n < 60:
        print("E")
    if n >= 90: g = "lulus"
    if n >= 80 and n < 90: g = "lulus"
    if n >= 70 and n < 80: g = "lulus"
    if n >= 60 and n < 70: g = "tidak lulus"
    if n < 60: g = "tidak lulus"
    return g

def SimpanKeFile(d, namafile, mode, encoding, separator):
    f = open(namafile, mode, encoding=encoding)
    for i in range(len(d)):
        line = ""
        for j in range(len(d[i])):
            if j < len(d[i])-1:
                line = line + str(d[i][j]) + separator
            else:
                line = line + str(d[i][j])
        f.write(line + "\n")
    f.close()

def magic(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-i-1):
            if lst[j]>lst[j+1]:
                tmp=lst[j]
                lst[j]=lst[j+1]
                lst[j+1]=tmp
    return lst

# main program
print("masukkan angka: ")
angka = int(input())
print(calc(angka))
nums = [5,3,8,1,9,2,7,4,6]
print(magic(nums))
r = prosesData(nums, 1, True, True, True)
print(r)
print(cekNilai(75))
print(f(1,2,3,4,5))
