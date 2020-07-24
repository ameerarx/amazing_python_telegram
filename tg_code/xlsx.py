# @pythonamazing(Telegram)
import xlrd
import csv
wb = xlrd.open_workbook('my_data.xlsx')
sheet = wb.sheet_by_name('Sheet1')

with open('output.csv','w') as csv_file:
    w = csv.writer(csv_file,quoting= csv.QUOTE_ALL)
    
    for r_num in range(sheet.nrows):
        w.writerow(sheet.row_values(r_num))