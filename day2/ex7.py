import openpyxl
from openpyxl.chart import Reference, BarChart
from openpyxl.chart.axis import ChartLines
from openpyxl.chart.layout import Layout, ManualLayout

filename = 'video2.xlsx'
wb = openpyxl.load_workbook(filename)
ws = wb['Total Sales by Genre']

# dane do wykresu
values = Reference(
    ws,
    min_col=2,
    max_col=2,
    min_row=1,
    max_row=13
)

cats = Reference(
    ws,
    min_col=1,
    max_col=1,
    min_row=2,
    max_row=13
)

# tworzenie wykresu
chart = BarChart()
chart.add_data(values, titles_from_data=True)
chart.set_categories(cats)

chart.title = "Total Sales"
chart.x_axis.title = "Genre"
chart.y_axis.title = "Total Sales by Genre"

ws.add_chart(chart, 'D2')

wb.save(filename)
wb.close()
