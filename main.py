from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep

s = Service('./chromedriver')
driver = webdriver.Chrome(service=s)

## Taking the URL 
yahoo = 'https://finance.yahoo.com/quote/BTC-EUR/history/'
driver.get(yahoo)
sleep(2)

## Selecting all dates 

yahoo_dates = driver.find_elements(By.TAG_NAME, 'tr')

  # Creating an empty list to add all dates after the loop 
list_dates = []

  # Looping and adding to list 
for date in yahoo_dates:
    date = date.find_element(By.TAG_NAME, 'span').text
    list_dates.append(date)

  # List of last 10 dates 
last_ten_dates = list_dates[1:11]


## Selecting all closures 

yahoo_closeds = driver.find_elements(By.TAG_NAME, 'td')

  # Creating an empty list to add all dates after the loop 
list_closeds = []

  # Looping and adding to list 
for closed in yahoo_closeds:
    closed = closed.find_element(By.TAG_NAME, 'span').text
    list_closeds.append(closed)

  # Filtering the closings 
all_closeds = list_closeds[4:-1:7]

  # Filtering the last 10 closes 
last_ten_closed = all_closeds[0:10]


## Converting to a csv file 
dict = {'date': last_ten_dates, 'BTC Closing Value': last_ten_closed} 
df = pd.DataFrame(dict) 
df.to_csv('eur_btc_rates.csv')