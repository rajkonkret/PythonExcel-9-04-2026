import openpyxl

wb = openpyxl.load_workbook('videogamesales.xlsx')
ws = wb.active

print(wb)  # <openpyxl.workbook.workbook.Workbook object at 0x000001D288501550>
print(ws)  # <Worksheet "vgsales">

ws = wb['vgsales']  # wybieramy arkusz do działąń

print("Total number of rows:", ws.max_row)  # Total number of rows: 16328
print("Total number of columns:", ws.max_column)  # Total number of columns: 10

print("Value in cell A1 is:", ws['A1'].value)  # Value in cell A1 is: Rank

# list comprehensions
values = [ws.cell(row=1, column=i).value for i in range(1, ws.max_column + 1)]
print(values)
# ['Rank', 'Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']

data = [ws.cell(row=i, column=2).value for i in range(2, 12)]
print(data)
# ['Wii Sports',
#  'Super Mario Bros.',
#  'Mario Kart Wii',
#  'Wii Sports Resort',
#  'Pokemon Red/Pokemon Blue',
#  'Tetris',
#  'New Super Mario Bros.',
#  'Wii Play',
#  'New Super Mario Bros. Wii',
#  'Duck Hunt']

my_list = list()  # pusta lista
for value in ws.iter_rows(
        min_row=1,
        max_row=11,
        min_col=1,
        max_col=6,
        values_only=True
):
    my_list.append(value)

print(my_list)
