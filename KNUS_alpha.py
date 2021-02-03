from bs4 import BeautifulSoup
from pandas import Series, DataFrame
from openpyxl import load_workbook
import re
import requests
import pandas as pd
import time


'''''''''''''''''''''''''''''''''''''''''''''''''''
추가할 사항들
    1. 같은 전공만 표시할것
    2. 강의실 위치 표시할것
    3. 시간표 빈 자리에 넣을 과목 추
'''''''''''''''''''''''''''''''''''''''''''''''''''


def rec(ali):
    catcha = ""
    compa = re.compile('[a-zA-Z0-9_]')

    m = compa.findall(ali)

    for i in range(len(m)):
        catcha += m[i]
    return catcha


def get_exel():
    global tempo, basic, tempo0, every, difcg, all_values
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
            # print(tempo1_values[0][1])
            if tempo1_values[0][1] == "IT대학 전자공학부 A":
                all_values.append(tempo1_values)
            tempo0_values = tempo0_values[a + 1:]
        except:
            return all_values


def get_exelm(tt):
    global tempo, basic, tempo0, every, difcm, frame3, count
    tempo3_values = get_exel()

    for i in range(len(tempo3_values)):
        for j in range(len(tempo3_values[i])):
            if code_subj in str(tempo3_values[i][j][3]):
                all_values.append(tempo3_values[i])
            # print(tempo3_values[i][j][1])
    for p in range(len(all_values)):
        for i in range(len(all_values[p])):
            c = str(all_values[p][i][3])
            c = rec(c)
            xl_time = str(all_values[p][i][10])
            xl_time = xl_time.replace(" ", "")
            if c[:7] != every[0][:7] and c != "None" and c != '' and xl_time == tt:
            # if xl_time == tt:
                tempo0.append(c)
    tempo0.sort()
    tempo = []
    for k in range(len(tempo0)):
        str_main = str_1 + semester + str_2 + tempo0[k][7:] + str_3 + tempo0[k][:7]
        html0 = requests.get(str_main).text
        soup0 = BeautifulSoup(html0, "html.parser")
        r = soup0.find_all(class_='subj_class_cde')
        for p in range(len(basic)):
            for q in range(2, len(r)):
                r = soup0.find_all(class_=basic[p])
                tempo.append(r[q].text)
        if tempo != []:
            difcm.append(tempo)
        tempo = []
    frame3 = DataFrame(difcm)
    try:
        frame3.columns = column
    except:
        pass

    # 3 4 6 9 10


def get_cls():
    global search, cls_time, tempo, every, same, samet, frame0, frame1, frame2, str_sub, code
    # 검색한 과목과 같은 과목들 받아옴
    html = requests.get(str_sub).text
    soup = BeautifulSoup(html, "html.parser")
    b = soup.find_all(class_='subj_class_cde')
    # print(b)
    for i in range(len(basic)):
        for j in range(2, len(b)):
            b = soup.find_all(class_=basic[i])
            tempo.append(b[j].text)
        # print(tempo)
        # search.append(tempo[num_class - 1])
        # tempo.remove(tempo[num_class - 1])
        try:
            find_num = tempo.index(code)
        except:
            pass
        search.append(tempo[find_num])
        tempo.remove(tempo[find_num])
        same.append(tempo)
        tempo = []

    for i in range(len(same[0])):
        if same[4][i] == search[4]:
            for j in range(len(same)):
                tempo.append(same[j][i])
            samet.append(tempo)
            tempo = []
        else:
            for j in range(len(same)):
                tempo.append(same[j][i])
            dift.append(tempo)
            tempo = []

    tempo = search
    every = search
    search = []
    search.append(tempo)
    tempo = []

    frame0 = DataFrame(search)
    frame1 = DataFrame(samet)
    frame2 = DataFrame(dift)

    try:
        frame0.columns = column
    except:
        pass
    try:
        frame1.columns = column
    except:
        pass
    try:
        frame2.columns = column
    except:
        pass
    cls_time = str(search[0][4])
    cls_time = cls_time.replace(" ", "")


def get_all(list_all):
    j = 0
    while j < len(list_all):
        str_01 = "http://my.knu.ac.kr/stpo/stpo/cour/lectReqCntEnq/list.action?lectReqCntEnq.search_open_yr_trm="
        str_02 = "&lectReqCntEnq.search_sub_class_cde="
        str_03 = "&lectReqCntEnq.search_subj_cde="

        codeIn = list_all[j]
        code_0 = codeIn[0:7]
        code_1 = codeIn[7:10]
        str_my_knu = str_01 + semester + str_02 + code_1 + str_03 + code_0
        try:
            html = requests.get(str_my_knu).text
            soup = BeautifulSoup(html, "html.parser")
        except:
            continue
        # print(soup)
        className = soup.find_all(class_='subj_nm')[2].text
        ProfName = soup.find_all(class_='prof_nm')[2].text
        classCode = soup.find_all(class_='subj_class_cde')[2].text
        print(className, end='\t')
        print(ProfName, end='\t')
        print(classCode, end='\t')
        max_per = soup.find_all(class_='lect_quota')
        max_per = max_per[2].text
        now_per = soup.find_all(class_='lect_req_cnt')
        now_per = now_per[2].text
        print(max_per, end='\t')
        print(now_per)
        print('=========================================')
        j += 1


if __name__ == "__main__" :
    basic = ['subj_class_cde', 'subj_nm', 'unit', 'prof_nm', 'lect_wk_tm', 'lect_quota', 'lect_req_cnt']
    column = ['코드', '과목명', '학점', '교수명', '시간', '수강정원', '수강인원']
    list_temp = ['CLTR112006', 'COME301007', 'COMP320001', 'COMP322005', 'COMP411005', 'ELEC462002', 'ELEC464001']
    every = []  # 검색한 전체 과목
    search = []  # 검색 받은 과목
    same = []  # 같은 과목코드 초기화 예정
    samet = []  # 같은 과목코드 같은 시간
    dift = []  # 같은 과목코드 다른 시간
    difcm = []  # 다른 과목코드 같은 시간
    difcg = []  # 다른 과목코드 같은 시간
    tempo = []  # 임시사용 초기화 예정
    tempo0 = []
    x = {}
    y = {}

    count = 0
    cls_time = ""
    semester = ""

    # 같은 과목 검색용 url
    str_1 = "http://my.knu.ac.kr/stpo/stpo/cour/lectReqCntEnq/list.action?lectReqCntEnq.search_open_yr_trm="
    str_2 = "&lectReqCntEnq.search_sub_class_cde="
    str_3 = "&lectReqCntEnq.search_subj_cde="

    # 강의 계획서 url
    str_a = "http://my.knu.ac.kr/stpo/stpo/cour/plans/viewPlanDetail.action?plans.searchOpenYrTrm=%27"
    str_b = "%27&plans.searchSubjCde=%27"
    str_c = "%27&plans.searchSubClassCde=%27"


    # main
    semester = input("현제 학기를 입력해 주세요(ex: 20201): ")
    while True:
        try:
            codeSearch = input("검색하고자 하는 과목 코드를 입력해 주세요: ")
            if codeSearch == '':
                get_all(list_temp)
            else:
                # code = 'COME331001'
                code_subj = codeSearch[:7]  # 과목 분류
                code_class = codeSearch[7:]  # 분반 세자리
                num_class = int(codeSearch[9:])  # 분반 한자리
                str_sub = str_1 + semester + str_2 + str_3 + code_subj  # 검색한 과목과 같은 과목들 표시
                str_obj = str_a + semester + str_b + code_subj + str_c + code_class + "%27"
                # print(str_sub)
                get_cls()
                print("\n")
                print("{0:.^70}".format("검색하신 과목 현황", end="\n\n"))
                print(frame0, end="\n\n")
                print("{0:.^70}".format("같은 시간의 같은 과목들", end="\n\n"))
                print(frame1, end="\n\n")
                print("{0:.^70}".format("다른 시간의 같은 과목들", end="\n\n"))
                print(frame2, end="\n\n")
                print('================================================')
                # get_exelm(cls_time)
                # print("{0:.^70}".format("같은 시간의 다른 전공 과목들", end="\n\n"))
                # print(frame3, end="\n\n")
        except:
            pass