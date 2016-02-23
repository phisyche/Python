def countdown(n):
    print('Entering countdown(',n,')')
    if n == 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n - 1)
    print('Exiting from countdown(',n,')')

limit = int(input())
countdown(limit)
