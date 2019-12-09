def collatz(number):
    if (number%2) == 0:
        number = number // 2
        print(number)
        return number
    else:
        number = 3 * number + 1
        print(number)
        return number

print('Enter number')
while True:
    try: 
        number = int(input())

        if number == 0:
            print(str(1))
        else:
            while number != 1:
                number = collatz(number)
            break
    except:
        print("必须输入一个整数！")