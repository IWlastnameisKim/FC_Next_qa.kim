import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
def login1test() :
    driver = webdriver.Chrome()

    driver.get('https://fastcampus.co.kr/')
    driver.implicitly_wait(5)
    time.sleep(5)
    driver.maximize_window()
    driver.implicitly_wait(2)
    time.sleep(2)

    def popupclose() :
        try:
            driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/button').click() #팝업 닫기 버튼 선택
        except:
            pass
    def LoginCHK() :
        if not driver.find_elements(By.XPATH, '/html/body/div[2]/header/div/div[2]/div/a') : #로그인 버튼이 안보인다면
            if driver.find_element(By.XPATH, '/html/body/div[2]/header/div/div[2]/div/div[1]/em').text == "김인원님" :
                print("로그인 상태") #로그인된 계정
            else :
                print("로그인 버튼 미노출")
                exit(1)
        else : print("로그인 버튼 노출")
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
    except : print("로그인 페이지 이상 있음")

    try :
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
    except Exception as LoginERR :
        print(LoginERR)

    driver.implicitly_wait(5)
    time.sleep(3)
    popupclose()


    if not driver.find_elements(By.XPATH, '/html/body/div[2]/header/div/div[2]/div/div[1]/em'):
        print("로그인 이상")
        exit(1)
    else:
        if driver.find_element(By.XPATH, '/html/body/div[2]/header/div/div[2]/div/div[1]/em').text == "김인원님" :
            print(driver.find_element(By.XPATH, '/html/body/div[2]/header/div/div[2]/div/div[1]/em').text+"으로 로그인 성공")
        else :
            print("로그인 된 계정 정보 상이함")
            exit(1)


    try :
        driver.find_element(By.XPATH, '/html/body/div[2]/header/div/div[2]/div/div[1]/em').click()
        print(driver.find_element(By.XPATH, '/html/body/div[2]/header/div/div[2]/div/div[3]/div[1]/a').text +"정상 노출") #내 강의 보기
        print(driver.find_element(By.XPATH, '/html/body/div[2]/header/div/div[2]/div/div[3]/div[2]/a').text + "정상 노출") #결제 대기 강의
        print(driver.find_element(By.XPATH, '/html/body/div[2]/header/div/div[2]/div/div[3]/div[3]/a').text + "정상 노출") # 거래 내역
        print(driver.find_element(By.XPATH, '/html/body/div[2]/header/div/div[2]/div/div[3]/div[5]/a').text + "정상 노출") # 로그 아웃
        # A = 1
        # MypageDropdown = f'/html/body/div[1]/header/div/div[2]/div/div[3]/div[{A}]'
        # while True :
        #     if not driver.find_elements(By.XPATH, MypageDropdown) :
        #         break
        #     else : A +=1

    except Exception as MypageError1 :
        print(MypageError1)

    try :
        driver.find_element(By.XPATH, '/html/body/div[2]/header/div/div[2]/div/div[1]/em').click()
        driver.find_element(By.XPATH, '/html/body/div[2]/header/div/div[2]/div/div[3]/div[1]/a').click()
        driver.implicitly_wait(3)
        time.sleep(3)
        if not driver.find_elements(By.XPATH, '/html/body/div[2]/div/div[2]/button') : pass
        else:
            try: driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/button').click()
            except : pass
        if not "/me/course" in driver.current_url :
            print("로그인 > 내 강의 보기 페이지 진입 FAIL")
        else : print("로그인 > 내 강의 보기 페이지 진입 PASS")
    except Exception as LoginCourse :
        print(LoginCourse)
        driver.get('https://fastcampus.co.kr')

    try :
        driver.find_element(By.XPATH, '/html/body/div[2]/header/div/div[2]/div/div[1]/em').click()
        driver.find_element(By.XPATH, '/html/body/div[2]/header/div/div[2]/div/div[3]/div[2]/a').click()
        driver.implicitly_wait(3)
        time.sleep(3)
        if not driver.find_elements(By.XPATH, '/html/body/div[2]/div/div[2]/button') : pass
        else:
            try: driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/button').click()
            except : pass
        if not "/me/enrolled" in driver.current_url :
            print("로그인 > 결제 대기 강의 페이지 진입 FAIL")
        else : print("로그인 > 결제 대기 강의 페이지 진입 PASS")
    except Exception as LoginEnroll :
        print(LoginEnroll)
        driver.get('https://fastcampus.co.kr')

    try :
        driver.find_element(By.XPATH, '/html/body/div[2]/header/div/div[2]/div/div[1]/em').click()
        driver.find_element(By.XPATH, '/html/body/div[2]/header/div/div[2]/div/div[3]/div[3]/a').click()
        driver.implicitly_wait(5)
        time.sleep(5)
        if not driver.find_elements(By.XPATH, '/html/body/div[2]/div/div[2]/button') : pass
        else:
            try: driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/button').click()
            except : pass
        if not "/me/payment/paid" in driver.current_url :
            print("로그인 > 거래 내역 페이지 진입 FAIL")
        else : print("로그인 > 거래 내역 페이지 진입 PASS")
    except Exception as LoginPaid :
        print(LoginPaid)
        driver.get('https://fastcampus.co.kr')


    try :
        driver.find_element(By.XPATH, '/html/body/div[2]/header/div/div[2]/div/div[1]/em').click()
        driver.find_element(By.XPATH, '/html/body/div[2]/header/div/div[2]/div/div[3]/div[5]/a').click()
        driver.implicitly_wait(5)
        time.sleep(5)
        if not driver.find_elements(By.XPATH, '/html/body/div[2]/div/div[2]/button') : pass
        else:
            try: driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/button').click()
            except : pass
        if not driver.find_elements(By.XPATH, '/html/body/div[2]/header/div/div[2]/div/div[1]/em') :
            try :
                driver.find_element(By.XPATH, '/html/body/div[2]/header/div/div[2]/div/a')
                print("로그아웃 성공")
            except Exception as LogoutERR :
                print(LogoutERR)
    except Exception as LogoutERR :
        print(LogoutERR)
        driver.get('https://fastcampus.co.kr')

    driver.close()

if __name__ == '__main__' :
    login1test()