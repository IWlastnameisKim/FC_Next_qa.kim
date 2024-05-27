import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
def FCBOSanity() :
    driver = webdriver.Chrome()

    '''
    스크립트 시나리오 : 
    1. 메뉴명과 url을 속성값으로 테이블 생성(엑셀파일로 대체)
    2. 반복문 실행
    1) BO 좌측 메뉴 갯수 만큼 반복
    2) 좌측 메뉴 선택한 랜딩 페이지 url 확인 (엑셀파일과 비교)
    3) 랜딩 페이지 내 리스트의 항목이 있을 경우 맨 위의 항목 선택
    4) 항목 상세 선택하여 랜딩된 페이지 url 비교 (항목 ID와 메뉴명)
    4-1) 리스트 내 항목이 없다면 다음 메뉴 선택
    
    *메뉴 변경 발생 시 엑셀파일 내용 변경 필요!
    '''

    driver.get("https://fastcampus.day1co.kr/#/login")  # FC BO 접속(환경에 따라 URL 변경필요)

    driver.maximize_window()
    driver.implicitly_wait(5)  # 윈도우 창 크기 최대로 하고 페이지 불러오기 완료후 5초대기
    driver.find_element(By.XPATH, '/html/body/div/div/form/div[1]/input').send_keys(('qa.kim')) # ID 입력(테스터의 ID로 변경 필요)
    #여기부터 유효하지 않은 비밀번호로 로그인 시도
    driver.find_element(By.XPATH, '/html/body/div/div/form/div[2]/input').send_keys(
        ('qlalfq'))
    driver.find_element(By.XPATH, '/html/body/div/div/form/div[3]/button').click()
    if not driver.find_elements(By.XPATH, '/html/body/div/div/p') : print("로그인 실패 문구 미노출")
    if str("home") in driver.current_url :
        print("주의!!!! 유효하지 않은 비밀번호로 로그인 성공함")
        exit(1)
    else: print("유효하지 않은 비밀번호 로그인 PASS")
    #유효하지 않은 비밀번호 로그인 테스트 종료

    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div/div/form/div[2]/input').clear()
    driver.find_element(By.XPATH, '/html/body/div/div/form/div[2]/input').send_keys(
        ('qlalfqjsgh1!'))  # 비밀번호 입력(ID에 맞는 비밀번호로 변경 필요)
    driver.find_element(By.XPATH, '/html/body/div/div/form/div[3]/button').click()  # 로그인 버튼 클릭
    driver.implicitly_wait(5)
    time.sleep(5)

    listNo = len(driver.find_elements(By.XPATH, '/html/body/section/nav[2]/div/ul/li'))  # BO 좌측 메뉴 리스트 갯수
    time.sleep(5)
    excel_file = 'FC_BO_TABLE.xlsx'  # 메뉴와 URL 리스트를 입력한 엑셀 파일 이름 지정 필요
    df = pd.read_excel(excel_file, engine='openpyxl')
    column_name = 'menu_name'

    for Y in range(1, listNo + 1):
        element_selector = f'#navMenu > div > ul > li:nth-child({Y}) > a'
        element_x = driver.find_element(By.CSS_SELECTOR, element_selector)
        # 좌측 메뉴 리스트 1번째 항목부터 선택하기 위한 반복문 조건 설정

        try:
            element_x.click()  # 좌측 메뉴 선택
            time.sleep(5)
            try:
                print(driver.switch_to.alert.text)
                time.sleep(2)
                driver.switch_to.alert.accept()

            except:
                pass

            if element_x.text in df[column_name].values:  # 메뉴 이름을 엑셀 파일내 "menu_name" 컬럼에 존재여부 확인
                row_with_element_x = df[df[column_name] == element_x.text]  # 엑셀 파일내에서 메뉴 이름이 있는 행을 'row_with_element_x'로 지정
                next_column_index = df.columns.get_loc(column_name) + 1  # 엑펠 파일내에서 메뉴 이름이 있는 열의 1칸 오른쪽을 'next_clumn_index'로 지정
                landing_url = row_with_element_x.iloc[0, next_column_index]
                # row_with_element_x 행의 오른쪽 열 값을 landing_url로 지정
                print(f'메뉴명 : {element_x.text}.')
                # print(f'Selected "landing_url": {landing_url}')
                if landing_url in driver.current_url:
                    print(f'{element_x.text}'+"의 랜딩페이지 PASS")
                else:
                    print(f'{element_x.text}'+"의 랜딩페이지 FAIL")
                driver.implicitly_wait(10)
                time.sleep(5)
                i = 0
                while i<2:

                    try:
                        driver.find_element(By.XPATH,
                                        '//*[@id="main"]/section/section/div/table/tbody/tr[1]/td[1]')

                        top_item_chk = driver.find_elements(By.XPATH,
                                                        '//*[@id="main"]/section/section/div/table/tbody/tr[1]/td[1]')  # 리스트 내 항목 존재 유무 체크용
                        top_item = driver.find_element(By.XPATH,
                                                   '//*[@id="main"]/section/section/div/table/tbody/tr[1]/td[1]')  # 리스트 최상단 항목
                        i+=2
                    except:
                        try:
                            driver.find_elements(By.XPATH,
                                             '//*[@id="main"]/section/section/table/tbody/tr[1]/td[1]')

                            top_item_chk = driver.find_elements(By.XPATH,
                                                            '//*[@id="main"]/section/section/table/tbody/tr[1]/td[1]')
                            top_item = driver.find_element(By.XPATH, '//*[@id="main"]/section/section/table/tbody/tr[1]/td[1]')
                            i += 2
                        except:
                            try:
                                driver.find_elements(By.XPATH,
                                                     '//*[@id="main"]/section/div/div/table/tbody/tr[1]/td[1]')
                                top_item_chk = driver.find_elements(By.XPATH,
                                                                    '//*[@id="main"]/section/div/div/table/tbody/tr[1]/td[1]')
                                top_item = driver.find_element(By.XPATH,
                                                               '//*[@id="main"]/section/div/div/table/tbody/tr[1]/td[1]')
                                i += 2
                            except:
                                try:
                                    driver.find_elements(By.XPATH, '//*[@id="main"]/section/div/div/table/tbody/tr/td[1]')
                                    top_item_chk = driver.find_elements(By.XPATH,
                                                                       '//*[@id="main"]/section/div/div/table/tbody/tr/td[1]')
                                    top_item = driver.find_element(By.XPATH,
                                                                   '//*[@id="main"]/section/div/div/table/tbody/tr/td[1]')
                                    i += 2
                                except:
                                    i+=1
                                    driver.implicitly_wait(10)
                                    time.sleep(10)

                    else :  pass

                if top_item_chk is not None:  # 리스트내 항목이 있다면 아래의 절차 실행
                    def Itemch():
                        ItemID = top_item.text  # 리스트 최상단 항목의ID를 ItemID로 선언
                        top_item.click()  # 리스트 최상단 항목 선택
                        driver.implicitly_wait(5)
                        time.sleep(5)
                        if ItemID and landing_url in driver.current_url:  # 랜딩된 페이지가 선택한 항목의 ID와 메뉴명이 있다면 PASS
                            print(f'{element_x.text}'+"의 상세페이지 PASS")
                        else:
                            print(f'{element_x.text}'+"의 상세페이지 이동 FAIL")

                        try:
                            driver.find_element(By.CSS_SELECTOR, '#main > section > section > div > div > table > tbody > tr:nth-child(1) > td')
                            if driver.find_element(By.CSS_SELECTOR, '#main > section > section > div > div > table > tbody > tr:nth-child(1) > td').text == "" :
                                print("상세페이지 항목 FAIL")
                            else : print("상세페이지 항목 PASS")
                        except :
                            try :

                                driver.find_element(By.CSS_SELECTOR, '#main > section > section > div.d-flex.flex-wrap > div:nth-child(1) > dl > dd:nth-child(2)')
                                if driver.find_element(By.CSS_SELECTOR, '#main > section > section > div.d-flex.flex-wrap > div:nth-child(1) > dl > dd:nth-child(2)').text == "":
                                    print("상세페이지 항목 FAIL")
                                else:
                                    print("상세페이지 항목 PASS")
                            except: print("상세페이지 항목 FAIL")




                    Itemch()
                else : print("리스트 항목 없음")







            else:
                print(f'메뉴명:" {element_x.text}이 엑셀 파일에 없음".')

        except Exception as e:
                (print(f'Error: {e}'))

    driver.close()
if __name__ == '__main__'  :
    FCBOSanity()
