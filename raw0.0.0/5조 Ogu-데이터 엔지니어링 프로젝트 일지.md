# 데이터 엔지니어링 프로젝트 일지

## 5조 Ogu



## 8월 4일 (수)

### 관심분야에 대한 토론을 진행함

김민형

- 도지코인, 비트코인
- 교통
- 식품
- 고객성향 분석

박경빈

- 주식
- 교육(수학,코딩)
- 스포츠(야구,축구)
- 커피(카페 추천 앱)
- 옷(온라인,오프라인 매출,흐름)

조민호

- 주식
- 게임
- 스포츠(야구)
- 여행

최원희

- 주식
- 식료품 매출
- 여행(에어비앤비) - `https://github.com/gogoj5896/2_teamproject_air_bnb_ligression`



## 8월 6일(금)

### 주제로 선정할 것을 토론하고  관련 데이터 셋을 모으는 작업을 진행함

- 유니버셜

`https://www.kaggle.com/dwiknrd/reviewuniversalstudio`

- 유기견

`https://www.kaggle.com/jmolitoris/adoptable-dogs`

- 롤

`https://www.kaggle.com/gyejr95/league-of-legendslol-ranked-games-2020-ver1?select=challenger_match.csv`

- 한국 혐오 언어

`https://www.kaggle.com/captainnemo9292/korean-extremist-website-womad-hate-speech-data`

- e러닝

`https://www.kaggle.com/c/learnplatform-covid19-impact-on-digital-learning/discussion?sort=votes`

`https://www.kaggle.com/ruchi798/covid-19-impact-on-digital-learning-eda-w-b`

- 한국 코로나 바이러스

`https://www.kaggle.com/kimjihoo/coronavirusdataset`

`https://github.com/ThisIsIsaac/Data-Science-for-COVID-19`

`https://www.kaggle.com/mbnb8317/ds4c-tutorial-all-about-folium-pydeck?scriptVersionId=35512489`

- 책

`https://www.kaggle.com/sootersaalu/amazon-top-50-bestselling-books-2009-2019`

- 삼성

`https://www.kaggle.com/hyunkic/south-korea-home-to-samsung-but-few-ai-experts`



## 8월 7일(토)

### 주제 선정 및 데이터 수집&전처리 과정 토의

주제:한국의 코로나 상황

데이터 수집:`data.go.kr`의 OPEN API를 통해서 데이터 수집

최종적으로 원하는 모습:코로나 라이브 `https://corona-live.com/`

전처리 과정:스파크와 AWS를 사용. 모은 데이터를 태블로라는 대쉬보드를 통해 보여줄 예정. 
                    스파크와 AWS를 어떻게 사용해야 할 지 토론을 함.



## 8월 9일(월)

### 스파크,AWS 사용 방법에 대해 토론 및 기획안 작성 

**스파크**

강사님의 조언 : 스파크의 df형태로 저장 - 하둡의 HDFS 형태로 저장, df(테이블 형태)저장된 것을 추출하여 시각화 

- 질문(csv파일로 df 구축하는 것은 의미?) : 정형 데이터를 로컬에서 만들어서, 스파크의 가상머신에서 데이터를 받아서 활용하면 의미없다.

**AWS 서버 구축**

 - 실시간 코로나 데이터 저장 ( 하둡 HDFS, 반정형 데이터 )
 - 반정형 데이터를 정형 데이터로 처리
 - 클라이언트에 정형 데이터를 response 함으로써 코로나 데이터 전송
 - 목표 : 데이터를 aws에 실시간으로 업데이트 되는 서버 구축



## 8월 10일 (화)

### 스파크,AWS,태블로 사용법

1. 데이터 모델의 이해
2. 각 조 Project
   1. 프로젝트 시나리오 구성안 
   2. 데이터 수집 결과
   3. 데이터 수집 solution test결과
   4. 데이터 저장 solution test결과
3. 각 조별 발표
4. 프로젝트 진행 중 Q&A

++ Tip : Linux명령어 찾기

​				http://explainshell.com



## 8월 11일(수)

### 강사님과 질문응답 및 DB 구축

1. OSI 7 Layer와 Internet
2. 각 조 Project
   1. 프로젝트 시나리오 구성 안
   2. 데이터 수집 결과
   3. 데이터 수집, 저장 Process 구현안 발표
3. 각 조별 발표
4. 프로젝트 진행 중 Q&A

**HDFS 입출력 실습 예제(java 버전)**

http://hisoftlab.com/4832

- hadoop file system이 어떻게 작동하는지? 



**질문**

서버에서 hdfs 작동할때 file로 자동으로 저장되는건지?

서버 내 db설치하는 경우?

- hdfs <> mysql 
  - db연결시 어떤 흐름인지 (그림으로 표현된다면?)

- db <> hdfs

- 파일 저장시 스파크쉘에서 저장?
  - 파이썬 저장 - 스파크쉘에서 파이썬 파일 불러옴
- 스파크 플랫폼이 hdfs를 사용하는 것
  - 스파크에서 hdfs로 저장을 시켜줌



**질문 정리**

1.서버에서 hdfs 명령어 썼을 때 hdfs 저장된거로 나와있는데 이 과정이 맞는 지 궁금합니다.

2.서버 내의 데이터베이스를 설치할 경우에 대해서도 물어봐야겠습니다. 제가 궁금한 것은 hdfs그 부분이랑 우리가 알고 있는 mysql을 연결시키면 어떤 흐름도가 되는지 궁금합니다.

3.DB랑 hdfs랑 경계가 애매모해서 문제가 되는 거 같습니다.둘 사이의 차이가 거의 없는 거 같은데 그러면 두 프로그램 중 하나만 사용해도 상관없는거 아닌가요?



**질문 답변**

AWS 에서 하나의 파이썬 코드로 정리

 - api 통해서 데이터 가져오고
 - 데이터를 RDD 형태로 저장
 - RDD 저장하는 코드가 나와야 하는데, 이것이 scala or python이 될 것

RDD로 만든 후 스파크 명령어로 쓰면, 일반 파일로 저장하는 것보다 빠르다

- python이 됐든, 스칼라가 됐든 spark 명령어를 통해서 저장을 하면, 일반 파일로 저장하는 것보다 훨씬 속도가 빠르다!

- 분산 처리가 가능해진다!



**데이터 처리**

pyspark로 파이썬 파일 작성 후 돌림

코드 내에서 파일 저장 등 처리

- 참고 -  PySpark로 데이터를 읽고 쓰는 방법

https://ichi.pro/ko/spark-essentials-pysparklo-deiteoleul-ilg-go-sseuneun-bangbeob-101455223728077



**++ 서버 사양**  

※ HW 

- 고주파수 인텔 제온 E5-2686 v4(Broadwell)급 프로세서, DDR4 메모리 
- 4vCPU / 30.5GB 급 RAM / 1000GB SSD 
- Ubuntu 18.04 0S 
- mxnet, tensorflow, caffe2, chainer, cntk, pytorch 등으로 이루어진 가상환경 有 

※ SW 

- Anaconda3 / python 3.7.6 -

- spark-3.1.2-bin-hadoop3.2(단일 머신) 설치 

  -  hadoop fs -cat dfDecide.csv
  -  lab18@ip-172-31-9-66:/home/lab17$ hadoop fs -cat dfDecide.csv

- 기타 : (base) Anaconda 환경에서 TensorFlow, Keras 등 

  ​		    머신러닝, 딥러닝 관련 패키지 및 라이브러리 추가 설치 가능

 

**EC2 > Local**

키파일 폴더에서 cmd실행

터미널 창 뜨면

$C:~/~/~>pscp -i "de-a5.ppk" lab18@52.78.90.155:/home/lab17/test/*.csv C:\Users\ftsv2\Desktop

>pscp -i "de-a5.ppk" lab18@52.78.90.155:/home/lab17/dfDistrict.csv C:\Users\ftsv2\Desktop              

corona.py    

​                                                                                                        

**Spark 파트**

 - api 통해서 데이터 가져오고
 - 데이터를 RDD 형태로 저장
 - RDD 저장하는 코드가 나와야 하는데, 이것이 scala or python이 될 것
 - 하나로 합치려면 pyspark가 어울릴 것으로 보이지만, 계속 진행해봐야 알 것 같다.

**태블로 파트**

- Spark SQL을 이용해서 태블로와 연결하는 방법을 진행하고 있고,
  이것이 힘들 경우, csv or json 파일을 태블로로 불러와서 대쉬보드화 하는 것을 고려하고 있다.



## 8월 12일(목)

### DB 구축 및 태블로 시각화

**일정**

1. open software 활용과 경진대회 예제
   **open source software 사이트** : `https://www.oss.kr/`

2. 각 조 Project
   1. 데이터 수집 sample 정제 결과 발표
   2. 저장 Process 구현 안 발표
3. 각 조별 발표
4. 프로젝트 진행 중 Q&A

Spark 파트

1. 날짜별 지역별로 df 정리되는 코드
2. 파이스파크를 통해서 파일로 내보내는 코드

태블로 파트

1. 코로나 관련 정제 데이터를 태블로에서 연결
2. 지리적 정보, 날짜 정보 변수 설정
3. 대시 보드 초기 적용



**HDFS에 저장**

df\
.write\
.mode("overwrite")\
.format("com.databricks.spark.csv")\
.save("/user/kidokim509/data.csv")

**pySpark이고 DN에 pandas가 설치 되어있다면**

df.\

toPandas().\
to_csv("data.csv")



시군구의 17개의 데이터를 컬럼으로 변경 후 날짜별로 csv파일로 만듬

pyspark

파이썬 내의 pyspark라이브러리에서 rdd형태 사용가능

- hdfs에 저장
- 파이썬 코드로 만들면 어케 rdd로 만들어서 hdfs에 저장하겠는가?
- rdd저장
- 판다스 df를 스파크의 rdd df만드는것은 가능

scala에서 rdd

13장 참고



**hadoop 작동 방식 ?**

aws내에서 

파이썬에서 판다스로 내부의 df메서드를 csv 파일로 해당 hdfs저장

df가 csv 로 저장

pyspark에서 rdd- > df

> hdfs df

df_test = spark.read.csv('dfDecide.csv', header=True)
df_test.show(5)

hdfs형태는 분산되어서 저장



**HDFS에 저장**
df1\
.write\
.mode("overwrite")\
.format("com.databricks.spark.csv")\
.save("data222.csv")



위에 날짜

지도 선택을 하면 

1. 확진자 
2. 사망자

3. 격리해제



치명률 - 확진자의 상관관계를 시각화

- 치명률 매개변수 생성!!

100% 기준으로 누적차트로  치명 - 확진자



돌파감염 수치로 보는거?

코로나 사망자 수 <> 백신 부작용 사망자 수

- 7월 3일 기준 509명



**백신 부작용 사망자**

1800명 중 500명 1/3.8

**코로나 사망자**

16만명 중 2천명 1/8



**wrap-up**

**Spark 파트**

- pyspark 라이브러리를 통해서 스파크 RDD를 통해서 분산 저장 가능, 완료 

- Read - write까지 거의 OK

- 데이터 정제 작업 진행 완료

**태블로 파트**

1. 코로나 관련 정제 데이터를 태블로에서 연결
   ( raw 데이터도 가능할 것으로 판단 )
   2.대쉬보드 큰 그림 구상
    — 여기까지 완료
2. 지리적 정보, 날짜 정보 변수 설정
3. 대시 보드 초기 적용

**1조의 도움**

open api를 mongoDB에 저장을해서
spark로 데이터를 처리하면
비정형 데이터가 정형 데이터로 바뀌나봄
그 상태에서 다시 MySQL로 보내서 저장



## 8월 13일(금)

### DB 구축 및 태블로 시각화

1. 빅데이터 3대 요소
2. 빅데이터 기술
3. 각 조 Project (Documanet 보강)
   1. 데이터 수집
   2. 저장 Process 구현
4. 각 조별 발표
5. 프로젝트 진행 중 qna



**spark 파트**

- aws서버 접속 `ubuntu` 로 로그인 → root 계정에서 mysql설치
- aws서버 내에서 계정 발급
- 각 조원들에게 접근 권한 부여, 각 local환경에서 mysql 서버 접속
- 공통 DataBase접근 성공



**태블로 파트**

- 태블로 ↔ mySQL 연동 성공
- spark 파트에서 생성한 DB에 접속하여 테이블 접근 성공



**<해야 할 것>**

**spark 파트** : pyspark의 DataFrame을 aws서버의 mysql 데이터베이스에 저장

pyspark로 mySQL 액세스

**태블로 파트** : 생성된 테이블 데이터를 활용하여 대쉬보드(시각화)제작 진행

태블로에서 HDFS 연결



root 계정 사용법 

- aws 서버 ubuntu 로그인 

- $sudo 

우분투 root 에서 aws내에 mysql설치

aws내에 계정 발급

권한 - 로컬 pc에서 mysql 서버 접속 - db 접근

태블로 - mysql연동



pyspark에 df를 aws서버의 mysql 데이터베이스에 저장

jupyter-notebook --ip=0.0.0.0 --no-browser --port=8907

김민형 : ogu02 / 1234
박경빈 : ogu03 / 1234
최원희 : ogu04 / 1234





> **sql 서버만들기**
>
> https://nickjoit.tistory.com/144

ubuntu 

$sudo su

@root #apt install mysql-server

@root #mysql -u root -p 1234

mysql> use mysql

>  DB changed

mysql> select user from user;

mysql> select user, authentication_string from user;

mysql> create user 'ogu05'@'%' indentified  by '1234'

> 사용자 추가 (권한추가)
> mysql > create user 사용자ID;  // 사용자 추가
>
> mysql > create user userid@localhost identified by '비밀번호';
>
> // 사용자(user)를 추가하면서 패스워드까지 설정
>
> 기존에 사용하던 계정에 외부 접근 권한을 부여하려면, Host를 '%' 로 하여 똑같은 계정을 추가한다
>
> mysql > create user 'userid'@'%' identified by '비밀번호'; // '%' 의 의미는 외부에서의 접근을 허용
>
> 

**권한 주기**

grant insert on corona19.* to 'ogu05'@'%' identified by 1234;



