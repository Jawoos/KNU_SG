# 경북대 수강신청 잔여 자리 찾기

경북대 수강신청시 내가 수강하고 하는 과목의 잔여자리와 그와 같은 과목코드를 가진 과목들의 잔여자리를 한번에 확인할 수 있도록 만든 프로그램이다.   
같은 과목코드를 가진 강의들은 내가 검색한 과목과의 시간을 기준으로 같은 시간인지 다른 시간인지 구분된다.
---
## 목차

- [설치 방법](#설치-방법)
- [사용법](#사용법)
- [코드 구성](#코드-구성)
    - [KNUS_alpha.py](#KNUS_alphapy)
---
## 설치 방법

설치 방법에는 2가지 방법이 있다.
### 1. 파이썬을 이용하는 방법   
main.py를 다운받아서 실행시키면 된다.   
사용된 파이썬 패키지   
```{.python}
from bs4 import BeautifulSoup
from pandas import DataFrame
import requests
import os
import platform
import time
```

### 2. exe 파일을 사용한 방법   
[exe파일 다운로드 링크](http://gofile.me/4Di5L/K7CLU5Iea)   
exe 파일을 실시킨다.   
실행시 화면이 출력될 때까지 시간이 좀 소요된다...
---
## 사용법
####시작화면입니다!
![시작화면](https://user-images.githubusercontent.com/49528515/106889792-d59ca680-672b-11eb-82f3-92374e945954.PNG)
#### 처음 실행하면 관심종목이 없어요   
#### 1번을 눌러 관심종목을 추가할수 있고 2번을 눌러 관심 종목을 삭제할수 있습니다.   
![관심과목 첫화면](https://user-images.githubusercontent.com/49528515/106889852-ecdb9400-672b-11eb-801d-e58eb5689603.PNG)
관심종목을 추가하고 나면 이런 화면이 나옵니다   
![관심종목 저장](https://user-images.githubusercontent.com/49528515/106889899-fc5add00-672b-11eb-9853-4d2d7cf64391.PNG)
#### 3번을 누르고 넘어가면 아래같은 화면이 나옵니다    
#### 과목코드를 입력하거나 관심종목 번호를 입력하여 검색할수 있습니다   
![검색할 리스트](https://user-images.githubusercontent.com/49528515/106889940-0b418f80-672c-11eb-9a54-a538585344fc.PNG)
#### 검색한 결과는 다음과 같이 내가 검색한 과목의 시간을 기준으로 구분하여 알려줍니다!   
![검색과목 현황](https://user-images.githubusercontent.com/49528515/106890294-73907100-672c-11eb-8625-ec800b286eb5.PNG)
---
## 코드 구성
### KNUS_alpha.py
#### 사용자 터미널(cmd)창 내용 지우기
```{.python}
def clear():
    system = 시스템 정보 받기
    if system is 윈도우
        'cls' 명령어 실행
    elif system is 리눅스 혹은 맥
        'clear' 명령어 실행
```
#### 입력된 과목과 같은 과목 크롤링 및 데이터 정리
```{.python}
def get_cls():
    tempo = 임시 저장 리스트
    samet = 같은 시간 과목 리스트
    dift = 다른 시간 과목 리스트
    html = 과목 정도 받아오기
    soup = bs4 사용(html.parser)
    b = 클라스로 과목정보 찾기
    for i less then len(basic):
        b에서 과목 정보 리스트로 받기
        과목 정보를 tempo에 저장
        if 사용자가 검색한 과목
            find_num = 인덱스 번호 저장
    for i less then len(tempo):
        if 사용자 검색 과목과 같은 시간
            samet에 저장
        else
            dift에 저장
    samet와 dift를 데이타 프레임에 저장하여 출력
```
#### 관심 종목 정보 크롤링
```
def get_all(list_all):  # 관심종목 리스트 인자로 받음
    while j < len(list_all):
        html = 관심 종목 정보 크롤링
        soup = bs4 사용(html.parser)
        className = soup.find 과목명
        ProfName = soup.find 교수명
        classCode = soup.find 과목코드
        max_per = soup.find 과목 정원
        now_per = soup.find 현재 수강인원
        print(과목정보들)
```
#### 저장되어있는 관심종목 읽어오기
```
def get_list():
    temp_list = 관심 과목 받을 리스트
    f = 입력한 학기와 같은 이름의 txt 파일 open
    lines = read lines from f
    for line in lines:
        line = line의 앞 10글자만 받기
        if len(line) != 10 or line이 영어 혹은 숫자로만 이루어지지 않았다면:   # 잘못된 코드 입력
            continue
        temp_list에 line 저장
    f.close()
    return temp_list
```
#### 입력받은 관심 종목 업데이트
```
def write_list(code_list):  # 관심종목 리스트 인자로 받기
    f = 입력한 학기와 같은 이름의 txt 파일 open
    for data in code_list:
        f에 데이터 입력
    f.close()
```
#### 메인 함수
```
__main__
    basic = 과목 구성 정보 리스트
    column = 과목 구성 정보 이름
    list_subject = 관심종목 리스트
    
    semester = 학기 정보 입력 받기
    while True:
        print(관심종목)
        temp = 관심 종목 추가, 관심 종목 삭제, 다음으로 넘어가기 중 선택
        if 관심종목 추가:
            code_all = 관심종목 코드 입력 받기
            관심 종목 소문자 전부 대문자로 변환
            관심 종목이 유효한지 검사
            list_subject에 저장
        elif 관심 종목 삭제:
            code_all = 관심종목 코드 혹은 리스트 번호 입력 받기
            관심 종목 소문자 전부 대문자로 변환
            관심 종목이 유효한지 검사
            if 리스트 번호:
                해당 리스트 번호 삭제
            else:
                과목코드 유효성 검사
                list_subject에서 삭제
        else:
            break
    while True:
        print(현재 관심 종목 리스트)
        codeSearch  = 검색하고자 하는 과목코드 혹은 관심 종목 리스트 번호
        codeSearch 소문자 전부 대문자 변환
        if codeSearch == 'ALL'
            get_all(list_subject)으로 관심 종목 현황 표시
            continue
        elif codeSearch == 리스트 번호:    
            code = 리스트 번호에 해당하는 관심 과목 코드
        else:
            과목코드 유효성 검사
        get_cls()로 검색한 과목에 대한 정보 받아오기
        clear()
        print(검색한 과목 정보)
        print(검색한 과목과 같은 시간 정보)
        print(검색한 과목과 다른 시간 정보)
```