#!usr/bin/puthon3

#############################
# Nama file: fungsi.py

#############################

def kali(a, b):
    return a * b

def bagi(a, b):
    return a / b

def main():
    print('PROGRAM PERKALIAN BILANGAN')
    a = float(input('Masukkan nilai a: '))
    b = float(input('Masukkan nilai b: '))

    print('\n%.3f x %.3f = %.3f' % (a, b, kali(a, b)))
    print('%.3f / %.3f = %.3f' % (a, b, bagi(a, b)))

if __name__ == '__main__':
    main()

