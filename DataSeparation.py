import pandas as pd
import numpy as np
import re
import os

def separate_files(path):
    """ This function reads multiple sheets of three types from data.xlsx, data_1.xlsx 
    and creates three csv files namely detail.csv, detailVol.csv and detailTemp.csv """
    
    df_detail = pd.DataFrame()    #to store data collected from "Detail_67_*"
    df_detvol = pd.DataFrame()    #to store data collected from "DetailVol_67_*.xlsx"
    df_dettemp = pd.DataFrame()   #to store data collected from "DetailTemp_67_*.xlsx"

    files = os.listdir(filepath)    #list the files present in the filepath

    for file in files:      #loop through all the files
        if file.endswith('.xlsx'):
            excel_file = pd.ExcelFile(file)
            sheets = excel_file.sheet_names
            for sheet in sheets:      #loop through sheets present inside the Excel file
                if re.match(r'Detail_67_*',sheet):      #regex to look for all sheets of "Detail_67" category
                    df = excel_file.parse(sheet_name = sheet)
                    df_detail = df_detail.append(df,ignore_index=True)
                if re.match(r'DetailVol_67_*',sheet):     #regex to look for all sheets of "DetailVol_67" category
                    df = excel_file.parse(sheet_name = sheet)
                    df_detvol = df_detvol.append(df,ignore_index=True)
                if re.match(r'DetailTemp_67_*',sheet):      #regex to look for all sheets of "DetailTemp_67" category
                    df = excel_file.parse(sheet_name = sheet)
                    df_dettemp = df_dettemp.append(df,ignore_index=True)
    
    df_detail.to_csv("detail.csv", index=None, header=True)
    df_detvol.to_csv("detailVol.csv", index=None, header=True)
    df_dettemp.to_csv("detailTemp.csv", index=None, header=True)

filepath = os.path.abspath('')
separate_files(filepath)


        
        