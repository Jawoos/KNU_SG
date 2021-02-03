from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup





def get_exle():
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
            tempo0_values = tempo0_values[a + 1:]
        except:
            break


code = input("검색하고자 하는 과목 코드를 입력해 주세요: ")
code = 'COME301004'
code_subj = code[:7]  # 과목 분류
code_class = code[7:]  # 분반 세자리
num_class = int(code[9:])  # 분반 한자리

# 강의 계획서 str
str_a = "http://my.knu.ac.kr/stpo/stpo/cour/plans/viewPlanDetail.action?plans.searchOpenYrTrm=%27"
str_b = "%27&plans.searchSubjCde=%27"
str_c = "%27&plans.searchSubClassCde=%27"
semester = "20192"

str_obj = str_a + semester + str_b + code_subj + str_c + code_class + "%27"

html = requests.get(str_obj).text
soup = BeautifulSoup(html, 'html.parser')
print(soup)

code_search0 = code_subj + "-" + code_class

