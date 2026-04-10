import xlwings as xw
import pandas as pd
import numpy as np

df = pd.DataFrame(data=np.random.randn(100, 5),
                  columns=[f'Próba {i}' for i in range(1, 6)])

print(df)

print(45 * "-")
print(df.head())  # pięć pierwszych
print(df.tail())
#      Próba 1   Próba 2   Próba 3   Próba 4   Próba 5
# 95  0.392119  0.377743  1.614881  0.692887 -0.194467
# 96 -0.818369  1.241335 -1.051172  1.659447  1.488548
# 97  0.813428 -0.437250  0.041143 -1.413062  0.726365
# 98  1.459269 -0.012810 -0.608347  0.968398  0.168882
# 99 -0.218745 -1.004996 -0.025484 -1.937173  0.640872

# xw.view(df)

# tworzymy pusty arkusz
book = xw.Book()
print(book.name)
print(book.sheets)
# Zeszyt1
# Sheets([<Sheet [Zeszyt1]Arkusz1>])

sheet1 = book.sheets[0]
print(sheet1.range('A1'))  # <Range [Zeszyt1]Arkusz1!$A$1>

sheet1.range('A1').value = [[1, 2],
                            [3, 4]]

sheet1.range('A4').value = "witaj!"

print(sheet1['A1'].value)  # 1.0
print(sheet1["A1:B2"].value)
# [[1.0, 2.0], [3.0, 4.0]]
