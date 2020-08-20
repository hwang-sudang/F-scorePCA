
import numpy as np
import pandas as pd



pbr=['003480', '006200', '005010', '002300', '000140', '002220', '000950',
       '016610', '001230', '003830', '001530', '017940', '006370', '005950',
       '000500', '004690', '001080', '071090', '002200', '001750', '003030',
       '015360', '006110', '010100', '009200', '002820', '008110', '010690',
       '001500', '012320', '001200', '071320', '001940', '005800', '010660',
       '006660', '005430', '104700', '003460', '000850', '001070', '023530',
       '129260', '002920', '003570', '004020', '006220', '000680', '004100',
       '025890', '030610', '010770', '001620', '004890', '016880', '001130',
       '002310', '025530', '015760', '024070', '005490', '001790', '018470',
       '084010', '024110', '003530', '007280', '000910', '002710', '004560',
       '092220', '003610', '002070', '000590', '004150', '030210', '013580',
       '002320', '023350', '004970', '036460', '017390', '082640', '103590',
       '034020', '011300', '067830', '082740', '006880', '026940', '009770',
       '019440', '003720', '013870', '001430', '000050', '117580', '033530',
       '003300', '006740']




# csv파일을 일일히 읽어옴. 자동화 방안 마련 필요.
netincome=pd.read_csv("/Users/hwangsujeong/FBA/새 폴더/adjusted_csv/netincome.csv",
               encoding="UTF-8") #당기순이익

gross=pd.read_csv("/Users/hwangsujeong/FBA/새 폴더/adjusted_csv/gross.csv",
                encoding="UTF-8") # 매출총이익

cfo=pd.read_csv("/Users/hwangsujeong/FBA/새 폴더/adjusted_csv/cfo.csv",
                encoding="UTF-8") # 영업현금흐름

lq_debt=pd.read_csv("/Users/hwangsujeong/FBA/새 폴더/adjusted_csv/lq_debt.csv",
                encoding="UTF-8") # 유동부채

lq_asset=pd.read_csv("/Users/hwangsujeong/FBA/새 폴더/adjusted_csv/lq_asset.csv",
                encoding="UTF-8") # 유동자산

equiss=pd.read_csv("/Users/hwangsujeong/FBA/새 폴더/adjusted_csv/equiss.csv",
                encoding="UTF-8") # 신주발행 (유상증자 주발초)

eq_cap=pd.read_csv("/Users/hwangsujeong/FBA/새 폴더/adjusted_csv/eq_cap.csv",
                encoding="UTF-8") # 자기자본

asset=pd.read_csv("/Users/hwangsujeong/FBA/새 폴더/adjusted_csv/asset.csv",
                encoding="UTF-8") # 총자산

non_debt=pd.read_csv("/Users/hwangsujeong/FBA/새 폴더/adjusted_csv/non_debt.csv",
                encoding="UTF-8") # 비유동자산


# 각 지표들의 이름을 담은 리스트 : 쉽게 참조하기 위해서 
indices=["netincome","gross","cfo","lq_debt", "lq_asset", "equiss", "eq_cap", 
        "asset", "non_debt"] # 지표 이름

indices2=[netincome,gross,cfo,lq_debt,lq_asset,equiss,eq_cap, 
        asset, non_debt] # 지표객체 자체를 넣은 리스트




#--------------------------------------------------------------------

# 자동화 실패 : 추후 

def idx_adjust(k):
    
    k["Stock"]=k["Stock"].map('{:06d}'.format)
    k["Stock"]=k["Stock"].map(str)
    k.set_index("Stock")
    
    return k


for i in indices2:
    i.apply(idx_adjust(i))

for i in range(indices2):
    

#indices2.apply(idx_adjust)

#--------------------------------------------------------------


# 날코딩으로 각 인덱스를 바꾸는 작업. 데이터프레임으로 함수로 돌릴 수 있는 방법 모색 필요.
netincome["Stock"]=netincome["Stock"].map('{:06d}'.format)
netincome["Stock"]=netincome["Stock"].map(str)
netincome.set_index("Stock", inplace=True)
netincome=netincome.loc[:,"2000":]

non_debt["Stock"]=non_debt["Stock"].map('{:06d}'.format)
non_debt["Stock"]=non_debt["Stock"].map(str)
non_debt.set_index("Stock", inplace=True)
non_debt=non_debt.loc[:,"2000":]

lq_asset["Stock"]=lq_asset["Stock"].map('{:06d}'.format)
lq_asset["Stock"]=lq_asset["Stock"].map(str)
lq_asset.set_index("Stock", inplace=True)
lq_asset=lq_asset.loc[:,"2000":]

lq_debt["Stock"]=lq_debt["Stock"].map('{:06d}'.format)
lq_debt["Stock"]=lq_debt["Stock"].map(str)
lq_debt.set_index("Stock", inplace=True)
lq_debt=lq_debt.loc[:,"2000":]


equiss["Stock"]=equiss["Stock"].map('{:06d}'.format)
equiss["Stock"]=equiss["Stock"].map(str)
equiss.set_index("Stock", inplace=True)
equiss=equiss.loc[:,"2000":]

cfo["Stock"]=cfo["Stock"].map('{:06d}'.format)
cfo["Stock"]=cfo["Stock"].map(str)
cfo.set_index("Stock", inplace=True)


asset["Stock"]=asset["Stock"].map('{:06d}'.format)
asset["Stock"]=asset["Stock"].map(str)
asset.set_index("Stock", inplace=True)
asset=asset.loc[:,"2000":]


gross["Stock"]=gross["Stock"].map('{:06d}'.format)
gross["Stock"]=gross["Stock"].map(str)
gross.set_index("Stock", inplace=True)
gross=gross.loc[:,"2000":]


eq_cap["Stock"]=eq_cap["Stock"].map('{:06d}'.format)
eq_cap["Stock"]=eq_cap["Stock"].map(str)
eq_cap.set_index("Stock", inplace=True)
eq_cap=eq_cap.loc[:,"2000":] #자기자본


#-------------------------------------------------

# pbr 100개만 뽑았다.~~~
netincome_100=pd.DataFrame(netincome,index=pbr)
non_debt_100=pd.DataFrame(non_debt,index=pbr)
lq_asset_100=pd.DataFrame(lq_asset,index=pbr)
lq_debt_100=pd.DataFrame(lq_debt,index=pbr)
equiss_100=pd.DataFrame(equiss,index=pbr)
cfo_100=pd.DataFrame(cfo,index=pbr)
gross_100=pd.DataFrame(gross,index=pbr)
eq_cap_100=pd.DataFrame(eq_cap,index=pbr)
asset_100=pd.DataFrame(asset,index=pbr)


'''# 자동화의 시도... >> 보완필요
namelist=['df'+str(i) for i in range(len(indices))]

for i in range(len(indices)):
    namelist= df+str(i) 
    namelist[i]= pd.Dataframe(indices2[i], index=pbr)'''

#-------------------------------------------------

# F-score 지표만들기
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

#-------------------------------------------------

# csv 로 바꾸기
# 저장경로 /Users/hwangsujeong/FBA/새 폴더/f_score

roa.T.to_csv("/Users/hwangsujeong/FBA/새 폴더/f_score/roa.csv", 
           header=True, index=True)

cfo_new.to_csv("/Users/hwangsujeong/FBA/새 폴더/f_score/cfo_new.csv", 
           header=True, index=True)

roa_chg.T.to_csv("/Users/hwangsujeong/FBA/새 폴더/f_score/roa_chg.csv", 
           header=True, index=True)

cfo_roa.T.to_csv("/Users/hwangsujeong/FBA/새 폴더/f_score/cfo_roa.csv", 
           header=True, index=True)

debt_chg.T.to_csv("/Users/hwangsujeong/FBA/새 폴더/f_score/debt_chg.csv", 
           header=True, index=True)

lq_chg.T.to_csv("/Users/hwangsujeong/FBA/새 폴더/f_score/lq_chg.csv", 
           header=True, index=True)

equiss_new.to_csv("/Users/hwangsujeong/FBA/새 폴더/f_score/equiss_new.csv", 
           header=True, index=True)

margin.T.to_csv("/Users/hwangsujeong/FBA/새 폴더/f_score/margin.csv", 
           header=True, index=True)

#--------------------------------------------------------

'''
모델 개발 보완점

문제점-> null 값을 더 빨리 조정했어야하나...?
생각보다 증발해버린 데이터가 많다. 데이터 정리 기준 재정리필요.'''
