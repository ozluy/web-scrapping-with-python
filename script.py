# Import libraries
import requests
import urllib
import time
from bs4 import BeautifulSoup
import xlwt
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1", cell_overwrite_ok=True)
# Set the URL you want to webscrape from
row = 0
for page in range(1, 57):
    url = 'https://quantiacs.com/Systems.aspx?searchMinLiveTradingDays=365&searchMinSharpeRatio=1&sortingCritera=%27%27%27SortTradingDaysAfter%27%27%27&sortingOrder=%27%27%27desc%27%27%27&&page='+str(page)
    # Connect to the URL
    response = requests.get(url)
    # Parse HTML and save to BeautifulSoup object
    soup = BeautifulSoup(response.text, "html.parser")
    # To download the whole data set, let's do a for loop through all a tags
    for i in soup.findAll('tr'): #'tr' tags are for links 
        cell = 0
        for j in i.findAll('td'):            
            sheet1.write(row, cell, j.get_text())
            cell = cell + 1
    row = row + 1 
    time.sleep(1)
book.save("trial.xls")
