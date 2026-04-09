import openpyxl

wb = openpyxl.load_workbook('videogamesales.xlsx')
ws = wb.active

print(wb)
print(ws)
