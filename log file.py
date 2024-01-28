import pandas as pd
data=pd.read_csv("E:/project trials/animal/object-coco/logdata.csv")
print("1.Log based on date ")
print("2.Log based on month ")
print("3.Log based on year ")
print("4.Quit ")
q=1
while q!=0:
    i=int(input("Enter the number "))
    if (i==1):
        a=(input("Enter the date in dd-mm-yyyy format "))
        df2=data.loc[data["Date"]==a]
        if df2.empty:
            print("No Records Found")
        else:
            print("The summary for the date ({})  is ".format(a))
            print(df2,"\n")
            print(df2["Animal Detected"].value_counts())
            
    elif(i==2):
        a=int(input("Enter the month in mm format "))
        b=int(input("Enter the year in yyyy format "))
        df2=data.loc[(data["Month"]==a)&(data["Year"]==b)]
        if df2.empty:
            print("No Records Found")
        else:
            print("The summary for {} month and {} year is ".format(a,b))
            print(df2,"\n")
            print("The animal count summary is ")
            print(df2["Animal Detected"].value_counts())
    elif(i==3):
        a=int(input("Enter the year in yyyy format "))
        df2=data.loc[data["Year"]==a]
        if df2.empty:
            print("No Records Found")
        else:
            print("The summary for the date ({})  is ".format(a))
            print(df2,"\n")
            print(df2["Animal Detected"].value_counts())
    elif(i==4):
        print("Thank You ")
        q=0
    else:
        print("Invalid Entry ", "Try Again!!")

    

