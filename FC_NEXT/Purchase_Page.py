import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
def PurchasePage() :
    driver = webdriver.Chrome()
    driver.get('https://fastcampus.co.kr/')
    driver.implicitly_wait(5)
    time.sleep(5)
    driver.maximize_window()
    driver.implicitly_wait(2)
    time.sleep(2)

    def popupclose():
        try:
            driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/button').click()  # 팝업 닫기 버튼 선택
        except:
            pass

    def LoginCHK():
        if not driver.find_elements(By.XPATH, '/html/body/div[2]/header/div/div[2]/div/a'):  # 로그인 버튼이 안보인다면
            if driver.find_element(By.XPATH, '/html/body/div[2]/header/div/div[2]/div/div[1]/em').text == "김인원님":
                print("로그인 상태")  # 로그인된 계정
            else:
                print("로그인 버튼 미노출")
                exit(1)
        else:
            print("로그인 버튼 노출")

    driver.implicitly_wait(5)
    time.sleep(3)
    popupclose()
    LoginCHK()
    try:
        driver.find_element(By.XPATH, '/html/body/div[2]/header/div/div[2]/div/a').click()
        driver.implicitly_wait(2)
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="user-email"]')
        driver.find_element(By.XPATH, '//*[@id="user-password"]')
    except:
        print("로그인 페이지 이상 있음")

    try:
        driver.find_element(By.XPATH, '//*[@id="user-email"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="user-email"]').send_keys("qa.kim@day1company.co.kr")
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="user-password"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="user-password"]').send_keys("qlalfqjsgh1!")
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[2]/section/div/form/div[2]/button').click()
        driver.implicitly_wait(2)
        time.sleep(2)
    except Exception as LoginERR:
        print(LoginERR)

    driver.implicitly_wait(5)
    time.sleep(3)
    popupclose()

    if not driver.find_elements(By.XPATH, '/html/body/div[2]/header/div/div[2]/div/div[1]/em'):
        print("로그인 이상")
        exit(1)
    else:
        if driver.find_element(By.XPATH, '/html/body/div[2]/header/div/div[2]/div/div[1]/em').text == "김인원님":
            print(driver.find_element(By.XPATH, '/html/body/div[2]/header/div/div[2]/div/div[1]/em').text + "으로 로그인 성공")
        else:
            print("로그인 된 계정 정보 상이함")
            exit(1)

    popupclose()

    try:
        CN = 1
        ActionChains(driver).move_to_element(driver.find_element(By.XPATH, f'/html/body/div[2]/header/nav/div/div[1]/div/div')).perform()
        time.sleep(1)
        while True:

            Category1depthNo = f'/html/body/div[2]/header/nav/div/div[1]/div/div[2]/div[2]/ul/li[{CN}]/a'  # 1depth 위치 /div/div[2]/ul/li[3]/a

            # Category1depthNo = len(driver.find_element(By.XPATH, Category1depth))
            if not driver.find_elements(By.XPATH, Category1depthNo):
                break  # 1depth 메뉴 전체 갯수 세기
            else:
                CN += 1  # 최종적으로 CN == 1depth 전체 메뉴 갯수

        driver.find_element(By.XPATH,f'/html/body/div[2]/header/nav/div/div[1]/div/div[2]/div[2]/ul/li[{CN-1}]/a').click()

    except Exception as Error1:
        print(Error1)
    time.sleep(15)
    driver.implicitly_wait(5)

    if "fastcampus.co.kr/categories" in driver.current_url :
        pass
    else:
        print("전체 카테고리 페이지 진입 실패")
        exit(1)
    for i in range(1,5) :
        if driver.find_elements(By.XPATH, f'//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[{i}]/a/div[2]/img') is not None :
            driver.find_element(By.XPATH,
                                 f'//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[{i}]/a/div[2]/img').click()
            try:
                ActionChains(driver).move_to_element(
                    driver.find_element(By.XPATH, f'//*[@id="main"]/div/div/aside/div/div[2]/button')).click().perform()
            except:
                ActionChains(driver).move_to_element(
                    driver.find_element(By.XPATH,
                                        f'//*[@id="main"]/div[1]/div/aside/div/div[2]/button')).click().perform()

            time.sleep(10)
            driver.implicitly_wait(5)
            if "fastcampus.co.kr/products/" in driver.current_url:
                if not driver.find_elements(By.XPATH, '/html/body/main/section/div/h2/span'):
                    print("주문서 페이지 이상")
                else:
                    print("주문서 페이지 Pass")
                    exit(0)
            else:
                print("구매 페이지 진입 실패")
                exit(1)
        else : pass


    # try :
    #     ActionChains(driver).move_to_element(
    #     driver.find_element(By.XPATH, f'//*[@id="main"]/div/div/aside/div/div[2]/button')).click().perform()
    # except :
    #     ActionChains(driver).move_to_element(
    #     driver.find_element(By.XPATH, f'//*[@id="main"]/div[1]/div/aside/div/div[2]/button')).click().perform()
    #
    # time.sleep(10)
    # driver.implicitly_wait(5)
    # if "fastcampus.co.kr/products/" in driver.current_url :
    #     if not driver.find_elements(By.XPATH,'/html/body/main/section/div/div[1]/section[1]/dl/dd[1]') :
    #         print("주문서 페이지 이상")
    #     else : pass
    # else :
    #     print("구매 페이지 진입 실패")

if __name__ == '__main__' :
    PurchasePage()
