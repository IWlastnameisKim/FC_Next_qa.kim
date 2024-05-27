import time


from selenium import webdriver
from selenium.webdriver.common.by import By

def MyCourse() :
    driver = webdriver.Chrome()

    driver.get('https://fastcampus.co.kr') #테스트 환경에 따라 주소 변경 필요!!
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

    driver.get('https://fastcampus.co.kr/me/course')
    time.sleep(3)
    if not driver.find_elements(By.XPATH, '//*[@id="main"]/div/section/div/section/div[3]/div[1]/div/div/div[2]/button') :
        print("수강 가능한 강의 없음")

    else :
        driver.find_element(By.XPATH, '//*[@id="main"]/div/section/div/section/div[3]/div[1]/div/div/div[2]/button').click() #강의시청하기 선택
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(5)
        if not driver.find_elements(By.CSS_SELECTOR, 'body > div.classroom-page > div:nth-child(2) > div > section > div > div > button.btn.close') :
            try:
                driver.find_element(By.CSS_SELECTOR,'body > div.classroom-container > div > div > aside > nav > svg').click()
            except:
                pass
            # 강의장 하단 내비 메뉴 선택 후 팝업창 노출 확인

            time.sleep(3)

            for CourseNavi in range(1, 6):
                CourseNavimenu = f'/html/body/div[2]/div/main/ul/li[{CourseNavi}]/label'
                driver.find_element(By.XPATH, CourseNavimenu).click()
                time.sleep(3)
                CourseNavimenuName = driver.find_element(By.XPATH, CourseNavimenu).text

                try:
                    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/aside/article/h2')
                except:
                    print(driver.find_element(By.XPATH, CourseNavimenu.text + "의 팝업창 열리지 않음"))
                    exit(1)

                if not driver.find_element(By.XPATH,
                                           '//html/body/div[2]/div/div/aside/article/h2').text == CourseNavimenuName:
                    print(CourseNavimenuName + " 팝업창 제목 미노출")

                else:
                    print(CourseNavimenuName + " 팝업창 정상 노출")
                    driver.find_element(By.CSS_SELECTOR,
                                        'body > div.classroom-container > div > div > aside > nav > svg').click()

            try:
                driver.find_element(By.CSS_SELECTOR, 'body > div.classroom-container > div > main > div > div.sc-a52635da-0.fCUAcT.classroom-video-player > div > iframe').click()
                time.sleep(10)
                # ActionChains(driver).move_to_element(driver.find_element((By.CLASS_NAME, 'kollus__viewer'))).perform()
                driver.find_element(By.CLASS_NAME, 'fc-player player')
                time.sleep(3)
                print("영상 플레이어 노출 확인")
            except:
                print("영상 플레이어 미노출")

            try:
                driver.find_element(By.XPATH,
                                    '/html/body/div[2]/div/main/div/div[2]/div[1]/button[1]/span')  # 이전 강의
                print("이전 강의 버튼 노출")
            except:
                print("이전 강의 버튼 미노출")

            try:
                driver.find_element(By.XPATH,
                                    '/html/body/div[2]/div/main/div/div[2]/div[1]/button[2]/span')  # 다음 강의
                print("다음 강의 버튼 노출")
            except:
                print("다음 강의 버튼 미노출")

            try:
                driver.find_element(By.XPATH,
                                    '/html/body/div[2]/div/main/div/div[2]/div[2]/div[1]')  # 화질 설정
                print("화질 설정 버튼 노출")
            except:
                print("화질 설정 버튼 미노출")
            try:
                driver.find_element(By.XPATH,
                                    '/html/body/div[2]/div/main/div/div[2]/div[2]/div[2]/button/span')  # 넓은화면 > 엘레멘트 텍스트로 비교
                print("화면 조정 버튼 노출")
            except:
                print("화면 조정 버튼 미노출")

            try:
                driver.find_element(By.XPATH,
                                    '/html/body/div[2]/div/main/div/div[2]/div[2]/div[1]').click()  # 화질 설정
                time.sleep(3)
                driver.find_element(By.XPATH,
                                    '/html/body/div[2]/div/main/div/div[2]/div[2]/div[1]/ul/li[1]')  # 1080p
                driver.find_element(By.XPATH,
                                    '/html/body/div[2]/div/main/div/div[2]/div[2]/div[1]/ul/li[2]')
                driver.find_element(By.XPATH,
                                    '/html/body/div[2]/div/main/div/div[2]/div[2]/div[1]/ul/li[3]')
                driver.find_element(By.XPATH,
                                    '/html/body/div[2]/div/main/div/div[2]/div[2]/div[1]/ul/li[4]')  # 720p , 540p, 360p
                driver.find_element(By.XPATH,
                                    '/html/body/div[2]/div/main/div/div[2]/div[2]/div[1]/ul/li[5]')

                print("해상도 정상 노출")

                # 현재 해상도
            except:
                print("해상도 노출 비정상")

            if not driver.find_elements(By.XPATH,
                                        '/html/body/div[2]/div/aside/div[1]/div[1]/div/div/div[1]'):
                try:
                    driver.find_elements(By.XPATH,
                                         '/html/body/div[2]/div/aside/div[1]/div[1]/div/div[1]/div[1]')
                    print("강의 목자 노출 PASS")
                except:
                    print("강의 목차 노출 FAIL")
            else:
                print("강의 목차 노출 PASS")

            time.sleep(3)

            if driver.find_element(By.XPATH,
                                   '/html/body/div[2]/div/main/div/div[2]/div[2]/div[2]/button/span').text == "넓은 화면":
                driver.find_element(By.XPATH,
                                    '/html/body/div[2]/div/main/div/div[2]/div[2]/div[2]/button/span').click()
                time.sleep(2)
                if driver.find_element(By.XPATH,
                                       '/html/body/div[2]/div/main/div/div[2]/div[2]/div[2]/button/span').text == "기본 화면":
                    print("화면 확대 PASS")
                else:
                    print("화면 확대 FAIL")
            elif driver.find_element(By.XPATH,
                                     '/html/body/div[2]/div/main/div/div[2]/div[2]/div[2]/button/span').text == "기본 화면":
                driver.find_element(By.XPATH,
                                    '/html/body/div[2]/div/main/div/div[2]/div[2]/div[2]/button/span').click()
                time.sleep(2)
                if driver.find_element(By.XPATH,
                                       '/html/body/div[2]/div/main/div/div[2]/div[2]/div[2]/button/span').text == "넓은 화면":
                    print("화면 축소 PASS")
                else:
                    print("화면 축소 FAIL")
            time.sleep(3)
            if driver.find_element(By.XPATH,
                                   '/html/body/div[2]/div/main/div/div[2]/div[2]/div[2]/button/span').text == "넓은 화면":
                driver.find_element(By.XPATH,
                                    '/html/body/div[2]/div/main/div/div[2]/div[2]/div[2]/button/span').click()
                time.sleep(2)
                if driver.find_element(By.XPATH,
                                       '/html/body/div[2]/div/main/div/div[2]/div[2]/div[2]/button/span').text == "기본 화면":
                    print("화면 확대 PASS")
                else:
                    print("화면 확대 FAIL")
            elif driver.find_element(By.XPATH,
                                     '/html/body/div[2]/div/main/div/div[2]/div[2]/div[2]/button/span').text == "기본 화면":
                driver.find_element(By.XPATH,
                                    '/html/body/div[2]/div/main/div/div[2]/div[2]/div[2]/button/span').click()
                time.sleep(2)
                if driver.find_element(By.XPATH,
                                       '/html/body/div[2]/div/main/div/div[2]/div[2]/div[2]/button/span').text == "넓은 화면":
                    print("화면 축소 PASS")
                else:
                    print("화면 축소 FAIL")

            ####작성 중######
            # 1) 강의장 진입시 '이어보기' 선택 !!<완료>!!
            # 2) 다른 목차(다음 or 이전)이동 후 '처음부터' 선택
            # 3) 선택하려는 목차가 현재 재생 중이라면????
            # 4) 현재 재생중인 목차 판별하기 (어떻게 하지?????!!매우중요!!)
            # 5) 노트 작성
            # 6) 작성한 노트 텍스트, 수정버튼, 삭제 버튼 확인
            # 7) 작성한 노트 채널명 및 재생 버튼 확인
            # 8) 수정 버튼 선택 후 문구 입력 > 수정하기 선택 > 문구입력 > 변경 문구 확인
            # 9) 삭제 버튼 선택 후 '확인' 선택
            # 10) 질의응답 게시판 진입




        else :
            try :
                print("3개 이상의 기기가 등록되어 있어 테스트 종료함")
                driver.find_element(By.CSS_SELECTOR, 'body > div.classroom-page > div:nth-child(2) > div > section > div > div > button.btn.close').click()
                time.sleep(2)
                driver.switch_to.window(driver.window_handles[0])

            except : pass





    time.sleep(2)
    driver.close()



if __name__ == '__main__':
    MyCourse()



# if not driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/aside/div[1]/div[1]/div/div/div[1]/p') :
#     driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/main/div/div[2]/div[2]/div[2]/span').click()
#     time.sleep(2)
#     try :
#         driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/aside/div[1]/div[1]/div/div/div[1]/p')
#         print("화면 축소 PASS")
#     except :
#         print("화면 축소 FAIL")
# else :
#     driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/main/div/div[2]/div[2]/div[2]/span').click()
#     time.sleep(2)
#     try :
#         driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/aside/div[1]/div[1]/div/div/div[1]/p')
#         print("화면 확대 PASS")
#     except :
#         print("화면 확대 FAIL")
