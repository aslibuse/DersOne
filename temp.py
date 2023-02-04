# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# %%
 # variable (degisken)
 
 # variable 
 # function
 # coject

var1 = 10 # integer
var2 = 15
 
gun = "pazartesi"  # string

var3 = 10.0 # double (float)
# 5var = 10 # hata verir
Var7 = 19 # standart convention of python'a gore buyuk harfle baslaması uygun degıl

# %%
# string

s = "bugun gunlerden pazartesi"

variable_type = type(s) # str = string

print(s)

var1 = "ankara"
var2 = "ist"
var3 = var1+var2
#%%
var4 = "100"
var5 = "200"
var6 = var4+var5


uzunluk = len(var6)
#%% numbers

# int double
integer_deneme = -50
# double = float = ondalikli sayi

float_deneme = -30.7

benimadim = "buse"
#%% built in functions 
str= "deneme"

float1 = 10.6
str2 = "1005"
# %% user defined function

var1 = 10
var2 = 100

output = (((var1+var2)*50)/100)*var1/var2

# fonksiyon parametresi = input
def benim_ilk_func(var1,var2):
    """
    bu benim ilk denemem
    
    parametre:
    
    return:
    """
    output = (((var1+var2)*50)/100)*var1/var2
   
    return output

def deneme1():
    print("bu benim ikinci denemem")
    
   
#%% default ve flexible function

name = 'omer'

def deneme(name):
    return name
# %%

def denne():
    return '12345'