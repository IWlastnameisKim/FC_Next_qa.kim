import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def MoveToFCBO() :
    webdriver.Chrome().get('fastcampus.day1co.kr/#/login')
    webdriver.Chrome().implicitly_wait(5)
    time.sleep(5)
    webdriver.Chrome().maximize_window()
    webdriver.Chrome().implicitly_wait(2)
    time.sleep(2)

def MoveToFCFO() :
    webdriver.Chrome().get('https://fastcampus.co.kr/')
    webdriver.Chrome().implicitly_wait(5)
    time.sleep(5)
    webdriver.Chrome().maximize_window()
    webdriver.Chrome().implicitly_wait(2)
    time.sleep(2)

def PopupClose() :
    try:
        webdriver.Chrome().find_element(By.XPATH, '/html/body/div[2]/div/div[2]/button').click()
    except:
        pass

def LoginCHK() :
    if not webdriver.Chrome().find_elements(By.XPATH, '/html/body/div[1]/header/div/div[2]/div/a') :
        if webdriver.Chrome().find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/div/div[1]/em').text == "김인원님" :
            print("로그인 상태")
        else :
            print("로그인 버튼 미노출")
            exit(1)
    else : print("로그인 버튼 노출")

if __name__ == '__main__' :
    MoveToFCFO()
    PopupClose()
    LoginCHK()