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
