# Import the required library  

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
import time

df = pd.DataFrame(columns=['URL', 'Restaurant Name', 'Cost For 2'])
# define dataframe to store the required information

locations = ['All_zomato_stores_locations']

for i in locations:
    browser.get("retrieves all zomato location one by one")  
    print(i)

    scroll_pause_time = 3 #set pause time
    screen_height = browser.execute_script("return window.screen.height;")  # get the screen height of the web
    i = 1

    while True:
        # scroll one screen height each time
        browser.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
        i += 1
        time.sleep(scroll_pause_time)
        # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
        scroll_height = browser.execute_script("return document.body.scrollHeight;")
        # Break the loop when the height we need to scroll to is larger than the total scroll height

        restaurant_list = browser.find_elements(By.CLASS_NAME, 'jumbo-tracker')
        # web element where all the required information stored  

        for data in restaurant_list:
            for item in data.find_elements(By.TAG_NAME,"a"):
                href = item.get_attribute('href')
                if href not in li:
                    li.append(href)
                    restaurant_name = data.find_element(By.TAG_NAME,"h4").text
                    cost_for_2 = data.find_elements(By.TAG_NAME,"p")[2].text
                    df.loc[len(df)] = [href, restaurant_name, cost_for_2 ]
        if (screen_height) * i > scroll_height:
            break

browser.close()

# saved all the data in excel file 
