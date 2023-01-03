# import required libraries 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
import time


df = pd.DataFrame(columns=['URL','Address','Number','Menu', 'Serves Alcohol'])
# define dataframe 

url_list = pd.read_csv("url_list.csv")
# read urls list 

# Read all urls one by one
# extract data from each urls 

p_tag = restaurant_list[-1].find_elements(By.TAG_NAME,"p")
Contact_Number = p_tag[0].text
Full_Address = p_tag[1].text

serve_alcohol = 'No'
h2_tag = restaurant_list[0].find_elements(By.TAG_NAME, 'h2')
if 'Menu' in [j.text for j in h2_tag]:
    menu = "Exist Menu"
    h4_tag = browser.find_elements(By.CSS_SELECTOR, "h4")
    h4_tag_list = [i.text for i in h4_tag]
    if 'Bar Menu' in h4_tag_list:
        serve_alcohol = 'Yes'
else:
    menu = "Not Exist Menu"

browser.close()

# stored all the data in csv file 



