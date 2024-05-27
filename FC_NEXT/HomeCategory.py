import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
def HomeCategory() :
    driver = webdriver.Chrome()

    driver.get('https://fastcampus.co.kr')
    driver.implicitly_wait(5)
    time.sleep(5)
    driver.maximize_window()
    driver.implicitly_wait(2)
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/button').click() #팝업 닫기
    except:
        pass
    try :
        CN = 1
        ActionChains(driver).move_to_element(driver.find_element(By.XPATH, f'/html/body/div[2]/header/nav/div/div[1]/div/div')).perform()
        time.sleep(1)
        while True :

            Category1depthNo = f'/html/body/div[2]/header/nav/div/div[1]/div/div[2]/div[2]/ul/li[{CN}]/a' #1depth 위치 /div/div[2]/ul/li[3]/a


            # Category1depthNo = len(driver.find_element(By.XPATH, Category1depth))
            if not driver.find_elements(By.XPATH, Category1depthNo) : break #1depth 메뉴 전체 갯수 세기
            else:
                CN +=1 #최종적으로 CN == 1depth 전체 메뉴 갯수

    except Exception as Error1 :
        print(Error1)

    try :
        for Category1depth in range(1, CN) :
            CN2 = 1
            # ActionChains(driver).move_to_element(driver.find_element(By.XPATH, f'/html/body/div[2]/header/nav/div/div[1]/div/div')).perform()
            time.sleep(1)
            ActionChains(driver).move_to_element(driver.find_element(By.XPATH, f'/html/body/div[2]/header/nav/div/div[1]/div/div[2]/div[2]/ul/li[{Category1depth}]/a')).perform()
            time.sleep(1)


            while True :
                Category2depthNo = f'/html/body/div[2]/header/nav/div/div[1]/div/div[2]/ul/li[{CN2}]/a' #2depth 위치
                if not driver.find_elements(By.XPATH, Category2depthNo) : break
                else:
                    CN2 +=1

            for Category2depth in range(1,CN2) :

                print((driver.find_element(By.XPATH, f'/html/body/div[2]/header/nav/div/div[1]/div/div[2]/div[2]/ul/li[{Category1depth}]/a').text)+" - "+(driver.find_element(By.XPATH, f'/html/body/div[2]/header/nav/div/div[1]/div/div[2]/ul/li[{Category2depth}]/a').text))
    except Exception as Error2 :
        print(Error2)


if __name__ == '__main__' :
    HomeCategory()

