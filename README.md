# < PCA를 이용한 F-Score 투자 기법의 설명력 검증 > 
PCA 기법을 활용한 기존 F-score 투자전략 재해석

### 2020 AIT 1 Project 구성원
- 황수정 
- 김지은 



## 1. P**urpose**

재무제표 데이터를 이용해 **F-score**에 해당하는 지표(9개)를 구하고 주성분 분석(PCA)을 통해 재무제표 내용을 대표하는 주성분이 존재하는지 찾는다.*

## 2. **F-score definition**
Joseph D. PIOTROSKI,  ⌜Value Investing: The Use of Historical Financial Statement Information to Separate Winners from Losers⌟

### F-Score 투자전략
재무제표를 기반으로 기업의 수익성, 재무성과, 영업 효율성에 따라 1 또는 0 값을 부여하여 향후 투자 수익률이 높을 가능성이 있는 기업을 선정하는데 사용하는 지표이다.

* F-score에 대해 더 자세히 알고 싶다면 > [F-Score 전략](https://m.blog.naver.com/mymoneymoney/221232481172)

## 3. About Data
### 데이터 출처

- KISVALUE
- 2000~2019년 연 데이터

### 데이터 선정기준

- KOSPI 전 종목
- 2000~2019년 연 데이터
- 데이터 종류 
  :PBR (Market Price/Book),당기순이익, 매출총이익, 비유동부채, 영업현금흐름, 유동부채, 유동자산, 유상증자(주식발행초과금), 총자산, 전 종목 월별 종가, 총매출



## 4. **각 파일에 대한 설명**
1. **Low_PBR_30.py**
- 저PBR (고 Book-to-Market) 상위 100 주 선정

2. **Data_adjusting.py**
- 저PBR 100주의 F-score 9개 지표 연산**

3. **저PBR 100주의 return 연산**
4. **F-score 기준에 따라 0,1 시그널 부여**
    - Long only, Long Short
5. **PCA를 위한 정규화**
6. **PCA 실행**


### ✅전체적인 전처리 단계

1. 저PBR (고 Book-to-Market) 상위 100 주 선정
2. 저PBR 100주의 F-score 9개 지표 연산
3. 저PBR 100주의 return 연산
4. F-score 기준에 따라 0,1 시그널 부여
    - Long only, Long Short
5. PCA를 위한 정규화
6. PCA 실행
  '>> 더 자세한 내용은 보고서파일을 참고하세요.

###  ✅각 단계 전처리 단계
1. **인덱싱 조정 : MultiIndexing**
2. **종목코드에 맞는 자산만 pick or throw away**
3. **NaN값 처리 : 모든 factor가 0인 종목은 아예 삭제**


## 5. Summary & Discussion
1) PCA 설명 **당위성**?
   - 요약 : PCA 작동원리 상 해당 투자기법을 대입하는 방법론은 올바른 접근. (교수님피드백)
   - 다만, 성능과 정확도를 비교하기 위해서 다음과 같은 방법론도 고려.
       * Binary Signal로 의사 결정 트리 관련 모델로 차라리 매수,매도,유지 분류...
       * 학습모델의 경우, 서포트 벡터 머신 등을 이용해 시그널 분류도 가능. 
       * But, 정답 데이터 필요하므로 거의 불가능
2) **주성분을 이용해 투자할 수 있는 방법 모색**
3) **논문 내용대로 정석으로 분석할 것** 
    → 이 프로젝트는 시간 관계 상 퀀트 블로그 참조한 내용을 바탕으로 진행.
4)  데이터 **전처리 과정에서의 오류** 검토
  - 재무 데이터 **분기별 데이터**로 처리하면 더 정확할 것이다.
  - **백테스팅**과 **kospi 200 수익률 (벤치마크)**과 비교 필요 🌟 
    (수익률, MDD, R-square등 )

5) 전처리 과정에서의 **하드코딩 자동화 필요성** → 함수를 이용
6) 26강 내용 관련 부분을 조금 더 심화학습하면, PC가 투자에 있어서 어떠한 가중치를 주는지 도출할 수 있다면 실질적으로 유의미한 투자지표를 도출할 수 있을 것이다.

