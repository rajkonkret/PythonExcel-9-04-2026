import pandas as pd

data = [
    ['Adiya', 179],
    ['Samen', 189],
    ['Darek', 169],
    ['John', 199],
]

column_name = ['Name', 'Height']

df = pd.DataFrame(data, columns=column_name)

