# Import libraries
import requests
import urllib
import time
from bs4 import BeautifulSoup
import xlwt
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1", cell_overwrite_ok=True)
keyword='test'
row = 0
url = 'https://tureng.com/en/turkish-english/' + keyword
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
for i in soup.findAll('tr'): # choose all 'tr'
        cell = 0
        for j in i.findAll('td'):   # choose all 'td' under selected 'tr'         
            sheet1.write(row, cell, j.get_text())
            cell = cell + 1
        row = row + 1 
book.save("trial.xls")
