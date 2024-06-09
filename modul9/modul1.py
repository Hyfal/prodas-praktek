import aritmatika

def main():
    a = int(input('Masukkan nilai a: '))
    b = int(input('Masukkan nilai b: '))
    c = float(b)

    print('a\t: %d' % a)
    print('b\t: %d' % b)
    print('c\t: %.2f\n' % c)
          
    print('a + b\t: %d' % aritmatika.tambah (a, b))
    print('a - b\t: %d' % aritmatika.kurang (a, b))
    print('a * b\t: %d' % aritmatika.kali (a, b))
    print('a // b\t: %d' % aritmatika.bagi (a, b))
    print('a / c\t: %f' % aritmatika.bagi (a, c))
    print('a ** b\t: %d' % aritmatika.pangkat (a, b))

if __name__ =='__main__':
    main()

    

