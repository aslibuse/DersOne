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
# importing
 import numpy as np 
 
array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) 1*15 vector

print(array.shape)

a = array.reshape(3,5)
print("shape": ,a.shape)
print("dimension:", a.ndim)

print("data type:",a.dtype.name)
print("size:", a.size)

print("type: ", type(a))

array1 = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,5]])

zeros = np.zeros((3,4))

zeros[0,0] = 5
print(zeros)

np.ones((3,4))

np.empty((2,3))

b = np.arrange(10,50,5)

a = np.linspace(10,50,20)
#%%
a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print(a-b)
print(a**2) #iki yıldız karesi demek
print(np.sin(a))
print(a<2)
 a = np.array([[1,2,3],[4,5,6]])
 b = np.array([[1,2,3],[4,5,6]])
 # element wise prodcut
 print(a*b)
 # matrix prodcut
 a.dot(b.T)
 
 print(np.exp(a))

 a = np.random.random((5,5))
 
 print(a.sum())
 print(a.max())
 print(a.min())
 
 print(a.sum(axis=0)) #axis 0 = kalınları topla
 print(a.sum(axis=1)) # satırları toplar
 
 print(np.sqrt(a)) #karekok
 print(np.square(a)) #a**2
 np.add(a,a)
 #%%
 import numpy as np
 array = np.array(1,2,3,4,5,6,7) # vector dimension = 1
 print(array[0])
 # programlamada ilk baştakini yazdırır ama sondakini yazdırmaz
 array[0:3]
 reverse_array = array[::-1]
 print(reverse_array)
 
 array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
 print(array1[1,1])
 print(array1[:,1])
 print(array1[1,1:4])
 print(array1[-1,:]) # son satır
 print(array1[:,-1]) # son sütun
 #%%
 # shape manipulation
 array = np.array([[1,2,3],[4,5,6],[7,8,9]])
 # flatten
 a = array.ravel() #sıraya koyar
 array2 = a.reshape(3,3)
 arrayT = array2.T
 print(array.shape)
 array5 = np.array([[1,2],[3,4],[4,5]])
 array5.resize((2,3)) #size = yeni bir variable yapar ama shape direkt yapar
 