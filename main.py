msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
messages = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]
operators = ["+", "-", "*", "/"]
memory = 0.0


def is_one_digit(var):
    var = float(var)
    if var > -10 and var < 10 and var.is_integer() is True:
        return True
    else:
        return False


def check(var1, var2, var3):
    msg = ""
    if is_one_digit(var1) is True and is_one_digit(var2) is True:
        msg = msg + msg_6
    if (var1 == 1 or var2 == 1) and var3 == '*':
        msg = msg + msg_7
    if (var1 == 0 or var2 == 0) and (var3 == '*' or var3 == '+' or var3 == '-'):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


while True:
    print(msg_0)
    x, oper, y = input().split()
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    try:
        x = float(x)
        y = float(y)
        if oper in operators:
            check(x, y, oper)
            if oper == "+":
                result = x + y
                print(result)
            elif oper == "-":
                result = x - y
                print(result)
            elif oper == "*":
                result = x * y
                print(result)
            elif oper == "/" and y != 0:
                result = x / y
                print(result)
            elif oper == "/" and y == 0:
                print(msg_3)
                continue
        else:
            print(msg_2)

    except ValueError:
        print(msg_1)

    print(msg_4)
    answer = input()

    if answer == "y":
        if is_one_digit(result) is True:
            msg_index = 10
            print(messages[msg_index])
            answer = input()
            if answer == "y" and msg_index < 12:
                msg_index += 1
                print(messages[msg_index])
                answer = input()
                if answer == "y" and msg_index < 12:
                    msg_index += 1
                    print(messages[msg_index])
                    answer = input()

    if answer == "y":
        memory = result
        print(msg_5)
        answer = input()

    if answer == "n":
        print(msg_5)
        answer = input()
        if answer == "y":
            continue
        elif answer == "n":
            break