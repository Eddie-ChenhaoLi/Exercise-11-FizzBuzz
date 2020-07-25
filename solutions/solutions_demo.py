def fizz(i):
    if i % 3 == 0:
        return 1
    if '3' in str(i):
        return 1
    return 0


def buzz(i):
    if i % 5 == 0:
        return 1
    if '5' in str(i):
        return 1
    return 0


for i in range(1, 101):
    if fizz(i):
        if buzz(i):
            print('FizzBuzz')
        else:
            print('Fizz')
        continue
    if buzz(i):
        print('Buzz')
        continue
    print(i)
