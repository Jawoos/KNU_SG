from openpyxl import load_workbook

xl_time = ""
tt = "월1A,1B,2A수5B,6A,6B"


tempo0 = []
majorEx = load_workbook(filename='major1.xlsx')
sheet = majorEx.worksheets[0]
all_values = []
tempo0_values = []
tempo1_values = []


for row in sheet.rows:
    row_value = []
    for cell in row:
        row_value.append(cell.value)
    tempo0_values.append(row_value)
while True:
    try:
        a = tempo0_values.index(
            [None, None, None, None, None, '수  업  시  간  표', None, None, None, None, None, None, None, None, None,
             None])
        tempo1_values = tempo0_values[:a]
        print(tempo1_values[0][1])
        if tempo1_values[0][1] == "IT대학 전자공학부 A":
            all_values.append(tempo1_values)
        tempo0_values = tempo0_values[a+1:]
    except:
        break
print(all_values)
# print(len(all_values))