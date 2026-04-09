import openpyxl

wb = openpyxl.load_workbook('videogamesales.xlsx')
ws = wb.active

print(wb)  # <openpyxl.workbook.workbook.Workbook object at 0x000001D288501550>
print(ws)  # <Worksheet "vgsales">
