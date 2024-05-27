import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
def FCFooter2() :
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
    driver.execute_script('window.scrollTo(0,  document.body.scrollHeight);')
    driver.implicitly_wait(3)
    time.sleep(1)
    driver.execute_script('window.scrollTo(0,  document.body.scrollHeight);')
    driver.implicitly_wait(3)
    time.sleep(1)
    #1. 캐로우즈 : 일시 정지 선택 > 캐로우즈 1~맨끝 까지 선택하며 캐로우즈 헤더/푸터 문구 존재여부 확인
    #2. 검색창 : 검색창 선택후 강의 입력 > 랜딩 url 확인 > 바디 내 강의 항목 존재 체크 > 검생창에서 다른강의 검색 > 랜딩 url 확인 > 바디 내 강의 항목 존재 체크 >
                #최근검색어 1 선택 > 랜딩 페이지 확인 > 바디 내 항목 존재 체크

    excelfile = 'FC_FOOTER.xlsx'
    df = pd.read_excel(excelfile, engine='openpyxl', sheet_name='FooterURL')
    df2 = pd.read_excel(excelfile, engine='openpyxl', sheet_name='FooterText')
    Footer_text = 'FooterText'
    Footerdetail = 'Footerdetail'

    for a in range(1,3) :
        for b in range(1,4):
            try :
                footert = f'//*[@id="footer"]/div[2]/div/div[2]/dl[{a}]/dt[{b}]'
                footerdeatil = f'//*[@id="footer"]/div[2]/div/div[2]/dl[{a}]/dd[{b}]'
                if a == 2 and b == 3 :
                    pass
                else:
                    textfooter = driver.find_element(By.XPATH, footert).text
                    textfooterdetail = driver.find_element(By.XPATH, footerdeatil).text
                    if textfooter in df2[Footer_text].values :
                        footername_index = df2[df2[Footer_text] == textfooter]
                        footername = footername_index.iloc[0,0]
                        if textfooterdetail in df2[Footerdetail].values :
                            footernamedetail = footername_index.iloc[0,1]
                            print(footername +" "+ footernamedetail)
                        else : print(footername)

                    else : print("엑셀 문서에 "+f'{textfooter}'+"이 없음")
            except Exception as error01 :
                print(error01)
    #
    #

    for f in range(1,4):
        try :
            footertli1 = f'//*[@id="footer"]/div[2]/div/div[4]/ul/li[{f}]'
            textfooterli1 = driver.find_element(By.XPATH, footertli1).text
            if textfooterli1 in df2[Footer_text].values :
                footertli1_index = df2[df2[Footer_text] == textfooterli1]
                footerli1name = footertli1_index.iloc[0,0]
                print(footerli1name)
            else : print("엑셀 문서에 "+f'{textfooterli1}'+"이 없음")
        except Exception as Error1 :
            print(Error1)

    for z in range(1,4) :
        try :
            footerli2 = f'//*[@id="footer"]/div[2]/div/div[4]/dl/dt[{z}]'
            footerli2deatil = f'//*[@id="footer"]/div[2]/div/div[4]/dl/dd[{z}]'
            textfooterli2 = driver.find_element(By.XPATH, footerli2).text
            textfooterli2deatil = driver.find_element(By.XPATH, footerli2deatil).text

            if textfooterli2 in df2[Footer_text].values :
                footerli2name_index = df2[df2[Footer_text] == textfooterli2]
                footerl2name = footerli2name_index.iloc[0,0]
                if textfooterli2deatil in df2[Footerdetail].values :
                    footerli2detailname_index = df2[df2[Footerdetail]==textfooterli2deatil]
                    footerli2detailname = footerli2detailname_index.iloc[0,1]
                    print(footerl2name +" "+ footerli2detailname)
                else : print(footerl2name)

            else : print("엑셀 문서에 "+f'{textfooterli2}'+"이 없음")
        except Exception as error01 :
            print(error01)

    try :
        driver.find_element(By.XPATH, '//*[@id="footer"]/div[2]/div/div[4]/dl/dd[3]/a').click()
        driver.implicitly_wait(5)
        time.sleep(2)

        if "storage.googleapis.com/static.fastcampus.co.kr/prod/uploads/202110/151443-146" in driver.current_url :
            print("572호 정상 진입")

        else : print(driver.current_url)


    except Exception as OchiliErr :
        print(f'{OchiliErr}')


    driver.close()
if __name__ == '__main__' :
    FCFooter2()
