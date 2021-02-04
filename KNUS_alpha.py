from bs4 import BeautifulSoup
from pandas import DataFrame
import requests
import os
import platform
import time


def clear():
    system = platform.system()
    if system == 'Windows':
        os.system('cls')
    elif system == 'Linux' or system == 'Darwin':
        os.system('clear')


def get_cls():
    global cls_time, frame0, frame1, frame2, str_sub, code, find_num

    search = []  # 검색 받은 과목
    same = []  # 같은 과목코드 초기화 예정
    samet = []  # 같은 과목코드 같은 시간
    dift = []  # 같은 과목코드 다른 시간
    tempo = []  # 임시사용 초기화 예정

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
            # print('getcls err')
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
        # print('frame0 err')
        pass
    try:
        frame1.columns = column
    except:
        # print('frame1 err')
        pass
    try:
        frame2.columns = column
    except:
        # print('frame2 err')
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
            # print(soup)
        except EOFError:
            # print('get_all err')
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


def get_list():
    temp_list = []
    f = open(semester + '.txt', 'r')
    lines = f.readlines()
    for line in lines:
        line = line[:10]
        if len(line) != 10 or line.isalnum() != True:   # 잘못된 코드 입력
            continue
        temp_list.append(line)
    f.close()
    return temp_list


def write_list(code_list):
    f = open(semester + '.txt', 'w')
    for data in code_list:
        f.write(data)
        f.write('\n')
    f.close()


if __name__ == "__main__":
    basic = ['subj_class_cde', 'subj_nm', 'unit', 'prof_nm', 'lect_wk_tm', 'lect_quota', 'lect_req_cnt']
    column = ['코드', '과목명', '학점', '교수명', '시간', '수강정원', '수강인원']
    list_subject = []

    tempo0 = []
    x = {}
    y = {}
    difcm = []  # 다른 과목코드 같은 시간
    difcg = []  # 다른 과목코드 같은 시간

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
    clear()

    while True:
        try:
            list_subject = get_list()
            print('-----현재 관심 종목 리스트-----')
            for i in range(len(list_subject)):
                print(i, ": ", list_subject[i])
            print('-------------------------')
        except FileNotFoundError:
            print('현재 관심 종목이 없습니다.')
        temp = input('다음중 원하는 행동을 선택해 주세요(1: 관심 과목을 추가하기 2: 관심 과목 삭제하기 3: 계속 진행하기): ')
        if temp == '1':
            code_all = input("추가하려는 관심 과목 코드를 입력해 주세요.: ")
            if len(code_all) != 10 or code_all.isalnum() != True:  # 잘못된 코드 입력
                print('잘못된 과목코드가 입력 되었습니다. 다시 입력해 주세요.')
                time.sleep(1)
                clear()
                continue
            list_subject.append(code_all)
        elif temp == '2':
            code_all = input("삭제하려는 관심 과목 코드 혹은 번호를 입력해 주세요: ")
            if code_all.isdigit() and int(code_all) < len(list_subject):
                del list_subject[int(code_all)]
            elif len(code_all) != 10 or code_all.isalnum() != True:  # 잘못된 코드 입력
                print('잘못된 과목코드가 입력 되었습니다. 다시 입력해 주세요.')
                time.sleep(1)
                clear()
                continue
            else:
                list_subject.remove(code_all)
        elif temp == '3':
            clear()
            break
        write_list(list_subject)
        clear()

    while True:
        try:
            print('-----현재 관심 종목 리스트-----')
            for i in range(len(list_subject)):
                print(i, ": ", list_subject[i])
            print('-------------------------')
            codeSearch = input("검색하고자 하는 과목 코드 혹은 위에 리스트의 번호를 입력해 주세요: ")
            if codeSearch == 'all':
                get_all(list_subject)
            elif codeSearch == '' and code != '':
                pass
            elif int(codeSearch) < len(list_subject) and codeSearch.isdigit():
                code = list_subject[int(codeSearch)]
            else:
                if len(codeSearch) != 10 or codeSearch.isalnum() != True:
                    print('잘못된 과목코드가 입력 되었습니다. 다시 입력해 주세요.')
                    time.sleep(1)
                    clear()
                    continue
                code = codeSearch
            code_subj = code[:7]  # 과목 분류
            code_class = code[7:]  # 분반 세자리
            num_class = int(code[9:])  # 분반 한자리
            str_sub = str_1 + semester + str_2 + str_3 + code_subj  # 검색한 과목과 같은 과목들 표시
            str_obj = str_a + semester + str_b + code_subj + str_c + code_class + "%27"
            # print(str_sub)
            get_cls()
            # print("\n")
            clear()
            print("{0:.^70}".format("검색하신 과목 현황", end="\n\n\n"))
            print(frame0, end="\n\n")
            print("{0:.^70}".format("같은 시간의 같은 과목들", end="\n\n\n"))
            if frame1.empty:
                print('\t같은 시간의 같은 과목이 없습니다.')
            else:
                print(frame1, end="\n\n")
            print("{0:.^70}".format("다른 시간의 같은 과목들", end="\n\n\n"))
            if frame2.empty:
                print('\t다른 시간의 같은 과목이 없습니다.')
            else:
                print(frame2, end="\n\n")
            print('================================================')
        except:
            pass