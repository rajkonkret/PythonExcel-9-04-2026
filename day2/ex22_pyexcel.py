import pyexcel

# pip install pyexcel pyexcel-xlsx

data = [
    ['Imie', "Wiek"],
    ["Tomek", "38"],
    ["Kasia", "34"]
]

sheet = pyexcel.Sheet(data)
sheet.save_as('wyniki.xlsx')
