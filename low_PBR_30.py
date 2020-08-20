#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 21:49:44 2020

@author: hwangsujeong
"""

import numpy as np
import pandas as pd

#우선 저 PBR 구하기

# csv파일 읽기
df=pd.read_csv("/Users/hwangsujeong/FBA/새 폴더/adjusted_csv/피비알 2015_2019 monthly.csv",
               encoding="UTF-8")


# 종목명 str로 형식 바꾸기
df["Stock"]=df["Stock"].map('{:06d}'.format)
df["Stock"]=df["Stock"].map(str)

# 데이터 파악하기
print("PBR shape: ",df.shape)
print("------------PBR info------------")
print(df.info())
#help(df.info)
#help(df.dropna())



# 결측치 밀기
# 모든 데이터가 null 값인 친구들만 지워보자 : how="all"
# 우리는 일단 12개 이상 없으면 지운다! df2=df.dropna(thresh=12)
# 근데 최근 5개년도인디... 쩝

df2=df.dropna()  # 그냥 널값있으면 다지움
df2.index=df2["Stock"] 
df2.drop('Stock', axis=1, inplace=True)


#평균을 내고 가장 수가 작은 아이부터 정렬!!
df3=pd.DataFrame(df2.mean(axis=1),columns=["rank"])
df4=df3.rank(method='min') #pbr 작을수록 높은 순위
df5=df4.sort_values(by='rank') #순위대로 내림차순

pbr=df5[df5['rank']<101].index
pbr
