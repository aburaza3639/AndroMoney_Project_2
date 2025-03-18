import datetime
import pandas as pd
import openpyxl
import AndroMoney.settings

xlsx_file_path = AndroMoney.settings.TABLE_FILE_PATH
xlsx2_file_path = AndroMoney.settings.xlsx2_file_path


def andro_pivotwriter(pivot_andromoney, df):

    with pd.ExcelWriter(xlsx_file_path, engine='openpyxl', mode='w+') as ew:
        pivot_andromoney.to_excel(ew, sheet_name='Sheet1', startrow=3, startcol=7)
        df.to_excel(ew, sheet_name='Sheet2')


def andro_excelwriter(pivot_andromoney, start_date=None):

#Retrieve year-date on table to identify new column
    df3=pd.read_excel(xlsx2_file_path, sheet_name="家計簿", skiprows=16, nrows=1, header=None)
    strd=datetime.datetime.strptime(start_date, "%Y-%m-%d")

    count=0

    for a,b in df3.iteritems():
        count+=1
        if b.iloc[-1] == strd:
            input_data(pivot_andromoney,count)


def input_data(pivot_andromoney, cell):


    wb = openpyxl.load_workbook(xlsx2_file_path)
    ws = wb["家計簿"]
    ws=[ws.cell(row=18+i, column=cell, value=pivot_andromoney.iloc[0+i,3]) for i in range(19)]
    wb.save(xlsx2_file_path)
    wb.close()