from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import json
import pandas as pd

with open("D:\\Company\\Python\\Automation\\CSVFiles\\Path.json") as file:
    path_manager = json.load(file)

df = pd.read_csv(path_manager["Data_filepath"])


options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = Options())
# driver.set_window_size(400,400)
int_index = 4
url = df["website"][int_index]
loginID = df["username"][int_index] #"psandip2806@gmail.com"
password = df["password"][int_index]

driver.get(url)
try:
    username = driver.find_element(By.ID,"luser")

    username.send_keys(loginID)

    passwordID = driver.find_element(By.ID,"password")

    passwordID.send_keys(password)

    passwordID.send_keys(Keys.RETURN)

    time.sleep(5)

    print("Login success")
except Exception as  e:
    print(">>>>>>",e)

finally:
    print("run successfully....")