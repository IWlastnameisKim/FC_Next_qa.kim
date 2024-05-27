import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
def HomeMenuAndCarousel() :
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

    #로고 노출 확인
    def WWWCategoryMenu() :
        try :
            driver.find_element(By.CSS_SELECTOR, 'body > div.header-new__wrapper.header-new__wrapper--theme-light > header > div > h1 > a > svg')
            print("로고 정상 출력")
        except : print("로고 미출력")

        try : #카테고리 드롭박스 메뉴 확인
            driver.find_element(By.XPATH, '/html/body/div[2]/header/nav/div/div[1]/div/div/span')
            print("카테고리 메뉴 노출")
        except : print("카테고리 메뉴 미노출")
        try : #포커스 메뉴 확인
            for a in range(1,len(driver.find_elements(By.XPATH, '/html/body/div[2]/header/nav/div/div[1]/ul/li'))+1) :
                Homevisual_no = f'/html/body/div[2]/header/nav/div/div[1]/ul/li[{a}]/a'
                HomeMenu = driver.find_element(By.XPATH, Homevisual_no)
                print(f'{HomeMenu.text}'+" 정상 노출")
        except Exception as HMEr :
            print(HMEr)
        try : #운영 메뉴 확인
            for b in range(1,3) :
                Homevisual_no2 = f'/html/body/div[2]/header/nav/div/div[2]/a[{b}]'
                driver.find_element(By.XPATH, Homevisual_no2)
                print(driver.find_element(By.XPATH, Homevisual_no2).text+" 메뉴 정상 노출")
        except : print("Error")

    WWWCategoryMenu()
    try : #메인배너 테스트
        driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/div/button[2]').click() #일시 정지 선택
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/span[1]').click() #1번째 슬라이드로 이동
        time.sleep(1)
    except Exception as Error1 :
        print(Error1)

    def CarouselTest_Next() :
        CroueCount = 0
        N = 1

        while True :

            i = f'/html/body/div[3]/div[1]/div[2]/span[{N}]'
            HeaderCount = f'/html/body/div[3]/div[2]/div/div[{N}]/a/div/div[1]/div/h3'
            FooterCount = f'/html/body/div[3]/div[2]/div/div[{N}]/a/div/div[1]/div/p'
            driver.find_elements(By.XPATH, i)
            driver.find_elements(By.XPATH, HeaderCount)
            driver.find_elements(By.XPATH, FooterCount)
            CroueCount += 1
            if driver.find_elements(By.XPATH, HeaderCount) : print(f'{N}'+"번째 슬라이드 헤더 PASS")
            elif not driver.find_elements(By.XPATH, HeaderCount) : pass
            if driver.find_elements(By.XPATH, FooterCount): print(f'{N}' + "번째 슬라이드 푸터 PASS")
            elif not driver.find_elements(By.XPATH, FooterCount): pass
            if not driver.find_elements(By.XPATH, i) :
                print(f'{CroueCount-1}'+"번째 슬라이드까지 이상 없음")
                break
            N +=1
            driver.find_element(By.CSS_SELECTOR, 'body > div.main-banner-carousel > div.main-banner-carousel__control-wrapper > div.main-banner-carousel__navigation > button.main-banner-carousel__navigation--next > svg').click()
            time.sleep(1)


        print("슬라이드 총 갯수 : "+f'{CroueCount-1}')
    CarouselTest_Next()
    driver.close()
if __name__ == '__main__' :
    HomeMenuAndCarousel()
# def CarouselTest_Previous() :
#     driver.find_element(By.XPATH, '//*[@id="slick-slide-control00"]').click()
#     CroueCount = 0
#     N = 0
#
#     while True :
#
#         i = f'//*[@id="slick-slide-control{str(N).zfill(2)}"]'
#         driver.find_elements(By.XPATH, i)
#         CroueCount += 1
#         N +=1
#
#         time.sleep(1)
#
#         if not driver.find_elements(By.XPATH, i) :
#             break
#     for a in range(CroueCount, 1, -1) :
#         driver.find_element(By.XPATH, '//*[@id="main"]/div/article/section/div/div[2]/div/div/button[1]').click()
#         HeaderCount = f'//*[@id="slick-slide{str({a-2}).zfill(2)}"]/div/div/div/a/div/div/p'
#         FooterCount = f'//*[@id="slick-slide{str({a-2}).zfill(2)}"]/div/div/div/a/div/div/p'
#         driver.find_elements(By.XPATH, HeaderCount)
#         driver.find_elements(By.XPATH, FooterCount)
#         print(a-2)
#
#         if driver.find_elements(By.XPATH, HeaderCount):
#             print(f'{a-1}' + "번째 슬라이드 헤더 PASS")
#         elif not driver.find_elements(By.XPATH, HeaderCount):
#             print(f'{a-1}' + "번째 슬라이드 헤더 FAIL")
#         if driver.find_elements(By.XPATH, FooterCount):
#             print(f'{N-1}' + "번째 슬라이드 푸터 PASS")
#         elif not driver.find_elements(By.XPATH, FooterCount):
#             print(f'{N-1}' + "번째 슬라이드 푸터 FAIL")
#







#캐로우즈 -> 갯수만큼 반복 : 캐로우즈 헤더와 푸터 텍스트 존재
#캐로우즈 일시 정지 > 현재의 캐로우즈 헤더와 푸터 텍스트 5초 뒤 확인 > 다음 버튼 > 헤더/푸터 텍스트 확인 > 5초 후 같은 텍스트인지 확인 > 이전 버튼 > 텍스트 확인
#카테고리 메뉴 확인(1depth, 비로그인 상태)
#카테고리 메뉴 확인(1depth, 로그인 상태)
#카테고리 메뉴 하위 depth 확인(가능한가?)
#검색창에 입력하여 검색 시 랜딩url로 체크 (강의가 있는것, 없는 것 1회씩 진행)
#검색창 검색 후 검색 내역 노출 확인

#Body 콘텐츠형 메뉴는 변화가 심하여 자동화 불가해보임