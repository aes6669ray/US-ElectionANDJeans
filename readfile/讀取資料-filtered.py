import pandas as pd
import os


# col=["state","county","fips","trump16","clinton16","otherpres16","romney12","obama12","otherpres12","demsen16","repsen16","othersen16","demhouse16","rephouse16","otherhouse16","demgov16","repgov16","othergov16","repgov14","demgov14","othergov14","total_population","cvap","white_pct","black_pct","hispanic_pct","nonwhite_pct","foreignborn_pct","female_pct","age29andunder_pct","age65andolder_pct","median_hh_inc","clf_unemploy_pct","lesshs_pct","lesscollege_pct","lesshs_whites_pct","lesscollege_whites_pct","rural_pct","ruralurban_cc"]

# df = pd.read_csv("2018.csv",sep=",",usecols=col)
# print(df)


col=["state","county","office","party","votes"]
# df = pd.read_csv("AK.csv",sep=",",usecols=col)
# filter1=df["office"]=="US House"
# df2=df[filter1]

# filter2=df2["party"]=="Democrat"
# filter3=df2["party"]=="Republican"

# df3d=df2[filter2]
# df3r=df2[filter3]

# de=df3d["votes"].sum()
# re=df3r["votes"].sum()
# all=de+re

path= r"C:\Users\aes66\OneDrive\桌面\joyp\state-files"
dirs=os.listdir(path)



df=pd.DataFrame()
dic={}
delist=[]
relist=[]
alllist=[]
statelist=[]


for file in dirs:
    df=pd.read_csv(r"C:\Users\aes66\OneDrive\桌面\joyp\state-files\\" + str(file),sep=",",usecols=col,encoding="ISO-8859-1")
    filter1=df["office"]=="US House"
    df2=df[filter1]

    filter2=df2["party"]=="Democrat"
    filter3=df2["party"]=="Republican"

    df3d=df2[filter2]
    df3r=df2[filter3]
    de=df3d["votes"].sum()
    re=df3r["votes"].sum()
    all=de+re

    delist.append(de)
    relist.append(re)
    alllist.append(all)
    statelist.append(str(file)[:2])

dic={"state":statelist,"democratvotes":delist,"republicanvotes":relist,"total_votes":alllist}
newdf=pd.DataFrame(dic)
newdf.to_excel("newdf.xlsx")

