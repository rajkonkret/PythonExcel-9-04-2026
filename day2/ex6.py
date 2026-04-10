import openpyxl

filename = 'video2.xlsx'

wb = openpyxl.load_workbook(filename)
ws = wb['vgsales']

ws['P1'] = "Averages Sales"
ws['P2'] = '=AVERAGE(K2:K16328)'
# =ŚREDNIA(K2:K16328)
wb.save(filename)
wb.close()

ws['Q1'] = "Number of populated cells"
ws['Q2'] = '=COUNTA(E2:E16328)'
# =ILE.NIEPUSTYCH(E2:E16328)
wb.save(filename)
wb.close()

ws["S1"] = "Total Sports Sales"
ws['S2'] = '=COUNTIF(E2:E16328, "Sports")'
# =LICZ.JEŻELI(E2:E16328; "Sports")

wb.save(filename)
wb.close()

print(ws['S2'].value)  # =COUNTIF(E2:E16328, "Sports")

# zsumanie sprzedazy dla spełniających warunek
ws['T1'] = "Total sum of Sports sales"
ws['T2'] = '=SUMIF(E2:E16328, "Sports", K2:K16328)'
# =SUMA.JEŻELI(E2:E16328; "Sports"; K2:K16328)

wb.save(filename)
wb.close()

# zaokrąglenie do najbliższego górnego 25
ws['U1'] = "Rounded sum of Sports Sales"
ws['U2'] = '=CEILING(T2, 25)'

wb.save(filename)
wb.close()

# zaokrąglenie do najbliższego górnego całkowitego
ws['V1'] = "Rounded sum of Sports Sales"
ws['V2'] = '=CEILING(T2, 1)'
# =ZAOKR.W.GÓRĘ(T2; 1)
wb.save(filename)
wb.close()

# w dół
ws['X1'] = "FLOOR"
ws['X2'] = '=FLOOR(T2, 25)'
wb.save(filename)
wb.close()
# =ZAOKR.W.DÓŁ(T2; 25)

ws['W1'] = "Rounded"
ws['W2'] = '=ROUND(T2, 0)'
wb.save(filename)
wb.close()
# =ZAOKR(T2; 0)
