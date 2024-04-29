climate = input('Enter climate here:\n')
temp = eval(input('Enter temperature measuements here:\n'))

if climate == 'Tropical':
    for x in temp:
        if x <= 30:
            print('F')
        else:
            print('U')

elif climate == 'Continental':
    for x in temp:
        if x <= 25:
            print('F')
        else:
            print('U')

else:
    for x in temp:
        if x <= 18:
            print('F')
        else:
            print('U')
