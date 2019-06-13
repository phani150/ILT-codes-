####################################################################################################################################################
#   File Name       : ITA_Data_Merge_Script.py
#   Description     :                      
#   Author          :Phanindra D(phanindra.d@unilever.com)
#   Version History :
#   1.0 - Initial Draft (05-Dec-2018)
####################################################################################################################################################

##Importing the required modules
import os
import sys
import numpy as np
import pandas as pd
from datetime import datetime
from functools import reduce
import matplotlib.pyplot as plt

cwd = os.getcwd()
status=0

Split_file="SOP_FVIH_SR_PH_CEE.txt"

print("************************** OPTIONS MENU *********************************")
print("1. Merge data from multiple files and Generate  Results")
print("2. Split data from a huge file and Generate Results")
print ("3. Exit")

while(status != 1):
    inputValue = input("\nPlease enter your choice : ")
    if(inputValue not in ['1','2','3']):
        print("Invalid Input!!!")
        status=0
    elif(inputValue == '3'):
        sys.exit()
    else:
        status=1
        
##Reading the Source .xlsx files
Data1_File="ITA Data1.XLSX"
Data2_File="ITA Data2.XLSX"
Data3_File="ITA Data3.XLSX"
Data4_File="ITA Data4.XLSX"

##Reading the Source .txt files
Data1_File_txt="ITA Data1.csv"
Data2_File_txt="ITA Data2.csv"
Data3_File_txt="ITA Data3.csv"
Data4_File_txt="ITA Data4.csv"

if(inputValue == '1'):    
    try:
        for file in os.listdir(cwd):
            if(".XLSX" in file):
                ##Processing the  excel Data files,we can read the files from the repository url also
                df1 = pd.read_excel(Data1_File,encoding = "ISO-8859-1",dtype='unicode')
                print ("Processing of " + Data1_File + " Completed")
                df2 = pd.read_excel(Data2_File,encoding = "ISO-8859-1",dtype='unicode')
                print ("Processing of " + Data2_File + " Completed")
                df3 = pd.read_excel(Data3_File,encoding = "ISO-8859-1",dtype='unicode')
                print ("Processing of " + Data3_File + " Completed")
                df4 = pd.read_excel(Data4_File,encoding = "ISO-8859-1",dtype='unicode')
                print ("Processing of " + Data4_File + " Completed")

                ##Concatinating all the DataFrames
                frames=[df1,df2,df3,df4]
                final_df = pd.concat([df1,df2,df3,df4])
                final_df.to_excel("OutputFile.xlsx",index=False)
            break
    except:
        ##Processing of Data files,we can read the files from the repository url also
        df1 = pd.read_csv(Data1_File_txt,encoding = "ISO-8859-1",sep=",")
        print ("Processing of " + Data1_File_txt + " Completed")
        df2 = pd.read_csv(Data2_File_txt,encoding = "ISO-8859-1",sep=",")
        print ("Processing of " + Data2_File_txt + " Completed")
        df3 = pd.read_csv(Data3_File_txt,encoding = "ISO-8859-1",sep=",")
        print ("Processing of " + Data3_File_txt + " Completed")
        df4 = pd.read_csv(Data4_File_txt,encoding = "ISO-8859-1",sep=",")
        print ("Processing of " + Data4_File_txt + " Completed")

        ##Concatinating all the DataFrames
        frames=[df1,df2,df3,df4]
        final_df = pd.concat([df1,df2,df3,df4])
        final_df.to_excel("OutputFile.xlsx",index=False)      
    finally:
        print ("Processing of Source files completed")
        
if(inputValue == '2'):
    num_split=int(input("Please enter the number of split's:"))
    for file in os.listdir(cwd):
        if ("PH" in  file): 
            df1= pd.read_csv(Split_file,encoding = "ISO-8859-1",sep="|")
            length=len(df1.index)
            print ("The Source file contains :" + str(length) + " rows")
            if (int(length) > 1048576):
                mul_df=np.array_split(df1,num_split)
                mul_df[0].to_csv("OutputFile1.txt",sep="|")
                mul_df[1].to_csv("OutputFile2.txt",sep="|")
                mul_df[2].to_csv("OutputFile3.txt",sep="|")
                mul_df[3].to_csv("OutputFile4.txt",sep="|")
                
            else:
                print ("The Source file contains less number of rows")
                break
            
#Process end time 
end = datetime.now()
print("Processing end time : "+str(end))
print("\n")
print("Please check Output Files Directory for results ...")
input("Press ENTER key to continue ...")
