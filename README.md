# 경북대 수강신청 잔여 자리 찾기(아직 작업중!!!)

경북대 수강신청시 내가 수강하고 하는 과목의 잔여자리와 그와 같은 과목코드를 가진 과목들의 잔여자리를 한번에 확인할 수 있도록 만든 프로그램이다.   
같은 과목코드를 가진 강의들은 내가 검색한 과목과의 시간을 기준으로 같은 시간인지 다른 시간인지 구분된다.


## Table of Contents

- [설치 방법](#설치-방법)
- [사용법](#사용법)


## 설치 방법
설치 방법에는 2가지 방법이 있다.
### 1. 파이썬을 이용하는 방법   
main.py를 다운받아서 실행시키면 된다.   
사용된 파이썬 패키지   
<pre><code>from bs4 import BeautifulSoup
from pandas import DataFrame
import requests
import os
import platform
import time</code></pre>
### 2. exe 파일을 사용한 방법   
[exe파일 다운로드 링크](http://gofile.me/4Di5L/r7QEOhKPu)   
exe 파일을 실시킨다.   
실행시 화면이 출력될 때까지 시간이 좀 소요된다...

## 사용법
시작화면입니다!
![시작화면](https://user-images.githubusercontent.com/49528515/106889792-d59ca680-672b-11eb-82f3-92374e945954.PNG)
처음 실행하면 관심종목이 없어요   
1번을 눌러 관심종목을 추가할수 있고 2번을 눌러 관심 종목을 삭제할수 있습니다.   
![관심과목 첫화면](https://user-images.githubusercontent.com/49528515/106889852-ecdb9400-672b-11eb-801d-e58eb5689603.PNG)
관심종목을 추가하고 나면 이런 화면이 나옵니다   
![관심종목 저장](https://user-images.githubusercontent.com/49528515/106889899-fc5add00-672b-11eb-9853-4d2d7cf64391.PNG)
3번을 누르고 넘어가면 아래같은 화면이 나옵니다    
과목코드를 입력하거나 관심종목 번호를 입력하여 검색할수 있습니다   
![검색할 리스트](https://user-images.githubusercontent.com/49528515/106889940-0b418f80-672c-11eb-9a54-a538585344fc.PNG)
검색한 결과는 다음과 같이 내가 검색한 과목의 시간을 기준으로 구분하여 알려줍니다!   
![검색과목 현황](https://user-images.githubusercontent.com/49528515/106890294-73907100-672c-11eb-8625-ec800b286eb5.PNG)

## 코드구성
<pre><code>def clear()</code></pre>
사용자 터미널(cmd)창 내용 지우기
<pre><code>def get_cls()</code></pre>
사용자 검색 과목을 받아 크롤링   
크롤링 결과를 검색 과목 시간을 기준으로 분류   
분류한 자료를 데이터프레임에 저장
<pre><code>def get_all()</code></pre>
사용자의 관심종목 리스트를 받아 크롤링   
크롤링 결과를 데이터프레임에 저장
<pre><code>def get_list()</code></pre>
입력받은 학기 정보와 같은 이름의 txt 파일을 받아와 저장되어 있는 관심 종목을 리스트에 저장   
<pre><code>def write_list()</code></pre>
관심 종목 리스트를 파일로 저장
<pre><code>__main__</code></pre>
학기정보를 입력 받음   
get_list() 함수를 호출
관심종목 추가 여부를 확인
검색하고자 하는 과목 코드를 입력 받음
검색 결과 
