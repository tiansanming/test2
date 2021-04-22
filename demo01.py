import pytest
from selenium import webdriver
import time
import allure

class Test_error_login:

    def test_C001001(self):

        print('\n用例 C001001: 不输入账号登录')

        # 实例化浏览器 如果为空就是是用的项目根目录的Chrome驱动
        allure.step("1 实例化浏览器 如果为空就是是用的项目根目录的Chrome驱动")
        borwser = webdriver.Chrome("E:\soft\driver\chromedriver_win32\chromedriver.exe")
        # 请求网址
        allure.step("2 请求网址")
        borwser.get('http://test.lemonban.com/ningmengban/app/login/login.html')
        # 隐式等待 每隔半秒请求
        allure.step("3 隐式等待 每隔半秒请求")
        borwser.implicitly_wait(10)
        # 窗口放大
        allure.step("4 窗口放大")
        borwser.maximize_window()
        # 点击密码框
        allure.step("5 点击密码框")
        borwser.find_element_by_id('password').click()
        borwser.find_element_by_id('password').send_keys('zzc222736')
        time.sleep(2)
        # 点击登陆
        allure.step("6 点击登陆")
        borwser.find_element_by_id('login-button').click()
        time.sleep(2)
        tes = borwser.find_element_by_xpath('//*[@id="myform"]/div[4]/p').text
        print(tes)
        allure.step("7 校验")
        assert tes == '用户名不能为空。'

    def test_C001002(self):
        print('\n用例 C001002: 正确的账号不输入密码')

        # 实例化浏览器 如果为空就是是用的项目根目录的Chrome驱动
        borwser = webdriver.Chrome("E:\soft\driver\chromedriver_win32\chromedriver.exe")
        # 请求网址
        borwser.get('http://test.lemonban.com/ningmengban/app/login/login.html')
        # 隐式等待 每隔半秒请求
        borwser.implicitly_wait(10)
        # 窗口放大
        borwser.maximize_window()
        # 点击账号框
        borwser.find_element_by_id('username').click()
        borwser.find_element_by_id('username').send_keys('13409222222')
        time.sleep(2)
        # 点击登陆
        borwser.find_element_by_id('login-button').click()
        time.sleep(2)
        tes = borwser.find_element_by_xpath('//*[@id="myform"]/div[4]/p').text

        print(tes)
        assert tes == '密码不能为空。'

    def test_C001003(self):
        print('\n用例 C001002: 正确的账号不输入密码')

        # 实例化浏览器 如果为空就是是用的项目根目录的Chrome驱动
        borwser = webdriver.Chrome("E:\soft\driver\chromedriver_win32\chromedriver.exe")
        # 请求网址
        borwser.get('http://test.lemonban.com/ningmengban/app/login/login.html')
        # 隐式等待 每隔半秒请求
        borwser.implicitly_wait(10)
        # 窗口放大
        borwser.maximize_window()
        # 点击账号框
        borwser.find_element_by_id('username').click()
        borwser.find_element_by_id('username').send_keys('13409222222')
        time.sleep(2)
        # 点击登陆
        borwser.find_element_by_id('login-button').click()
        time.sleep(2)
        tes = borwser.find_element_by_xpath('//*[@id="myform"]/div[4]/p').text

        print(tes)
        assert tes == '密码不能为空1。'

    def test_C001004(self):
        print('\n用例 C001003: 错误的账号正确的密码')

        # 实例化浏览器 如果为空就是是用的项目根目录的Chrome驱动
        borwser = webdriver.Chrome()
        # 请求网址
        borwser.get('http://test.lemonban.com/ningmengban/app/login/login.html')
        # 隐式等待 每隔半秒请求
        borwser.implicitly_wait(10)
        # 窗口放大
        borwser.maximize_window()
        # 点击账号框
        borwser.find_element_by_id('username').click()
        borwser.find_element_by_id('username').send_keys('13409222222')
        borwser.find_element_by_id('password').click()
        borwser.find_element_by_id('password').send_keys('zzc222736')
        time.sleep(2)
        # 点击登陆
        borwser.find_element_by_id('login-button').click()
        time.sleep(2)
        alertText = borwser.switch_to.alert.text
        print(alertText + '+打印效果')
        assert alertText == '该手机号没有注册'