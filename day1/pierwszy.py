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

print(25 * "-")

# teksty są niemutowalne
tekst = "Witaj Świecie"
print(tekst)  # Witaj Świecie

tekst.upper()  # zwraca kopie
# Return a copy of the string converted to uppercase.
print(tekst)  # Witaj Świecie

nowy_tekst = tekst.upper()
print(nowy_tekst)  # WITAJ ŚWIECIE

print(tekst.upper())  # WITAJ ŚWIECIE

zmienna1 = "GROSS"
zmienna2 = "groẞ"

print(zmienna1.lower() == zmienna2.lower())  # False, == - porównanie
# ctrl d - kopiowanie linii
print(zmienna1.casefold() == zmienna2.casefold())  # True, == - porównanie

# typ logiczny-> True, False
print(1 != 0)  # czy różne, True

name = "Radek"

# Nazywam się Radek!
# f-string - sformatowany string
print(f"Nazywam się {name}!")  # Nazywam się Radek!

a = 4.5678
print(f"Liczba: {a}")  # Liczba: 4.5678
print(f"Liczba: {a:.2f}")  # Liczba: 4.57 zaokraglenie
print("Liczba:", a)  # Liczba: 4.5678
print("Liczba:", a, sep="::::")  # Liczba:::::4.5678
# sep
# string inserted between values, default a space.
# end
# string appended after the last value, default a newline.

# %f - float
print("Liczba %f" % a)  # Liczba 4.567800
print("Liczba %.2f" % a)  # Liczba 4.57

# print("Liczba %f" % "Radek")  # TypeError: must be real number, not str

print("""
Tekst
    wielolinijkowy""")
# "Tekst
#     wielolinijkowy"

"""
Komentarz
    wielolinijkowy - dokumentacja - docstring"""

print(print.__doc__)

print(100 / 3)  # 33.333333333333336 -> float
print(100 // 3)  # 33 - część całkowita
print(100 % 3)  # modulo - reszta z dzielenia, 1
# 33 * 3 = 99, 100 - 99 = 1 reszta, modulo
print(10 % 3)  # reszta 1

zysk = 908765432190
print(f"Nasza duża liczba {zysk:,}")  # Nasza duża liczba 908,765,432,190
print(f"Nasza duża liczba {zysk:_}")  # Nasza duża liczba 908_765_432_190
print(f"Nasza duża liczba {zysk:_}".replace("_", " "))
# Nasza duża liczba 908 765 432 190
print(f"Nasza duża liczba {zysk:_}".replace("_", "."))
# Nasza duża liczba 908.765.432.190

liczba = 100_000_000_000
print(type(liczba))  # <class 'int'>
print(liczba)  # 100000000000

# kolekcja

# lista - przechowuje elementy z zachowaniem kolejności

lista = [1, 2, 3, 4, 5, 6, "Radek"]
print(lista)  # [1, 2, 3, 4, 5, 6, 'Radek']
print(type(lista))  # <class 'list'>

lista = []  # pusta lista
lista.append("Radek")
lista.append("Radek")
lista.append("Tomek")
lista.append("Dawid")
lista.append("Artur")
lista.append("Zenek")
print(lista)
# ['Radek', 'Radek', 'Tomek', 'Dawid', 'Artur', 'Zenek']

# usunięcie pierwszego napotkanego
lista.remove("Radek")
print(lista)
# ['Radek', 'Tomek', 'Dawid', 'Artur', 'Zenek']

lista_copy = lista.copy()  # kopia elemtow listy, kopia danych
lista_k = lista  # kopia referencji (adresu)
print(lista_k)  # ['Radek', 'Tomek', 'Dawid', 'Artur', 'Zenek']
print(lista)  # ['Radek', 'Tomek', 'Dawid', 'Artur', 'Zenek']

lista.clear()  # usunięcie wszystkie elementy z listy
print(lista)  # []
print(lista_k)  # []
print(lista_copy)  # ['Radek', 'Tomek', 'Dawid', 'Artur', 'Zenek']

# sprawdzenie adresu
print(id(lista_copy))  # 2180494839744
print(id(lista))  # 2180498864960
print(id(lista_k))  # 2180498864960

# krotka (tupla) - kolekcja niemutowalna, do odczytu
# pozwala lepiej zarzadzac pamięciu

krotka = tuple(lista_copy)
print(krotka)  # ('Radek', 'Tomek', 'Dawid', 'Artur', 'Zenek')
print(type(krotka))  # <class 'tuple'>

tupla1 = "Radek", "Tomek"
print(type(tupla1))  # <class 'tuple'>

tupla2 = "Radek",
print(type(tupla2))  # <class 'tuple'>

# tupla1[1] = "190" # TypeError: 'tuple' object does not support item assignment

