# https://peps.python.org/pep-0008/
import sys

print()  # wypisz/ wydrukuj
# Process finished with exit code 0 - program zakonczył się bez błedu

print("Radek")
print('Radek')

# ctrl / - komentarz
# print('Radek")
# C:\Users\Szkolenie\PycharmProjects\PythonExcel-9-04-2026\.venv\Scripts\python.exe C:\Users\Szkolenie\PycharmProjects\PythonExcel-9-04-2026\day1\pierwszy.py
#   File "C:\Users\Szkolenie\PycharmProjects\PythonExcel-9-04-2026\day1\pierwszy.py", line 9
#     print('Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 9)
#
# Process finished with exit code 1
print("Dalsza część programu")

print(type("Radek"))  # <class 'str'>, tekstowe

print(45)
print(type(45))  # <class 'int'>, całkowite

print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4,
# default_max_str_digits=4300, str_digits_check_threshold=640)

print("34" + "90")  # 3490
print(34 + 19)  # 53

# print("34" + 19)  # TypeError: can only concatenate str (not "int") to str

print(34 * "168")
# 168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168

print(34 * 168)  # 5712

print(25 * "-")

# liczby zmiennoprzecinkowe
print(4.56)
print(type(4.56))  # <class 'float'>

print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
# min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

# błąd zokrąglenia
print(0.1 + 0.9)  # 1.0
print(0.1 + 0.2)  # 0.30000000000000004
# For example, in a floating-point arithmetic with five base-ten digits,
# the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345

# decimal - pozwala ominąc problem zaokrąglenia

# zmienna - pudełko na dane
# snake_case

# typowanie dynamiczne
name = "Radek"
print(name)  # Radek
print(type(name))  # <class 'str'>

name = 90
print(name)
print(type(name))  # <class 'int'>

# rzutowanie
a = "1"
b = 0
# print(a + b) # TypeError: can only concatenate str (not "int") to str
print(int(a) + int(b))  # int() - rzutowanie na int, 1

print(str(1) + str(1))  # 11
# mypy
# type hinting
a: int = "1"
print(a)  # 1
