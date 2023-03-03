

op_count = int(input("Введите количество операций: "))

num1 = int(input("Введите число: "))
count = num1
num2 = 0
i = 1
tru = True


while i <= op_count:
    symbol = input("Введите знак: ")
    num2 = float(input("Введите второе число: "))
    i +=1
    match symbol:
        case "+":
            count = count + num2
            print(count)
        case "-":
            count = count - num2
            print(count)
        case "*":
                
            count = count * num2
            print(count)
        case "/":
            if (num2 == 0 or num1 == 0 and symbol == "/"):
                print("На ноль делить нельзя!!!")
            else:
                count = count / num2
                print(count)
        case "^":
            count = count ** num2
            print(count)
        case "%":
            if (num2 == 0 or num1 == 0 and symbol == "%"):
                print("На ноль делить нельзя!!!")
            else:
                count = count % num2
                print(count)
        case _:
            print("Знак не верен!!!")