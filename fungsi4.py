def kali(a,b):
    return a * b
def echo(s, n):
    for i in range(n):
        print(s)
def main():
    print('pemanggilan pertama fungsi kali():')
    print('2 x 3 = %d' % kali(2,3))

    print('\Pemanggilan kedua fungsi kali():')
    print('10 x 20 =%d' % kali(10,20))

    print('\nPemanggilan pertama fungsi echo():')
    echo('python',5)

    print('\nPemanggilan kedua fungsi echo():')
    echo('Pemograman python', 3)

if __name__ =='__main__':
    main()