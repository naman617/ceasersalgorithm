# Open a file
fo = open("foo.txt", "a+")
while(1):
    a = input('enter the name')
    b = input('enter the phone no')
    c = input('Place of origin')
    d = input('Body Temp')
    fo.write(f'\n{a}\n')
    fo.write(f'{b}\n')
    fo.write(f'{c}\n')
    fo.write(f'{d}\n')
    e = input('c for continue e for exit')
    if e == 'e':
        break


# Close opend file
fo.close()
