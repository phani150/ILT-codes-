####################################################################################################################################################
#   File Name       : Testing_tk_weekly.py
#   Description     :                      
#   Author          :Phanindra D(phanindra.d@unilever.com)
#   Version History :
#   2.0 - Initial Draft (28-Nov-2018)
####################################################################################################################################################

##Importing the required modules

from tkinter import *
from tkinter import filedialog
##import PIL.Image, PIL.ImageTk
##import cv2
from tkinter import messagebox
import csv
import pandas as pd
import numpy as np
import os
from datetime import datetime
from functools import reduce
import math
import shutil
import sys
cwd = os.getcwd()
os.chdir(cwd)

class Window:
    """Creating the Window"""
    
    def __init__(self, master):     
        self.filename=""
        csvfile=Label(root, text="File").grid(row=29, column=20)
        bar=Entry(master).grid(row=29, column=21) 

        #Buttons  
        y=7
        self.cbutton= Button(root, text="Execute", command=self.process_csv, relief=RAISED)
        y+=1
        self.cbutton.grid(row=30, column=32, sticky = S+W)
        self.bbutton= Button(root, text="Browse", command=self.browsecsv)
        self.bbutton.grid(row=29, column=32,sticky= S+W)

        self.opco_code= Entry(root,bd = 5)
        self.opco_label=Label(root,text="Opco Code")
        self.cal_start_mnth = Entry(root,bd = 5)
        self.cal_start_label=Label(root,text="Cal Start")
        self.cal_end_mnth=Entry(root,bd = 5)
        self.cal_end_label=Label(root,text="Cal End")
        
        
        self.opco_code.grid(row=7, column=12)
        self.opco_label.grid(row=7,column=9)
        self.cal_start_mnth.grid(row=8, column=12)
        self.cal_start_label.grid(row=8,column=9)
        self.cal_end_mnth.grid(row=9,column=12)
        self.cal_end_label.grid(row=9,column=9)
    
    def browsecsv(self):

        Tk().withdraw() 
        self.filename = filedialog.askopenfilenames(filetypes=(('Text files', '*.txt'),('All Files','*.*')),title='Select Input File')
        self.fileList = root.tk.splitlist(self.filename)
        
    def process_csv(self):
        global final_df
        global final_df1
        global final_df2
        opco=int(self.opco_code.get())
        start=int(self.cal_start_mnth.get())
        end=int(self.cal_end_mnth.get())
        for file in self.fileList:
            if file.endswith('.txt') and "PH" in file:
                ####Reading the PH file
                df1=pd.read_csv(file,sep="|", usecols=['opco_code','product_DU_code','product_category_desc','product_SPF_code','product_sub_division2_desc','product_sub_division1_desc','product_division_desc'],encoding = "ISO-8859-1",low_memory=False)
                opco_booleans1=[]
                for opco_len in df1['opco_code']:
                    if opco_len == opco:
                        opco_booleans1.append(True)
                    else:
                        opco_booleans1.append(False)
                is_opco=pd.Series(opco_booleans1)        
                final_df1=df1[opco_booleans1]    
                final_df1.replace(r'\s+', np.nan, regex=True)
                print("Processing of "+ file + " Completed")
            if file.endswith('.txt') and "FCST" in file:
                ##Reading the FCST file
                df2=pd.read_csv(file,sep="|",encoding="ISO-8859-1",low_memory=False)
                opco_booleans=[]
                for opco_len in df2['opco_code']:
                    if opco_len == opco:
                        opco_booleans.append(True)
                    else:
                        opco_booleans.append(False)
                is_opco=pd.Series(opco_booleans)        
                final_df2=df2[opco_booleans]    
                final_df2.replace(r'\s+', np.nan, regex=True)
                booleans2=[]
                for length in final_df2['calendar_month_id']:
                    if  start <=  length <= end:
                        booleans2.append(True)
                    else:
                        booleans2.append(False)
                is_long=pd.Series(booleans2)
                final_df=final_df2[booleans2]
                final_df.replace(r'\s+', np.nan, regex=True)
                print("Processing of" + file + " Completed")
            if file.endswith('.txt') and "UOM" in file:
                ####Reading the UOM file
                df3=pd.read_csv(file,sep="|",usecols=['sales_org_opco_code','product_DU_code','pack_nature','product_FU_code','product_FG_code','FS_INDICATOR'],encoding="ISO-8859-1",low_memory=False)
                opco_booleans3=[]
                for opco_len in df3['sales_org_opco_code']:
                    if opco_len == opco:
                        opco_booleans3.append(True)
                    else:
                        opco_booleans3.append(False)
                is_opco=pd.Series(opco_booleans3)        
                final_df3=df3[opco_booleans3]    
                final_df3.replace(r'\s+', np.nan, regex=True)
                print("Processing of " + file +" Completed")
                #print (list(df3.columns.values))
                ##sys.exit()
                dfs = [final_df,final_df1,final_df3]
                req_df = reduce(lambda left,right: pd.merge(left,right,on='product_DU_code',how="outer"), dfs)
                req_df.dropna(subset=['OpCo_DU_CL3_MU_Channel_week_month_code'],inplace=True)
##               print (req_df)
##               sys.exit()
                req_df.to_csv("OutputFile.txt",sep="|",index=False)            
        messagebox.showinfo("Reading files completed", "Please check Output Files Directory for results ...")   

        #Process end time
        
        end = datetime.now()
        print("Processing end time : "+str(end))
        print("\n")
        print("Please check Output Files Directory for results ...")
        input("Press ENTER key to continue ...")

root = Tk()
root.wm_title("SnOP Weekly Lookup")
  
##cv_img = cv2.imread("Unilever_logo")
##height, width, no_channels = cv_img.shape  
root.configure(bg='sky blue')
root.geometry("400x400")
window=Window(root)
root.mainloop()




