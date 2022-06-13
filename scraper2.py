from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("/Users/anand/Downloads/chromedriver_win32 (2)/chromedriver.exe")
browser.get(START_URL)
time.sleep(10)
star_data = []
soup = BeautifulSoup(browser.page_source, "html.parser")
temp_list = []

def scrape():
    headers = ["Name", "Distance", "Mass", "Radius"]
    for tr_tag in soup.find("table").find_all("tr"): 
        td_tags = tr_tag.find_all("td")
        row = [i.text.rstrip() for i in td_tags]
        temp_list.append(row)

    name = []
    distance = []
    mass = []
    radius = []

    for i in range(1, len(temp_list)):
        name.append(temp_list[i][1])
        distance.append(temp_list[i][3])
        mass.append(temp_list[i][5])
        radius.append(temp_list[i][6])

    star_data.append(temp_list)

    df = pd.DataFrame(list(zip(name, distance, mass, radius)),columns=["Name", "Distance", "Mass", "Radius"])
    df.to_csv("scraper_3.csv")
scrape()