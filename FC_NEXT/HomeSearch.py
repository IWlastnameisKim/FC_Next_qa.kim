import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
def HomeSearch() :

    driver = webdriver.Chrome()

    driver.get('https://fastcampus.co.kr')
    driver.implicitly_wait(5)
    time.sleep(5)
    driver.maximize_window()
    driver.implicitly_wait(2)
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/button').click()
    except:
        pass
    try :
        driver.find_element(By.XPATH, '//*[@id="search-input"]').click()
        driver.find_element(By.XPATH, '//*[@id="search-input"]').send_keys("검색테스트1")
        driver.find_element(By.XPATH, '//*[@id="search-input"]').send_keys(Keys.ENTER)
    except Exception as Error1 :
        print(Error1)

    driver.implicitly_wait(5)
    time.sleep(2)

    if str("검색테스트1") in driver.find_element(By.XPATH, '//*[@id="main"]/div/section/div/p/span').text: print("검색 동작 PASS")
    elif str("검색테스트1") not in driver.find_element(By.XPATH, '//*[@id="main"]/div/section/div/p/span').text : print("검색 동작 FAIL")

    try :
        driver.find_element(By.XPATH, '//*[@id="search-input"]').click()
        driver.find_element(By.XPATH, '//*[@id="search-input"]').clear()
        driver.find_element(By.XPATH, '//*[@id="search-input"]').send_keys("파이썬")
        driver.find_element(By.XPATH, '//*[@id="search-input"]').send_keys(Keys.ENTER)
    except Exception as Error2 :
        print(Error2)

    driver.implicitly_wait(5)
    time.sleep(2)
    try :

        if not driver.find_elements(By.XPATH, '//*[@id="main"]/div/section/div/div[2]/a[1]/div[2]/img') :
            print("강의 검색 동작 FAIL")
        else : print("강의 검색 동작 PASS")

        driver.find_element(By.XPATH, '//*[@id="search-input"]').click()
        time.sleep(2)
        if not driver.find_elements(By.XPATH, '/html/body/div[2]/header/div/div[1]/div[1]/div/div[1]/ul/li[1]/a') : print("검색 기록 FAIL")
        elif driver.find_element(By.XPATH, '/html/body/div[2]/header/div/div[1]/div[1]/div/div[1]/ul/li[1]/a').text == "파이썬" :
            print("검색 기록 PASS")
        else : print("검색 기록 FAIL")
    except Exception as Error3 :
        print(Error3)

    try :
        driver.find_element(By.CLASS_NAME, 'recommend-search__list')
        print("추천 검색어 노출 PASS")
    except : print("추천 검색어 미노출")
    driver.close()
if __name__ == '__main__' :
    HomeSearch()