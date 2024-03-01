#!/usr/bin/env python3

"""dog = "playful"

if dog == "hungry":
    owner = "refilling the food bowl."
elif dog == "thirsty":
    owner = "Refill water bowl."
elif dog == "playful":
    owner = "Playing tag of war."
elif dog == "cuddly":
    owner = "snuggling."
else:
    owner = "Reading newspaper."
print(f"The {dog} dog is {owner}.")"""


"""def divide(num1, num2):
    try:
        quotient = num1 / num2
        print(quotient)
    except ZeroDivisionError:
        print("Error: num2 cannot be equal to 0")
    except TypeError:
        print("Error: input must be of type int or float")
    finally:
        print("Isn't division fun?")

divide(10 , 0)"""

"""dog = "thirsty"

dict_map = {
    "hungry": "Refilling food bowl.",
    "thirsty": "Refilling water bowl.",
    "playful": "Playing tug-of-war.",
    "cuddly": "Snuggling.",
}

owner = dict_map.get(dog, "Reading newspaper.")
print(f"The {dog} dog is {owner}.")"""


def admin_login(username, password):
    # your code here
    return (
        "Access granted"
        if (username == "admin" or username == "ADMIN") and password == "12345"
        else "Access denied"
    )


print(admin_login("admin", "1245"))


def hows_the_weather(temperature):

    # your code here
    if temperature <= 40:
        return "It's brisk out there!"
    elif temperature > 40 and temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"


print(hows_the_weather(20))


def tell_the_weather(temp):
    return (
        "It's brisk out there!"
        if temp <= 40
        else (
            "It's a little chilly out there!"
            if (temp > 40 and temp <= 65)
            else (
                "It's too dang hot out there!"
                if temp > 85
                else "It's perfect out there!"
            )
        )
    )


print(tell_the_weather(70))


def fizzbuzz(num):
    # your code here
    return (
        "FizzBuzz"
        if (num % 3 == 0 and num % 5 == 0)
        else "Fizz" if num % 3 == 0 else ("Buzz" if num % 5 == 0 else num)
    )


print(fizzbuzz(1))


def calculator(operation, num1, num2):
    # your code here
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print( "Invalid operation!")
        return None


print(calculator("nope", 2, 2))

def calc(op, a, b):
    return (
        a + b
        if op == "+"
        else (
            a - b
            if op == "-"
            else (
                a * b
                if op == "*"
                else a / b if op == "/" else "Invalid operation!"
            )
        )
    )
print(calc("+", 8, 2))
