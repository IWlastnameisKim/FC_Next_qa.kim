import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
def FCFooter1() :

    driver = webdriver.Chrome()

    driver.get('https://fastcampus.co.kr/')
    driver.implicitly_wait(5)
    time.sleep(5)
    driver.maximize_window()
    driver.implicitly_wait(2)
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/button').click()
    except:
        pass
    driver.execute_script('window.scrollTo(0,  document.body.scrollHeight);')
    driver.implicitly_wait(3)
    time.sleep(1)
    driver.execute_script('window.scrollTo(0,  document.body.scrollHeight);')
    driver.implicitly_wait(3)
    time.sleep(1)



    #페이지 푸터 메뉴
    excelfile = 'FC_FOOTER.xlsx'
    df = pd.read_excel(excelfile, engine='openpyxl', sheet_name='FooterURL')
    df2 = pd.read_excel(excelfile, engine='openpyxl', sheet_name='FooterText')
    Footer_column_name = 'Footer_Menu'

    for i in range(1,8) :
        try :
                tempfooter = f'//*[@id="footer"]/div[2]/div/ul/li[{i}]/a'
                footer_element = driver.find_element(By.XPATH, tempfooter)
                if footer_element.text in df[Footer_column_name].values:
                    row_footerelement_x = df[df[Footer_column_name] == footer_element.text]
                    footer_landing_url = row_footerelement_x.iloc[0, 1]
                    footer_name = row_footerelement_x.iloc[0, 0]
                    footer_element.click()
                    driver.implicitly_wait(5)
                    time.sleep(2)
                    if len(driver.window_handles) > 1:
                        driver.switch_to.window(driver.window_handles[1])
                        if footer_landing_url in driver.current_url :
                            print(f'{footer_name}'+" 정상 진입")
                        else :
                            print(f'{footer_name}'+" 진입 FAIL")
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])
                    else:
                        if footer_landing_url in driver.current_url :
                            print(f'{footer_name}'+" 정상 진입")
                        else :
                            print(f'{footer_name}'+" 진입 FAIL")
                    driver.get('https://fastcampus.co.kr/')
                    driver.implicitly_wait(5)
                    time.sleep(2)
                    driver.maximize_window()
                    driver.implicitly_wait(2)
                    time.sleep(2)
                    driver.execute_script('window.scrollTo(0,  document.body.scrollHeight);')
                    driver.implicitly_wait(3)
                    time.sleep(1)
                    driver.execute_script('window.scrollTo(0,  document.body.scrollHeight);')
                    driver.implicitly_wait(3)
                    time.sleep(1)
                    try:
                        driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/button').click()
                    except :
                        pass
                else : print("엑셀 파일 내 메뉴이름 없음")
        except Exception as ac :
                print(ac)
    time.sleep(5)

    driver.close()

if __name__ == '__main__' :
    FCFooter1()



