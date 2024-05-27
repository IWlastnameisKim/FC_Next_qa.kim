import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def Login2() :
    driver = webdriver.Chrome()

    driver.get('https://fastcampus.co.kr')
    driver.implicitly_wait(5)
    time.sleep(5)
    driver.maximize_window()
    driver.implicitly_wait(2)
    time.sleep(2)
    def popupclose() :
        try:
            driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/button').click()
        except:
            pass

    popupclose()
    try :
        driver.find_element(By.XPATH, '/html/body/div[2]/header/div/div[2]/div/a').click()
        driver.find_element(By.XPATH, '//*[@id="user-email"]')
        driver.find_element(By.XPATH, '//*[@id="user-password"]')
    except : print("로그인 페이지 이상 있음")

    try :
        driver.find_element(By.XPATH, '//*[@id="user-email"]').click()
        driver.find_element(By.XPATH, '//*[@id="user-email"]').send_keys("qa.kim@day1company.co.kr")
        driver.find_element(By.XPATH, '//*[@id="user-password"]').click()
        driver.find_element(By.XPATH, '//*[@id="user-password"]').send_keys("qlalfqjsgh1!")
        driver.find_element(By.XPATH, '/html/body/div[2]/section/div/form/div[2]/button').click()
        driver.implicitly_wait(2)
        time.sleep(2)
    except Exception as LoginERR :
        print(LoginERR)

    if not driver.find_elements(By.XPATH, '/html/body/div[2]/header/div/div[2]/div/div[1]/em'):
        print("로그인 이상")
        exit(1)
    else:
        if driver.find_element(By.XPATH, '/html/body/div[2]/header/div/div[2]/div/div[1]/em').text == "김인원님" :
            print(driver.find_element(By.XPATH, '/html/body/div[2]/header/div/div[2]/div/div[1]/em').text+"으로 로그인 성공")
        else :
            print("로그인 된 계정 정보 상이함")
            exit(1)
    popupclose()
    try :
        driver.find_element(By.XPATH, '/html/body/div[2]/header/div/div[2]/div/div[1]/em').click()
        driver.find_element(By.XPATH, '/html/body/div[2]/header/div/div[2]/div/div[3]/div[1]/a').click()
        driver.implicitly_wait(3)
        time.sleep(3)
        if not driver.find_elements(By.XPATH, '/html/body/div[5]/div/div[2]/button') : pass
        else:
            try: driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/button').click()
            except : pass
        if not "/me/course" in driver.current_url :
            print("로그인 > 내 강의 보기 페이지 진입 FAIL")
        else : print("로그인 > 내 강의 보기 페이지 진입 PASS")
    except Exception as LoginCourse :
        print(LoginCourse)
        driver.get('https://fastcampus.co.kr')


    for N in range(1,10) : #마이페이지 좌측메뉴 위에서부터 차례대로 선택하여 url 비교
        MeSubmenu = f'//*[@id="main"]/div/section/div/div/nav/ul/li[{N}]'
        SelectMemenu = driver.find_element(By.XPATH, MeSubmenu)
        excelfile = 'FC_Mypage.xlsx'
        df = pd.read_excel(excelfile, engine='openpyxl', sheet_name='Mypage')
        Mypagesubmenu = df[df['MyPage_Sub']==SelectMemenu.text]
        landingurl = Mypagesubmenu.iloc[0,1]


        SelectMemenu.click()
        driver.implicitly_wait(3)
        time.sleep(2)
        if len(driver.window_handles) > 1 : #탭이 1개 더 생길 경우에 대한 예외 처리
            driver.switch_to.window(driver.window_handles[1])
            if landingurl in driver.current_url :
                print(Mypagesubmenu.iloc[0,0] + " 진입 PASS")
                driver.close()
                driver.implicitly_wait(3)
                time.sleep(2)
                driver.switch_to.window(driver.window_handles[0])
                driver.implicitly_wait(3)
                time.sleep(2)
            else :
                print(Mypagesubmenu.iloc[0,0] + " 진입 FAIL")
                driver.close()
                driver.implicitly_wait(3)
                time.sleep(2)
                driver.switch_to.window(driver.window_handles[0])
                driver.get('https://fastcampus.co.kr/me/course')
                driver.implicitly_wait(3)
                time.sleep(2)
        else :
            if not driver.find_elements(By.XPATH, '/html/body/div[5]/div/div[2]/button'):
                pass
            else:
                try:
                    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/button').click()
                except:
                    pass
            if landingurl in driver.current_url :
                print(Mypagesubmenu.iloc[0,0]+ " 진입 PASS")
            else :
                print(Mypagesubmenu.iloc[0,0]+ " 진입 FAIL")

    driver.close()
if __name__ == '__main__' :
    Login2()



