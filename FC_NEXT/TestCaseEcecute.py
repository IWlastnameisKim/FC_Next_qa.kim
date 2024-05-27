import time
from selenium import webdriver
import unittest
import pandas as pd
from selenium.webdriver.common.by import By
import Login1, Login2, HomeSearch, HomeMenuAndCarousel, HomeCategory, FCFooter1, FCFooter2, MyCourse, FCBO_Sanity, Purchase_Page


if __name__ == '__main__' :
    Login1.login1test()
    Login2.Login2()
    HomeMenuAndCarousel.HomeMenuAndCarousel()
    HomeCategory.HomeCategory()
    HomeSearch.HomeSearch()
    FCFooter1.FCFooter1()
    FCFooter2.FCFooter2()
    MyCourse.MyCourse()
    Purchase_Page.PurchasePage()
    print("FC BO 테스트 시작")
    FCBO_Sanity.FCBOSanity()

    ###결과 슬랙으로 보내기 배우기
    ###슬랙으로 보낼 결과 필터링 배우기
