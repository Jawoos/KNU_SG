# import openpyxl
#
# wb = openpyxl.load_workbook('major1.xlsx')
#
# ws = wb.active

# for r in ws.rows:
#     check = r[5].value
#     if check == "수  업  시  간  표":
#         print(check)
import pandas as pd
import numpy as np
import os

df_from_excel = pd.read_excel(header = 3)