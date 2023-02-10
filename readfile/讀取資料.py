import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import butter, lfilter,filtfilt
import os

path= r"C:\Users\aes66\OneDrive\桌面\python test\TEST\8_test"
dirs=os.listdir(path)

df=pd.DataFrame()
dic={}
dic2={}

for file in dirs:
    df=pd.read_excel(r"C:\Users\aes66\OneDrive\桌面\python test\TEST\8_test\\" + str(file))
    filter1=df["Event"] == "M3"
    filter2=df["Event"] == "M4"
    df2=df[filter1 | filter2]
    dic2={file:df2}
    dic.update(dic2)

print(dic)
  
# path= r"C:\Users\aes66\OneDrive\桌面\joyp\state-files"
# dirs=os.listdir(path)




