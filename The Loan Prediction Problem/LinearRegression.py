# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 21:49:04 2017

@author: Swapnil.Walke
"""
import re
import numpy as np
import pandas as pd
import string
"""functions for data cleaning"""


def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate

def isNan(value):
    if str(value)=='nan':
        return True
    else:
        return False

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def id_verified(value):
    if 'not' in str(value).lower().split(" "):
        return 0
    else:
        return 1

def conv_lower(value):
    if not isfloat(value):
        return value.lower()

title = {}
@static_vars(a=1)
def change_title(value):
    value = str(value)
    if isNan(value):
        return 0
    value = value.lower()
    if value not in title.keys():
        title[value] = change_title.a
        change_title.a = change_title.a + 1
        return title[value]
    else:
        return title[value]
    
def home_ownership(value):
    value = str(value)
    if value == "ANY":
        return 0
    elif value == "MORTGAGE":
        return 1
    elif value == "OWN":
        return 2
    elif value == "RENT":
        return 3

state={}
@static_vars(b=1)
def change_addr_state(value):
    value = str(value)
    if isNan(value):
        return 0
    value = value.lower()
    if value not in state.keys():
        state[value] = change_addr_state.b
        change_addr_state.b = change_addr_state.b + 1
        return state[value]
    else:
        return state[value]
    
grade = {}
@static_vars(g=0)
def grade_value(value):
    value = str(value)
    if value not in grade.keys():
        grade[value] = grade_value.g + 1
        grade_value.g = grade_value.g+1
        return grade[value]
    else:
        return grade[value]

@static_vars(g=0)
def sub_grade_value(value):
    value = str(value)
    if value not in grade.keys():
        grade[value] = grade_value.g + 1
        grade_value.g = grade_value.g+1
        return grade[value]
    else:
        return grade[value]
    
emp = {}
@static_vars(g=1)
def emp_value(value):
    value= str(value)
    if isNan(value):
        return 0
    value = value.lower()
    if value not in emp.keys():
        emp[value] = emp_value.g
        emp_value.g = emp_value.g + 1
        return emp[value]
    else:
        return emp[value]
    
def change_emp_length(year):
    year = str(year)
    if isNan(year):
        return 0
    else:
        all = string.maketrans('','')
        nodigs = all.translate(all, string.digits)
        year = year.translate(all, nodigs)
        return year

def change_desc(value):
    value = str(value)
    if isNan(value):
        return 0
    else:
        return 1
    
purp = {}
@static_vars(g=1)
def change_purpose(value):
    value= str(value)
    if isNan(value):
        return 0
    value = value.lower()
    if value not in purp.keys():
        purp[value] = change_purpose.g
        change_purpose.g = change_purpose.g + 1
        return purp[value]
    else:
        return purp[value]
    
def change_pymnt_plan(plan):
    plan = str(plan)
    if plan == 'n':
        return 1
    else:
        return 0
    
df = pd.read_csv("train_indessa.csv")
#print df.iloc[0,:]

"""Drop unnecessary columns"""

df = df.drop('member_id', 1)
df = df.drop('zip_code', 1)
df = df.drop('batch_enrolled', 1)
df = df.drop('verification_status_joint', 1)

"""Fromat the necessary columns"""

df['term'] = df['term'].str[:2].astype(int)

#change every string to lower case
"""k = 0
for index, row in df.iterrows():
    
    for i in range(0, len(row)):
        if not str(row[i]).isdigit() and not isfloat(str(row[i])):
            row[i]=row[i].lower()
    k = k +1
    if k == 100:
        break
   """ 

#df.to_csv('train.csv')
#data wrangling
mean_df = df.mean(axis=0, skipna = True, numeric_only = True)
grade = {}
emp = {}
own = {}
ver_status = {}
app_type = {}
x = 0

#df.loc[isNan(df['desc']),'desc'] = 0
#df.loc[not isNan(df['desc']), 'desc'] = 1

"""Data cleaning happening here"""
#df['application_type'] = df.apply(lambda row: conv_lower(row['application_type']), axis=1)
#df['verification_status'] = df.apply(lambda row: id_verified(row['verification_status']), axis=1)
#df['home_ownership'] = df.apply(lambda row: home_ownership(row['home_ownership']), axis=1)
#df['grade'] = df.apply(lambda row: grade_value(row['grade']), axis=1)
#df['sub_grade'] = df.apply(lambda row: sub_grade_value(row['sub_grade']), axis=1)
#df['emp_title'] = df.apply(lambda row: emp_value(row['emp_title']), axis=1)
#df['emp_length'] = df.apply(lambda row: change_emp_length(row['emp_length']), axis=1)
#df['pymnt_plan'] = df.apply(lambda row: change_pymnt_plan(row['pymnt_plan']), axis=1)
#df['desc'] = df.apply(lambda row: change_desc(row['desc']), axis=1)
#df['purpose'] = df.apply(lambda row: change_purpose(row['purpose']), axis=1)
#df['title'] = df.apply(lambda row: change_title(row['title']), axis=1)
df['addr_state'] = df.apply(lambda row: change_addr_state(row['addr_state']), axis=1)
print df.iloc[1,:]
for index, row in df.iterrows():
    print row['application_type']
    break
#print grade

#for index, row in df.iterrows():
    #if row['']






#print mean_df['pub_rec']
#print mean_df.shape, df.shape
#for index, row in df.iterrows():
 #   if not isNan(row['emp_title']) and str(row['emp_title']) not in emp.keys():
#        emp[str()]
    #
#print df.shape
#for index, row in df.iterrows():
 #   row['emp_title'] = row['emp_title'].lower()
    #if row['emp_title'].lower() not in emp.keys():
    #    emp[row['emp_title'].lower()] = x + 1
    
#df.to_csv("train_indessa.csv")