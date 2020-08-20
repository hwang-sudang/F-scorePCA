# < PCA를 이용한 F-Score 투자 기법의 설명력 검증 >
PCA 기법을 활용한 기존 F-score 투자전략 재해석

2020 AIT 1 Project  김지은, 황수정
보고서 본문 : https://www.notion.so/sudang2020fba/PCA-F-Score-e04e27ea47364b2bafdc5eec622b11ab


## Index

1. Purpose
2. F-score definition
3. About Data
4. Preprocessing 
5. PCA
6. Results
7. Summary & Discussions
    References
 
 
 
# 1. P**urpose**

> *재무제표 데이터를 이용해 **F-score**에 해당하는 지표(9개)를 구하고 주성분 분석(PCA)을 통해 재무제표 내용을 대표하는 주성분이 존재하는지 찾는다.*

# 2. **F-score definition**

*Joseph D. PIOTROSKI,  ⌜Value Investing: The Use of Historical Financial Statement Information to Separate Winners from Losers⌟*

### F-Score란?

F-score란 재무제표를 기반으로 기업의 수익성, 재무성과, 영업 효율성에 따라 1 또는 0 값을 부여하여 향후 투자 수익률이 높을 가능성이 있는 기업을 선정하는데 사용하는 지표이다. 

### 선행 연구

- Piotroski는 **저PBR (고 Book-to-Market)**인 기업 주식의 평균 return은 연 7.5% 이상 증가하고,

    **수익성**(**high BM**(book to market value)) **= Book value(장부가치) of firm/ market value(주식가치) of firm  * 100**

    **저PBR = Book-to-Market의 역수**

- 전체적인 실현리턴(realized return)의 분포는 오른쪽으로(Positively Skew) 기울었다.
- 우수한 성과는 낮은 주가와 독립적 관계.
- **시장은 처음에 과거 정보를 축소 반영하는 경향이 있다.**

    ⇒ 따라서 초기 정보가 주는 **signal과 High BM주식의 수익률은 (+)의 관계**

### F-score에 포함되는 9가지 Factors




- 위의 표에서 개별 지표의 **조건을 만족**하면 **F-score값이 1점 증가**한다.
- Piotroski는 **저PBR 종목의 수익률을 증대시키기 위해** F-score를 적용했다.
- 백테스팅으로 비교한다면 저PBR보다 **저PBR+F-score를 적용할 때의 수익률이 더 증가**한다.
- 그러나, F-score의 9개의 지표에서 7-9점의 주식을 매수하는 것이 Piotroski의 F-score 전략이지만, **어떤 지표가 우량주를 대표하는 지, 미래 수익에 영향을 주는 지에 대한 논의는 지속되고 있다.**

[F-Score 전략](https://m.blog.naver.com/mymoneymoney/221232481172)

# 3. About Data

### 데이터 출처

- KISVALUE

### 데이터 선정기준

- KOSPI 전 종목
- 2000~2019년 연 데이터
- 데이터 종류

# 4. **Preprocessing**

## ✅전체적인 전처리 단계

1. **저PBR (고 Book-to-Market) 상위 100 주 선정**
2. **저PBR 100주의 F-score 9개 지표 연산**
3. **저PBR 100주의 return 연산**
4. **F-score 기준에 따라 0,1 시그널 부여**
    - Long only, Long Short
5. **PCA를 위한 정규화**
6. **PCA 실행**

## ✅각 단계 전처리 단계

1. **인덱싱 조정 : MultiIndexing**
2. **종목코드에 맞는 자산만 pick or throw away**
3. **NaN값 처리 : 모든 factor가 0인 종목은 아예 삭제**

### ✔️저PBR (고 Book-to-Market) 상위 100 주 선정 & 인덱싱 조정

1. 100개 데이터 추출 (정렬해서 낮은 기업 기준으로) 
2. 우선 기업 정보에 해당되는 번호와 년도를 index로 설정(multi index) 

```python
#인덱싱
#일부만, 그리고 자동화 해야할 부분
import numpy as np
import pandas as pd
roa=pd.read_csv("/Users/hwangsujeong/FBA/새 폴더/f_score/roa.csv",
               encoding="UTF-8",index_col='Unnamed: 0') #수익성
roa.index=roa.index.map('{:06d}'.format)
```

### ✔️**종목코드에 맞는 자산만 pick or throw away**

```python
# null 값 처리
# 두 종목으로 우선 대충 삭제할 종목을 확인
k=roa.isna().sum()
q=cfo_new.isna().sum()
f=pd.concat([k,q], axis=1)

# 삭제할 종목 목록 정리해서 구하기
k1=roa.isna().sum(axis=1).reset_index()
stocks_drop=list(k1[k1.iloc[:,-1]==20]["index"]) #ㅇdrop_stocks 구한거
stocks_drop

#----------------------------------------------------------------
# 드롭 실행
# 함수화 해야 할 부분
roa1=roa.copy().reset_index()
roa_mask = roa1[~roa1['index'].isin(stocks_drop)].set_index(["index"])

# 드롭 후 다시 멀티인덱싱
df_roa=roa_mask.stack(dropna=False)
```

⇒ 결과 취합 본은 바로 아래 표 그림을 참조.

### ✔️F-Score Scoring

- **연산을 통해 F-score 지표 계산**

```python
# F-score 지표만들기
# 또 문제: 여기서 가로로 가야되는데.... 홀리....
# 모든 연산을 transepose 후 진행.

roa=netincome_100.T/asset_100.T  #수익성 roa

cfo_new=cfo_100/asset_100  # 영업현금흐름, 영업현금흐름/총자산

roa_chg=roa/roa.shift(1) # dela roa

cfo_roa=cfo_new.T-netincome_100.T # cfo-roa 

#장기부채 : 비유동부채로 간주하고 진행.
debt_chg=lq_debt_100.T/lq_debt_100.T.shift(1)

#유동비율
lq=lq_asset_100/lq_debt_100
lq_chg=lq.T-lq.T.shift(1) # delta liquid

#EQUISS
equiss_new=equiss_100.copy()
equiss_new.fillna(0, inplace=True)
equiss_new[equiss_new > 0]=1 

#영업효율성
margin=gross_100.T-gross_100.T.shift(1)

#총자산 회젼율 차이: 헐 이거 매출액/자산총계
#매출액이랑 return 따로 구하기 ㅠㅠ
```

- **기준에 따라 1,0 으로 점수 부여 ⇒ 총 합으로 "F-score" 도출.**

```python
df_tf["ROA"]=(df1["ROA"]>0)*1 # ROA Weight
df_tf["CFO"]=(df1["CFO"]>0)*1 # CFO
df_tf["d_ROA"]=(df1["d_ROA"]>1)*1 # ROA delta
df_tf["CFO-ROA"]=(df1["CFO-ROA"]>0)*1 # CFO-ROA
df_tf["d_Debt"]=(df1["d_Debt"]>0)*1 # d_Debt
df_tf["d_Liquid"]=(df1["d_Liquid"]>0)*1 # d_Liquid
# d_Equiss 는 이미 처리되어 있음
df_tf["Margin"]=(df1["Margin"]>0)*1 # Margin
df_tf["Turn"]=(df1["Turn"]>0)*1 # Turn
```
### ✔️F-score 로 Long Only, Long Short Signaling

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9ec43578-37c9-4b64-8b01-77bb0dbd4e0e/_2020-04-18__1.56.40.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9ec43578-37c9-4b64-8b01-77bb0dbd4e0e/_2020-04-18__1.56.40.png)

                **< Long Short >**

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d15cf325-eb0d-4923-892c-524e83d39b0b/_2020-04-18__1.56.51.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d15cf325-eb0d-4923-892c-524e83d39b0b/_2020-04-18__1.56.51.png)

                   **< Long Only >**

### 🚴🏿‍♀️Long, Short 기준

- Long : F-score ≥ 7  ⇒ Signal = 1
- Short : F-score ≤ 2 ⇒ Signal = -1

**코드** 

```python
# Signals 배열
Signals=pd.DataFrame(np.zeros_like(F_Score.copy()),index=F_Score.index,columns=["signal"])
#Signals["F_score"]=(df1["ROA"]>0)*1 

Signals1=(F_Score["F-Score"]>=7)*1 # Long only
q1=(F_Score["F-Score"]<=2)*(-1)
Signals["signal"]=Signals1+q1  # Long short
```

### ✅5. PCA를 위한 정규화

주성분 분석을 하기 위한 정규화 

- 분산 증가량에 따라 판단하기 때문에 데이터의 단위가 중요한 요인으로 작용한다. 이에 [0,1] 범위 내의 값을 가지도록 정규화를 실시했다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8f279787-8e87-4aa8-a40a-0ee88e0f5bec/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8f279787-8e87-4aa8-a40a-0ee88e0f5bec/Untitled.png)

```python
#regularization
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df[:] = scaler.fit_transform(df[:])
```

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8edf0fb4-33ab-4d2a-8725-99c2b86f4bd6/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8edf0fb4-33ab-4d2a-8725-99c2b86f4bd6/Untitled.png)

# 5. **PCA(Principal Component Analysis)**

**PCA definition**

고차원 데이터 집합이 주어졌을 때, 원래의 고차원 데이터와 가장 유사하면서 더 낮은 차원의 데이터를 찾아내는 방법이다. 주성분을 이용해 데이터를 표현하도록 변환을 하는 것으로 전체 데이터의 분산을 가장 잘 설명하는 축의 개수를 선정한다. 낮은 차원의 데이터로 높은 차원의 데이터를 설명할 수 있다는 것을 의미하므로 차원축소(dimension reduction)라고도 한다. 

**1) 주성분(n_components=2)** 

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e9d1fea1-5bdb-432b-a607-b67a65bc4985/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e9d1fea1-5bdb-432b-a607-b67a65bc4985/Untitled.png)

2개의 주성분이 전체 분산의 약 85%를 설명한다. 첫번째 주성분의 설명량은 0.68, 두번째 분산의 설명량은 0.17이다. 따라서 2개의 주성분이 데이터를 충분히 설명하지 못한다고 판단하여 3개의 주성분의 분산 설명량을 구해보았다. 

**2) 주성분 분석 (n_components=3)**

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/16a7b1a4-ad97-4279-8853-7620dc72683b/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/16a7b1a4-ad97-4279-8853-7620dc72683b/Untitled.png)

3개의 주성분이 전체 분산의 약 90%를 설명한다는 것을 확인할 수 있다.  추가적인 주성분을 투입하였을 때 설명가능한 분산량이 일정 기준 이상 증가하였으므로 주성분은 세 개로 결정하는 것이 적절하다. 

지은이 굿... *^-^*

<choose number of components>

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/42af616d-4ada-4dfe-9321-a79b133f0787/Figure_2.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/42af616d-4ada-4dfe-9321-a79b133f0787/Figure_2.png)

-**xlabel:** number of components

-**ylabel**: cumulative explained variance

# 7. Summary & Discussions

### 🚩Implications, Complementary Points

- PCA 설명 **당위성**?
    - 방법론의 변경
- **주성분을 이용해 투자할 수 있는 방법 모색**
- **논문 내용대로 정석으로 분석할 것** → 시간 관계 상 퀀트 블로그 참조.
- 데이터 **전처리 과정에서의 오류** 검토
- 재무 데이터 **분기별 데이터**로 처리하면 더 정확할 것이다.
- **백테스팅**과 **kospi 200 수익률 (벤치마크)**과 비교 필요 🌟

    (수익률, MDD, R-square등 )

- 전처리 과정에서의 **하드코딩 자동화 필요성** → 함수를 이용
- 26강 내용 관련 부분을 조금 더 심화학습하면, PC가 투자에 있어서 어떠한 가중치를 주거나, 의사결정에 도움이 될 가능성 환기

    []()

### 🚩Summary

2개의 주성분은 전체 분산의 약 85%, 3개의 주성분은 전체 분산의 약 90%를 설명한다. F-score의 9개의 지표에서 7-9점의 주식을 매수하는 것이 Piotroski의 F-score 전략이다. 위 과정을 통해 대표하는 세 가지 주성분을 발견할 수 있었고 특정 지표의 대표성은 알 수 없지만 미래의 수익에 영향을 주는 성분이 존재한다는 것을 프로젝트를 통해 확인할 수 있었다. 

# References

- F-Score 논문

    ***Joseph D. PIOTROSKI,  ⌜Value Investing: The Use of Historical Financial Statement Information to Separate Winners from Losers⌟***

    [b030da18ab28d1e1a1bbf7e33fb5911f189e.pdf](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/26e313b0-cde5-4d51-af05-dbe8112636d3/b030da18ab28d1e1a1bbf7e33fb5911f189e.pdf)

- F-Score 요약 블로그

[F-Score 전략](https://m.blog.naver.com/mymoneymoney/221232481172)
