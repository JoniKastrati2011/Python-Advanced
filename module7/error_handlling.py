#
# try:
#
#     result = 10 / 0
# except ZeroDivisionError:
#     print("You can't divide by zero")
#
#
# fruits = {
#     "apple": 10,
#     "banana": 20,
#     "orange": 30,
# }
#
# try:
#     print(fruits["cherry"])
# except KeyError:
#     print("You can't print something it doesn't exist")
#
#
# text = "this is a text"
#
# try:
#     text_to_int = int(text)
# except Exception as e:
#     print("An error will typecasting" , e)


def divide_numbers (a , b):
    try:
        result = a / b
        print("Result is ", result)
    except ZeroDivisionError:
        print("You can't divide by zero")
    except TypeError:
        print("Invalide type of dev")
    except Exception as e:
        print("An error will typrcasting" , e)


divide_numbers(10, 2)
divide_numbers(10, 0)
divide_numbers(10, "2")